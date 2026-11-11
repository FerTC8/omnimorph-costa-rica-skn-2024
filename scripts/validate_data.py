#!/usr/bin/env python3
"""Validador de esquema, paridad JSON/CSV/MD/SVG, invariantes y enlaces para OMNIMORPH v2."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FILES = [
    ".gitignore",
    "README.md",
    "ANALISIS_PARTIDO.md",
    "FUENTES.md",
    "datos/ficha_partido.json",
    "datos/alineaciones.json",
    "datos/alineaciones.csv",
    "datos/estadisticas.json",
    "datos/estadisticas.csv",
    "datos/goles_y_eventos.json",
    "datos/goles_y_eventos.csv",
    "assets/esquemas_tacticos.svg",
    "assets/timeline_partido.svg",
    "assets/uniformes_y_zonas.svg",
    "scripts/validate_data.py",
]

REQUIRED_SVGS = [
    "assets/esquemas_tacticos.svg",
    "assets/timeline_partido.svg",
    "assets/uniformes_y_zonas.svg",
]

FORBIDDEN_PATTERNS = [
    (r"\bgenerad[oa]s?\b", "uso de 'generado/a'"),
    (r"\bsintetizad[oa]s?\b", "uso de 'sintetizado/a'"),
    (r"\ba continuaci[oó]n\b", "uso de 'a continuación'"),
    (r"\bcabe destacar\b", "muletilla 'cabe destacar'"),
    (r"\bsin lugar a dudas\b", "muletilla 'sin lugar a dudas'"),
    (r"\ben conclusi[oó]n\b", "muletilla 'en conclusión'"),
]

EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]")


class ValidationError(Exception):
    pass


def load_json(rel_path: str) -> dict:
    with open(ROOT / rel_path, encoding="utf-8") as f:
        return json.load(f)


def load_csv(rel_path: str) -> list[dict[str, str]]:
    with open(ROOT / rel_path, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def check_files_and_svgs(errors: list[str]) -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).is_file():
            errors.append(f"Falta archivo obligatorio: {rel}")

    readme_path = ROOT / "README.md"
    readme_txt = readme_path.read_text(encoding="utf-8") if readme_path.is_file() else ""

    for svg_rel in REQUIRED_SVGS:
        svg_path = ROOT / svg_rel
        if svg_rel not in readme_txt:
            errors.append(f"README.md no referencia el gráfico requerido: {svg_rel}")
        if svg_path.is_file():
            try:
                tree = ET.parse(svg_path)
                root_tag = tree.getroot().tag
                if not root_tag.endswith("svg"):
                    errors.append(f"Raíz XML inesperada en {svg_rel}: {root_tag}")
            except ET.ParseError as exc:
                errors.append(f"XML inválido en {svg_rel}: {exc}")


def check_lineups_and_subs(
    alineaciones: dict, eventos: dict, errors: list[str]
) -> None:
    al_csv = load_csv("datos/alineaciones.csv")
    csv_by_key = {(r["codigo"], int(r["dorsal"])): r for r in al_csv}

    expected_count = 0
    for team_key, team_name in [
        ("costa_rica", "Costa Rica"),
        ("san_cristobal_y_nieves", "San Cristóbal y Nieves"),
    ]:
        t = alineaciones["equipos"][team_key]
        code = t["codigo"]
        titulares = t["titulares"]
        suplentes = t["suplentes"]

        if len(titulares) != 11:
            errors.append(f"{code}: se esperaban 11 titulares, hay {len(titulares)}")
        if len(suplentes) != 12:
            errors.append(f"{code}: se esperaban 12 suplentes, hay {len(suplentes)}")

        all_players = titulares + suplentes
        expected_count += len(all_players)

        dorsals = [p["dorsal"] for p in all_players]
        if len(dorsals) != len(set(dorsals)):
            errors.append(f"{code}: dorsales duplicados en alineaciones.json")

        captains = [p for p in all_players if p["capitan"]]
        if len(captains) != 1 or captains[0]["dorsal"] != t["capitan"]["dorsal"]:
            errors.append(f"{code}: inconsistencia en capitán")

        active_count = sum(1 for p in all_players if p["participo"])
        if active_count != 16:
            errors.append(f"{code}: se esperaban 16 participantes con minutos, hay {active_count}")

        for p in all_players:
            key = (code, p["dorsal"])
            if key not in csv_by_key:
                errors.append(f"alineaciones.csv omite jugador {key}")
                continue
            r = csv_by_key[key]
            checks = [
                ("equipo", team_name),
                ("director_tecnico", t["director_tecnico"]),
                ("nombre", p["nombre"]),
                ("nombre_fifa", p["nombre_fifa"]),
                ("posicion_linea", p["posicion_linea"]),
                ("rol_tactico", p["rol_tactico"]),
                ("capitan", "true" if p["capitan"] else "false"),
                ("titular", "true" if p["titular"] else "false"),
                ("participo", "true" if p["participo"] else "false"),
                ("entro_minuto", "" if p["entro_minuto"] is None else str(p["entro_minuto"])),
                ("salio_minuto", "" if p["salio_minuto"] is None else str(p["salio_minuto"])),
                ("minutos_jugados", str(p["minutos_jugados"])),
                ("goles", str(p["goles"])),
                ("asistencias", str(p["asistencias"])),
                ("tarjeta_amarilla", "" if p["tarjeta_amarilla"] is None else p["tarjeta_amarilla"]),
                ("tarjeta_roja", "" if p["tarjeta_roja"] is None else p["tarjeta_roja"]),
                ("fifa_id_player", p["fifa_id_player"]),
                ("estado", p["estado"]),
            ]
            for col, expected_val in checks:
                if r[col] != expected_val:
                    errors.append(
                        f"Paridad alineaciones.csv {key} columna {col}: '{r[col]}' != '{expected_val}'"
                    )

    if len(al_csv) != expected_count:
        errors.append(f"alineaciones.csv tiene {len(al_csv)} filas, se esperaban {expected_count}")

    subs = eventos["sustituciones"]
    if len(subs) != 10:
        errors.append(f"Se esperaban 10 sustituciones, hay {len(subs)}")

    sub_out_map: dict[tuple[str, int], int] = {}
    sub_in_map: dict[tuple[str, int], int] = {}
    for s in subs:
        code = s["codigo"]
        team_key = "costa_rica" if code == "CRC" else "san_cristobal_y_nieves"
        tit_map = {p["dorsal"]: p for p in alineaciones["equipos"][team_key]["titulares"]}
        sup_map = {p["dorsal"]: p for p in alineaciones["equipos"][team_key]["suplentes"]}

        d_out = s["sale"]["dorsal"]
        d_in = s["entra"]["dorsal"]
        minute = s["minuto"]

        if d_out not in tit_map:
            errors.append(f"Cambio {s['orden']}: dorsal saliente #{d_out} ({code}) no es titular")
        else:
            po = tit_map[d_out]
            if po["nombre"] != s["sale"]["nombre"]:
                errors.append(f"Cambio {s['orden']}: nombre saliente no coincide")
            if po["salio_minuto"] != minute or po["minutos_jugados"] != minute:
                errors.append(f"Cambio {s['orden']}: minutos de salida inconsistentes para #{d_out}")
            sub_out_map[(code, d_out)] = minute

        if d_in not in sup_map:
            errors.append(f"Cambio {s['orden']}: dorsal entrante #{d_in} ({code}) no es suplente")
        else:
            pi = sup_map[d_in]
            if pi["nombre"] != s["entra"]["nombre"]:
                errors.append(f"Cambio {s['orden']}: nombre entrante no coincide")
            if pi["entro_minuto"] != minute or pi["minutos_jugados"] != 90 - minute:
                errors.append(f"Cambio {s['orden']}: minutos jugados inconsistentes para #{d_in}")
            sub_in_map[(code, d_in)] = minute

    for team_key in ("costa_rica", "san_cristobal_y_nieves"):
        t = alineaciones["equipos"][team_key]
        code = t["codigo"]
        for p in t["titulares"]:
            if (code, p["dorsal"]) not in sub_out_map and p["minutos_jugados"] != 90:
                errors.append(f"{code} #{p['dorsal']} titular sin cambio debe tener 90 min")
        for p in t["suplentes"]:
            if (code, p["dorsal"]) not in sub_in_map and (p["minutos_jugados"] != 0 or p["participo"]):
                errors.append(f"{code} #{p['dorsal']} suplente sin ingreso debe tener 0 min")


def check_events_and_scores(
    ficha: dict, alineaciones: dict, eventos: dict, estadisticas: dict, errors: list[str]
) -> None:
    marc = ficha["marcador"]
    for side in ("costa_rica", "san_cristobal_y_nieves"):
        mt = marc["medio_tiempo"][side]
        st_p = marc["segundo_tiempo_parcial"][side]
        ft = marc["final"][side]
        if mt + st_p != ft:
            errors.append(f"Marcador {side}: {mt} + {st_p} != {ft}")

    goles = eventos["goles"]
    crc_goals = [g for g in goles if g["codigo"] == "CRC"]
    skn_goals = [g for g in goles if g["codigo"] == "SKN"]
    if len(crc_goals) != marc["final"]["costa_rica"] or len(skn_goals) != marc["final"]["san_cristobal_y_nieves"]:
        errors.append("Cantidad de goles en goles_y_eventos.json no coincide con ficha_partido.json")

    for g in goles:
        coords = g["zona_remate_fuente_oficial"]["coordenadas_fifa_norm"]
        if not (0.0 <= coords["x_0_100"] <= 100.0 and 0.0 <= coords["y_0_100"] <= 100.0):
            errors.append(f"Coordenadas fuera de rango [0,100] en gol {g['numero']}")

    # Paridad goleadores/asistencias en alineaciones.json y estadisticas.json
    for team_key, code in [("costa_rica", "CRC"), ("san_cristobal_y_nieves", "SKN")]:
        team_goals = [g for g in goles if g["codigo"] == code]
        g_by_dorsal: dict[int, int] = {}
        a_by_dorsal: dict[int, int] = {}
        for g in team_goals:
            g_by_dorsal[g["autor"]["dorsal"]] = g_by_dorsal.get(g["autor"]["dorsal"], 0) + 1
            if g["asistencia"]:
                a_by_dorsal[g["asistencia"]["dorsal"]] = a_by_dorsal.get(g["asistencia"]["dorsal"], 0) + 1

        for p in alineaciones["equipos"][team_key]["titulares"] + alineaciones["equipos"][team_key]["suplentes"]:
            if p["goles"] != g_by_dorsal.get(p["dorsal"], 0):
                errors.append(f"Goles de {code} #{p['dorsal']} en alineaciones.json no coinciden con eventos")
            if p["asistencias"] != a_by_dorsal.get(p["dorsal"], 0):
                errors.append(f"Asistencias de {code} #{p['dorsal']} en alineaciones.json no coinciden con eventos")

        for sp in estadisticas["estadisticas_jugadores"][team_key]:
            if sp["participo"] and not sp["es_portero"]:
                if sp["goles"] != g_by_dorsal.get(sp["dorsal"], 0):
                    errors.append(f"Goles de {code} #{sp['dorsal']} en estadisticas.json no coinciden con eventos")
                if sp["asistencias"] != a_by_dorsal.get(sp["dorsal"], 0):
                    errors.append(f"Asistencias de {code} #{sp['dorsal']} en estadisticas.json no coinciden con eventos")

    # Tarjetas amarillas
    yc_ev = {(y["codigo"], y["dorsal"], y["minuto"]) for y in eventos["tarjetas_amarillas"]}
    yc_al = set()
    for team_key, code in [("costa_rica", "CRC"), ("san_cristobal_y_nieves", "SKN")]:
        for p in alineaciones["equipos"][team_key]["titulares"] + alineaciones["equipos"][team_key]["suplentes"]:
            if p["tarjeta_amarilla"]:
                yc_al.add((code, p["dorsal"], p["tarjeta_amarilla"]))
    if yc_ev != yc_al:
        errors.append(f"Tarjetas amarillas difieren entre eventos {yc_ev} y alineaciones {yc_al}")

    # Paridad goles_y_eventos.csv
    ev_csv = load_csv("datos/goles_y_eventos.csv")
    csv_goals = [r for r in ev_csv if r["tipo_evento"] == "gol"]
    csv_yc = [r for r in ev_csv if r["tipo_evento"] == "tarjeta_amarilla"]
    csv_subs = [r for r in ev_csv if r["tipo_evento"] == "sustitucion"]

    if len(csv_goals) != len(goles):
        errors.append(f"goles_y_eventos.csv tiene {len(csv_goals)} goles, esperados {len(goles)}")
    else:
        for g, rg in zip(goles, csv_goals):
            asist_name = g["asistencia"]["nombre"] if g["asistencia"] else ""
            if (
                rg["minuto"] != f"{g['minuto_oficial']}'"
                or int(rg["reloj_segundos"]) != g["reloj_espn_segundos"]
                or int(rg["dorsal_principal"]) != g["autor"]["dorsal"]
                or rg["jugador_principal"] != g["autor"]["nombre"]
                or rg["jugador_secundario"] != asist_name
                or rg["parte_cuerpo"] != g["parte_del_cuerpo"]
                or float(rg["coord_fifa_x"]) != g["zona_remate_fuente_oficial"]["coordenadas_fifa_norm"]["x_0_100"]
                or float(rg["coord_fifa_y"]) != g["zona_remate_fuente_oficial"]["coordenadas_fifa_norm"]["y_0_100"]
            ):
                errors.append(f"Desajuste en gol {g['numero']} dentro de goles_y_eventos.csv")

    if len(csv_yc) != len(eventos["tarjetas_amarillas"]):
        errors.append("Cantidad de amarillas en goles_y_eventos.csv no coincide con JSON")
    if len(csv_subs) != len(eventos["sustituciones"]):
        errors.append("Cantidad de sustituciones en goles_y_eventos.csv no coincide con JSON")

    # Orden cronológico estricto por (orden_cronologico, mitad, minuto_num)
    prev_key = (0, 0)
    for idx, r in enumerate(ev_csv, 1):
        if int(r["orden_cronologico"]) != idx:
            errors.append(f"orden_cronologico discontinuo en fila {idx} de goles_y_eventos.csv")
        mit_rank = 1 if r["mitad"] == "1T" else 2
        cur_key = (mit_rank, int(r["minuto_num"]))
        if cur_key < prev_key:
            errors.append(f"goles_y_eventos.csv fuera de orden cronológico en fila {idx}: {cur_key} < {prev_key}")
        prev_key = cur_key


def check_statistics(ficha: dict, eventos: dict, estadisticas: dict, errors: list[str]) -> None:
    eq = estadisticas["estadisticas_equipo"]
    tot = eq["total"]
    t1 = eq["primer_tiempo"]
    t2 = eq["segundo_tiempo"]

    # 1. Suma 1T + 2T == Total para métricas absolutas
    for k in t1:
        if k == "estado" or k.endswith("_pct"):
            continue
        for team in ("costa_rica", "san_cristobal_y_nieves"):
            v1 = t1[k][team]
            v2 = t2[k][team]
            vt = tot[k][team]
            if v1 + v2 != vt:
                errors.append(f"1T + 2T != Total en {k} ({team}): {v1} + {v2} != {vt}")

    # 2. Invariantes matemáticas en Total, 1T, 2T
    period_goals = {
        "total": (ficha["marcador"]["final"]["costa_rica"], ficha["marcador"]["final"]["san_cristobal_y_nieves"]),
        "primer_tiempo": (ficha["marcador"]["medio_tiempo"]["costa_rica"], ficha["marcador"]["medio_tiempo"]["san_cristobal_y_nieves"]),
        "segundo_tiempo": (ficha["marcador"]["segundo_tiempo_parcial"]["costa_rica"], ficha["marcador"]["segundo_tiempo_parcial"]["san_cristobal_y_nieves"]),
    }

    for periodo, (g_crc, g_skn) in period_goals.items():
        blk = eq[periodo]
        goals_map = {"costa_rica": g_crc, "san_cristobal_y_nieves": g_skn}
        opp_map = {"costa_rica": "san_cristobal_y_nieves", "san_cristobal_y_nieves": "costa_rica"}
        for team in ("costa_rica", "san_cristobal_y_nieves"):
            opp = opp_map[team]
            g = goals_map[team]
            saves_opp = blk["atajadas"][opp]
            sot = blk["tiros_a_puerta"][team]
            soff = blk["tiros_fuera"][team]
            sblk = blk["tiros_bloqueados"][team]
            stot = blk["tiros_totales"][team]
            s_in = blk["tiros_dentro_area"][team]
            s_out = blk["tiros_fuera_area"][team]
            posts = blk["tiros_al_poste"][team]

            if g + saves_opp > sot:
                errors.append(
                    f"Invariante violada ({periodo} {team}): goles({g}) + atajadas_rival({saves_opp}) > tiros_a_puerta({sot})"
                )
            if sot + soff + sblk != stot:
                errors.append(
                    f"Desglose tiros ({periodo} {team}): {sot}+{soff}+{sblk} != {stot}"
                )
            if s_in + s_out != stot:
                errors.append(
                    f"Ubicación tiros ({periodo} {team}): {s_in}+{s_out} != {stot}"
                )
            if posts > stot:
                errors.append(f"Postes ({posts}) > tiros totales ({stot}) en {periodo} {team}")

            if blk["duelos_suelo_ganados"][team] + blk["duelos_aereos_ganados"][team] != blk["duelos_ganados"][team]:
                errors.append(f"Suma duelos ({periodo} {team}) inconsistente")
            if (
                blk["pases_precisos_campo_propio"][team] + blk["pases_precisos_campo_rival"][team]
                != blk["pases_precisos"][team]
            ):
                errors.append(f"Suma pases por campo ({periodo} {team}) inconsistente")
            if blk["pases_precisos"][team] > blk["pases_intentados"][team]:
                errors.append(f"Pases precisos > intentados ({periodo} {team})")

    # 3. Suma de estadísticas individuales == totales de equipo
    for team in ("costa_rica", "san_cristobal_y_nieves"):
        active = [p for p in estadisticas["estadisticas_jugadores"][team] if p["participo"]]
        field = [p for p in active if not p["es_portero"]]
        gks = [p for p in active if p["es_portero"]]

        sum_checks = [
            ("tiros_totales", sum(p["tiros_totales"] for p in field), tot["tiros_totales"][team]),
            ("tiros_a_puerta", sum(p["tiros_a_puerta"] for p in field), tot["tiros_a_puerta"][team]),
            ("tiros_fuera", sum(p["tiros_fuera"] for p in field), tot["tiros_fuera"][team]),
            ("tiros_bloqueados", sum(p["tiros_bloqueados"] for p in field), tot["tiros_bloqueados"][team]),
            ("tiros_al_poste", sum(p["tiros_al_poste"] for p in field), tot["tiros_al_poste"][team]),
            ("pases_precisos", sum(p["pases_precisos"] for p in active), tot["pases_precisos"][team]),
            ("pases_intentados", sum(p["pases_intentados"] for p in active), tot["pases_intentados"][team]),
            ("atajadas", sum(p["atajadas"] for p in gks), tot["atajadas"][team]),
            ("entradas_tackles", sum(p["entradas_tackles"] for p in active), tot["entradas_tackles"][team]),
            ("intercepciones", sum(p["intercepciones"] for p in active), tot["intercepciones"][team]),
            ("despejes", sum(p["despejes"] for p in active), tot["despejes"][team]),
            ("faltas_cometidas", sum(p["faltas_cometidas"] for p in active), tot["faltas_cometidas"][team]),
        ]
        for label, s_val, t_val in sum_checks:
            if s_val != t_val:
                errors.append(f"Suma individual {label} ({team}): {s_val} != equipo {t_val}")

        rec_total = sum(p["recuperaciones"] for p in active)
        rec_field = sum(p["recuperaciones"] for p in field)
        rec_gk = sum(p["recuperaciones"] for p in gks)
        rec_json = tot["recuperaciones_totales_suma_jugadores"]
        if (
            rec_total != rec_json[team]
            or rec_field != rec_json["solo_jugadores_campo"][team]
            or rec_gk != rec_json["porteros"][team]
        ):
            errors.append(f"Suma recuperaciones ({team}) no coincide con total en estadisticas.json")

    # 4. Paridad estadisticas.json vs estadisticas.csv
    st_csv = load_csv("datos/estadisticas.csv")
    csv_map = {(r["periodo"], r["metrica"]): r for r in st_csv}

    for periodo in ("total", "primer_tiempo", "segundo_tiempo"):
        blk = eq[periodo]
        for k, val in blk.items():
            if k == "estado":
                continue
            if k == "recuperaciones_totales_suma_jugadores":
                checks = [
                    (k, val["costa_rica"], val["san_cristobal_y_nieves"]),
                    ("recuperaciones_jugadores_campo", val["solo_jugadores_campo"]["costa_rica"], val["solo_jugadores_campo"]["san_cristobal_y_nieves"]),
                    ("recuperaciones_porteros", val["porteros"]["costa_rica"], val["porteros"]["san_cristobal_y_nieves"]),
                ]
                for mk, vc, vs in checks:
                    row = csv_map.get((periodo, mk))
                    if not row or str(row["costa_rica"]) != str(vc) or str(row["san_cristobal_y_nieves"]) != str(vs):
                        errors.append(f"Paridad estadisticas.csv fallida en ({periodo}, {mk})")
            else:
                row = csv_map.get((periodo, k))
                if (
                    not row
                    or str(row["costa_rica"]) != str(val["costa_rica"])
                    or str(row["san_cristobal_y_nieves"]) != str(val["san_cristobal_y_nieves"])
                    or row["estado"] != blk["estado"]
                ):
                    errors.append(f"Paridad estadisticas.csv fallida en ({periodo}, {k})")

    for campo in estadisticas["metricas_no_disponibles"]["campos"]:
        row = csv_map.get(("no_disponible", campo))
        if not row or row["estado"] != "no_disponible" or row["costa_rica"] != "no_disponible":
            errors.append(f"Falta métrica no_disponible '{campo}' en estadisticas.csv")


def check_markdown_svg_and_style(errors: list[str]) -> None:
    analisis = (ROOT / "ANALISIS_PARTIDO.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")

    must_have_analisis = [
        "15,700",
        "Gustavo Alfaro",
        "Francisco Molina",
        "Orlando Galo",
        "Josimar Alcócer",
        "Andy Rojas",
        "65.3%",
        "no_disponible",
        "Distancia recorrida",
        "Mapas de calor",
        "xG",
        "PPDA",
        "40'",
        "49'",
        "82'",
        "84'",
    ]
    for token in must_have_analisis:
        if token not in analisis:
            errors.append(f"ANALISIS_PARTIDO.md omite dato clave requerido: '{token}'")

    for token in ["15,700", "Orlando Galo", "Josimar Alcócer", "Andy Rojas", "65.3%", "no_disponible"]:
        if token not in readme:
            errors.append(f"README.md omite dato clave requerido: '{token}'")

    # Etiquetas mínimas de paridad en SVGs
    svg_checks = {
        "assets/esquemas_tacticos.svg": ["Gustavo Alfaro", "F. Molina", "3-4-3", "5-4-1", "65.3%", "34.7%"],
        "assets/timeline_partido.svg": ["Orlando Galo", "Josimar Alcócer", "Andy Rojas", "40'", "49'", "82'", "84'"],
        "assets/uniformes_y_zonas.svg": ["95.1, 56.3", "79.6, 60.5", "94.2, 48.5", "86.5, 41.5", "no_disponible"],
    }
    for svg_rel, tokens in svg_checks.items():
        txt = (ROOT / svg_rel).read_text(encoding="utf-8")
        for token in tokens:
            if token not in txt:
                errors.append(f"{svg_rel} omite etiqueta de paridad: '{token}'")

    # Escaneo de frases prohibidas y emojis decorativos
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        if p.suffix.lower() not in {".md", ".json", ".csv", ".svg"}:
            continue
        txt = p.read_text(encoding="utf-8")
        rel = p.relative_to(ROOT)
        for pat, desc in FORBIDDEN_PATTERNS:
            if re.search(pat, txt, flags=re.IGNORECASE):
                errors.append(f"Frase prohibida ({desc}) detectada en {rel}")
        if EMOJI_RE.search(txt):
            errors.append(f"Emoji decorativo detectado en {rel}")


def check_fuentes_urls(errors: list[str]) -> int:
    txt = (ROOT / "FUENTES.md").read_text(encoding="utf-8")
    urls = sorted(set(re.findall(r"https?://[^\s\)\>\`]+", txt)))
    if not urls:
        errors.append("No se encontraron URLs en FUENTES.md")
        return 0

    for url in urls:
        req = urllib.request.Request(url, headers={"User-Agent": "curl/8.7.1"})
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                if resp.status != 200:
                    errors.append(f"URL devolvió HTTP {resp.status}: {url}")
        except urllib.error.HTTPError as exc:
            errors.append(f"URL devolvió error HTTP {exc.code}: {url}")
        except Exception as exc:
            errors.append(f"Fallo al consultar URL ({exc}): {url}")
    return len(urls)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida paridad JSON/CSV/MD/SVG, invariantes matemáticas y URLs de OMNIMORPH v2."
    )
    parser.add_argument(
        "--check-urls",
        action="store_true",
        help="Verifica en vivo que todas las URLs de FUENTES.md devuelvan HTTP 200.",
    )
    args = parser.parse_args()

    errors: list[str] = []

    check_files_and_svgs(errors)
    if not any("Falta archivo obligatorio" in e for e in errors):
        ficha = load_json("datos/ficha_partido.json")
        alineaciones = load_json("datos/alineaciones.json")
        eventos = load_json("datos/goles_y_eventos.json")
        estadisticas = load_json("datos/estadisticas.json")

        check_lineups_and_subs(alineaciones, eventos, errors)
        check_events_and_scores(ficha, alineaciones, eventos, estadisticas, errors)
        check_statistics(ficha, eventos, estadisticas, errors)
        check_markdown_svg_and_style(errors)

    checked_urls = 0
    if args.check_urls:
        checked_urls = check_fuentes_urls(errors)

    if errors:
        print(f"FALLO DE VALIDACIÓN ({len(errors)} errores):")
        for err in errors:
            print(f"  - {err}")
        return 1

    msg = "VALIDACIÓN OK: archivos, paridad JSON/CSV/MD/SVG, invariantes matemáticas y reglas de estilo aprobadas."
    if args.check_urls:
        msg += f" ({checked_urls} URLs verificadas con HTTP 200)"
    print(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
