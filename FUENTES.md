# Fuentes y Trazabilidad de Datos — Costa Rica 4–0 San Cristóbal y Nieves (2024)

Registro de fuentes consultadas y verificadas en vivo (`HTTP 200`) el **10 de noviembre de 2026 (CST / 2026-11-11 UTC)** para el partido **Costa Rica 4–0 San Cristóbal y Nieves** (Eliminatorias Concacaf rumbo al Mundial 2026, Segunda Ronda, Grupo B, Jornada 1, 6 de junio de 2024 local, Estadio Nacional de Costa Rica, San José).

---

## 1. Fuentes Primarias y Estadísticas Verificadas (`HTTP 200`)

| Fuente | Tipo | URL verificada | Datos que aporta al paquete |
| :--- | :--- | :--- | :--- |
| **FIFA Live API v3 (Acta oficial ES)** | Oficial FIFA (`JSON`) | https://api.fifa.com/api/v3/live/football/520/288301/288302/400017724?language=es | ID oficial FIFA (`400017724`), competición (`520`), fecha UTC/local, asistencia oficial (`15700`), tiempo añadido (`+4'` en 1T y 2T), posesión oficial (`65.3%` vs `34.7%`), terna arbitral guatemalteca completa, técnicos (`Gustavo Alfaro` y `Francisco Molina`), tácticas (`3-4-3` y `5-4-1`), capitanes y plantillas de 23 jugadores por equipo. |
| **FIFA Timelines API v3 (Cronología ES)** | Oficial FIFA (`JSON`) | https://api.fifa.com/api/v3/timelines/520/288301/288302/400017724?language=es | Marcas exactas UTC del pitazo inicial real (`02:39:53.53Z`), descanso (`03:29:01.167Z`), inicio 2T (`03:46:27.89Z`), pitazo final (`04:35:52.893Z`), minuto exacto de los 4 goles (`40'`, `49'`, `82'`, `84'`), 4 amarillas, 10 cambios, atajadas y coordenadas IFES normalizadas `(0..100)` de los eventos. |
| **FIFA Calendar API v3 (Segunda Ronda)** | Oficial FIFA (`JSON`) | https://api.fifa.com/api/v3/calendar/matches?idSeason=288301&idStage=288302&count=100&language=es | Mapeo de temporada (`288301`), etapa (`288302`) y cruce de calendarios del Grupo B. |
| **Concacaf Match Centre (ES)** | Oficial Concacaf (`HTML`) | https://es.concacaf.com/competitions/concacaf-qualifiers/matches/94968cbf476d4bfeb2a75732b5a38ef5/costa-rica-vs-st.-kitts-and-nevis | Centro oficial de partido vigente en el portal de Concacaf (marcador, sede, competición y ficha del encuentro). |
| **Concacaf Match Centre (EN)** | Oficial Concacaf (`HTML`) | https://www.concacaf.com/competitions/concacaf-qualifiers/matches/94968cbf476d4bfeb2a75732b5a38ef5/costa-rica-vs-st.-kitts-and-nevis | Versión en inglés del centro oficial de partido en Concacaf. |
| **Concacaf Crónica Oficial de Jornada** | Oficial Concacaf (`HTML`) | https://www.concacaf.com/competitions/concacaf-qualifiers/news/grenada-bermuda-look-to-add-points-in-day-four-of-concacaf-qualifiers | Confirmación oficial de Concacaf del 4-0 con doblete de Orlando Galo y goles de los suplentes Josimar Alcócer y Andy Rojas. |
| **SKNFA Crónica Oficial** | Federación visitante (`HTML`) | https://sknfa.com/sugar-boyz-fall-to-costa-rica-in-opening-world-cup-qualifier/ | Reporte oficial de la federación de San Cristóbal y Nieves; aporta detalle previo del 1-0 (centro de Brenes tras un saque de banda) y confirmación del desarrollo del encuentro. |
| **FotMob / Opta (Match `4416441`)** | Estadística avanzada (`HTML`/`JSON`) | https://www.fotmob.com/matches/st-kitts-nevis-vs-costa-rica/1bhibc | Fuente completa de estadísticas por equipo separadas en `Total`, `1T` y `2T` (tiros a puerta/fuera/bloqueados/postes, pases precisos/intentados, campo propio/rival, centros, balones largos, entradas, intercepciones, despejes, duelos, regates, atajadas, faltas), parados tácticos (`3-4-2-1` y `5-4-1`), calificación y métricas individuales de los 32 jugadores con minutos (incluido `error_derivado_en_gol: 1` de Archibald y recuperaciones individuales). |
| **ESPN Summary API (`event=698147`)** | Datos deportivos (`JSON`) | https://site.api.espn.com/apis/site/v2/sports/soccer/fifa.worldq.concacaf/summary?event=698147 | Reloj en segundos exactos de goles (`2344s`, `2926s`, `4904s`, `5006s`), `112` entradas de crónica minuto a minuto (`24'` travesaño de Calvo, `74'` travesaño de Ugalde, `73'` atajada de Sequeira a Sawyers, `87'` mano de Calvo), dorsales, posiciones, coordenadas Opta y enlaces a fichas individuales. |
| **ESPN Ficha Web (`698147`)** | Datos deportivos (`HTML`) | https://www.espn.com/soccer/match/_/gameId/698147 | Interfaz web del encuentro con marcadores parciales (`1-0` / `4-0`), asistencia (`15,700`) y alineaciones. |
| **Transfermarkt (`4343320`)** | Base de datos (`HTML`) | https://www.transfermarkt.com/spielbericht/index/spielbericht/4343320 | Cruce de dorsales, partes del cuerpo en los 4 goles, asistencias oficiales y motivos de tarjetas (protestas de Ible y Brenes; faltas de Sterling-James y Maynard). |
| **Wikipedia Concacaf Segunda Ronda** | Referencia secundaria (`HTML`) | https://en.wikipedia.org/wiki/2026_FIFA_World_Cup_qualification_%E2%80%93_CONCACAF_second_round | Contexto de formato, bombos del sorteo basados en Ranking FIFA de diciembre 2023 (CRC #52, SKN #147) y resultados paralelos del Grupo B (`TRI 2-2 GRN`). |

---

## 2. Prensa Costarricense e Internacional Verificada (`HTTP 200`)

| Medio | URL verificada | Aporte principal |
| :--- | :--- | :--- |
| **La Nación (Análisis táctico y rendimiento)** | https://www.nacion.com/puro-deporte/seleccion-nacional/seleccion-de-costa-rica-vs-san-cristobal-y-nieves/IQJDIGMS4BFT3JJRBCU3RXGKE4/story/ | Lectura táctica del partido: lluvia intensa y cancha rápida en La Sabana, 79% de posesión sin remates en los primeros 20 minutos, ajustes pedidos por Gustavo Alfaro, descenso asociativo de Manfred Ugalde (35/39 pases), rol de carrileros y foto real de juego verificando las medias azul marino con banda superior roja. |
| **La Nación (Orlando Galo y vestuario)** | https://www.nacion.com/puro-deporte/seleccion-nacional/orlando-galo-sigue-el-consejo-de-gustavo-alfaro-y/FCHXQYYZPZFU3JWY4QZZ6D6DLA/story/ | Instrucción táctica de Alfaro tras el amistoso contra Uruguay para la llegada desde segunda línea de Galo y fotografía real bajo la lluvia con el uniforme Adidas 2024 y parche Concacaf. |
| **Everardo Herrera (Crónica y alineaciones)** | https://everardoherrera.com/index.php/futbol-costa-rica/115698-costa-rica-arranca-la-eliminatoria-goleando-a-san-cristobal-y-nieves | Confirmación de roles en cancha (línea de tres centrales con Jeyland Mitchell, Quirós y Lassiter por bandas, contención Galo-Brenes), detalle de la mala salida de Archibald en el 1-0 y crónica de los cuatro goles. |
| **Everardo Herrera (Designación arbitral)** | https://everardoherrera.com/index.php/futbol-costa-rica/115693-conozca-detalles-de-julio-luna-el-arbitro-guatemalteco-que-impartira-justicia-en-el-estadio-nacional-audio | Cuarteto arbitral completo de Guatemala (`Julio Luna`, `Jorge Ordóñez`, `Cristian Alvarado`, `Cristhofer Corado`). |
| **Radio Columbia (Declaraciones DT SKN)** | https://columbia.co.cr/dt-de-san-cristobal-califico-a-costa-rica-como-rival-muy-exigente-con-jugadores-de-calidad | Declaraciones postpartido confirmando al mexicano Francisco Molina como seleccionador de San Cristóbal y Nieves en el Estadio Nacional. |
| **La Teja (Lanzamiento uniforme Adidas 2024)** | https://www.lateja.cr/deportes/fedefutbol-y-adidas-asombran-al-mundo-con/N6HH573PI5AS3G7RDWUW3LALQA/story/ | Diseño oficial de Adidas para Costa Rica 2024 (inspiración en carretas típicas en la camiseta local roja con patrón azul marino). |
| **La Teja (Declaraciones de Galo)** | https://www.lateja.cr/deportes/orlando-galo-dio-fuerte-mensaje-tras-convertirse/KK6RD4WK6ZBTTLHM4U4UIWL4RA/story/ | Fotografía directa del encuentro mostrando a Orlando Galo (#14) con la indumentaria de Costa Rica y detrás al arquero Julani Archibald (#18) con buzo naranja fluorescente, pantaloneta negra, medias naranjas, guantes negros y brazalete de capitán. |
| **Teletica (Declaraciones y foto)** | https://www.teletica.com/la-sele/galo-queremos-triunfar-queremos-alcanzar-grandes-metas_359839 | Fotografía real del encuentro que permite verificar el uniforme de campo de San Cristóbal y Nieves (camiseta verde con banda diagonal negra y pequeñas estrellas, cuello amarillo con ribete blanco, hombros con ribete blanco y pantaloneta verde con detalle amarillo). |
| **FDP Radio (Crónica bajo lluvia)** | https://fdpradio.com/costa-rica-goleo-a-san-cristobal-y-nieves-en-medio-de-un-fuerte-aguacero/ | Contexto de la lluvia torrencial y fotografía del dorsal/espalda de los jugadores de Costa Rica en la celebración. |
| **EFE / Infobae (Cable de agencia)** | https://www.infobae.com/america/agencias/2024/06/07/4-0-costa-rica-golea-a-san-cristobal-y-nieves-en-el-comienzo-de-las-eliminatorias/ | Confirmación independiente de alineaciones, técnico Francisco Molina, amarillas, aproximación de asistencia ("unos 15.000 aficionados") y relato de la resistencia física visitante. |
| **The Tico Times (Crónica EN)** | https://ticotimes.net/2024/06/07/costa-rica-thrashes-saint-kitts-and-nevis-4-0-in-world-cup-qualifier-opener | Descripción del 5-2-3 sin balón de Costa Rica, condiciones húmedas y ventosas de la cancha y ocasión clara de Zamora al 76'. |
| **Puro Periodismo (Crónica)** | https://www.puroperiodismo.com/2024/06/sele-se-da-un-gustazo-4-0-ante-una-debil-st-kitts-nevis-en-el-arranque-de-la-eliminatoria-mundialista/ | Registro del incremento progresivo de la lluvia durante la noche y contexto de las anotaciones. |
| **Fútbol Centroamérica (Kit Adidas)** | https://futbolcentroamerica.com/costarica/para-cuando-uniformes-de-verdad-las-reacciones-ante-la-nueva-camiseta-de-costa-rica | Imagen promocional oficial de FCRF/Adidas mostrando detalle frontal de la camiseta roja y pantaloneta azul marino 2024. |

> **Nota metodológica sobre portales bloqueados:** En la verificación automatizada en vivo del 10/11/2026, tanto `Sofascore` como `FBref` devolvieron `HTTP 403` ante consultas directas. Ningún dato de este repositorio depende de URLs con error o acceso restringido; toda la estadística de equipo, por mitades e individual está respaldada y verificada mediante `FIFA Live API v3`, `FotMob (Opta)`, `ESPN` y `Transfermarkt`. Asimismo, el antiguo enlace de `Concacaf` enlazado desde Wikipedia (`concacaf.com/en/world-cup-qualifying-men/game-details/...`) devuelve `HTTP 404` y se reemplazó aquí por las rutas oficiales vigentes en `concacaf.com`.

---

## 3. Enlaces Oficiales Verificados para Fotos, Planteles y Uniformes

De acuerdo con la política editorial del proyecto, no se redistribuyen fotografías con derechos reservados dentro del repositorio; los diagramas propios van en SVG vectorial y aquí quedan únicamente los enlaces oficiales vivos (`HTTP 200`):

- **Portal oficial Eliminatorias Concacaf en FIFA (ES):** https://www.fifa.com/es/tournaments/mens/worldcup/canadamexicousa2026/qualifiers/concacaf *(SPA oficial FIFA; los datos estructurados se consultan vía los endpoints JSON `api.fifa.com` listados en la Sección 1).*
- **Plantel y fichas oficiales de Costa Rica en Concacaf:** https://es.concacaf.com/competitions/concacaf-qualifiers/teams/costa-rica/roster *(incluye retratos oficiales; advertencia: muestra los dorsales de la convocatoria vigente más reciente, por ejemplo Orlando Galo con otro número distinto al `#14` usado el 6 de junio de 2024).*
- **Perfil oficial de Costa Rica en Concacaf:** https://www.concacaf.com/competitions/concacaf-qualifiers/teams/costa-rica
- **Plantel y fichas oficiales de San Cristóbal y Nieves en Concacaf:** https://es.concacaf.com/competitions/concacaf-qualifiers/teams/st.-kitts-and-nevis/roster *(incluye retratos oficiales de plantilla en la eliminatoria).*
- **Perfil oficial de San Cristóbal y Nieves en Concacaf:** https://www.concacaf.com/competitions/concacaf-qualifiers/teams/st.-kitts-and-nevis
- **Federación Costarricense de Fútbol (FCRF) — Sitio oficial:** https://www.fcrf.cr/
- **FCRF — Tienda oficial (uniformes e indumentaria):** https://www.fcrf.cr/tienda
- **FCRF — Galería oficial:** https://www.fcrf.cr/galer%C3%ADa
- **Asociación de Fútbol de San Cristóbal y Nieves (SKNFA) — Crónica con foto:** https://sknfa.com/sugar-boyz-fall-to-costa-rica-in-opening-world-cup-qualifier/

---

## 4. Tabla de Disponibilidad y Estado por Dato (`confirmado` / `estimacion_tactica` / `no_disponible`)

| Categoría / Métrica | Estado | Fuente o Motivo |
| :--- | :--- | :--- |
| Ficha general (fechas local/UTC, horarios reales de inicio y fin, estadio, marcador MT/FT) | `confirmado` | FIFA Live/Timeline API, Concacaf, FotMob, ESPN |
| Asistencia oficial (`15,700`) | `confirmado` | FIFA Live API, FotMob, ESPN, Wikipedia *(ver discrepancia TM abajo)* |
| Terna arbitral completa (4 oficiales de Guatemala) | `confirmado` | FIFA Live API, Everardo Herrera |
| Directores técnicos (`Gustavo Alfaro` y `Francisco Molina`) | `confirmado` | FIFA Live API, Transfermarkt, EFE, Everardo Herrera, Radio Columbia |
| Condiciones climáticas cualitativas (aguacero y césped rápido/resbaladizo) | `confirmado` | Prensa (La Nación, EFE, FDP Radio, Tico Times) y fotos del partido |
| Campo estructurado `Weather` FIFA y temperatura/viento exactos en °C / km/h | `no_disponible` | `Weather: null` en FIFA API; sin parte meteorológico oficial |
| Alineaciones completas (23 convocados por equipo, dorsales, capitanes, minutos jugados) | `confirmado` | FIFA Live API, FotMob, ESPN, Transfermarkt |
| Los 4 goles (autor, asistencia, parte del cuerpo, minuto exacto, reloj en s, jugada previa) | `confirmado` | FIFA Timeline, ESPN, FotMob, Transfermarkt, SKNFA, prensa |
| Coordenadas normalizadas FIFA/Opta de los 4 goles (`(0..100)` IFES) | `confirmado` | FIFA Timeline API v3 (`Event.PositionX/Y`) y ESPN `keyEvents` |
| Zonas aproximadas de remate en lectura táctica y gestación cualitativa de fases | `estimacion_tactica` | Etiquetado explícito en `datos/alineaciones.json` y `datos/goles_y_eventos.json` |
| Tarjetas amarillas (`4`), expulsiones (`0`) y los `10` cambios | `confirmado` | FIFA Timeline/Bookings/Substitutions, ESPN, FotMob, Transfermarkt |
| Posesión oficial FIFA (`65.3%` CRC vs `34.7%` SKN) y cortes `1T / 2T / Total` (FotMob) | `confirmado` | FIFA Live API (`BallPossession`) y FotMob (`Periods`) |
| Estadísticas colectivas `1T`, `2T` y `Total` (tiros, pases, córners, faltas, fueras de juego, atajadas, duelos, despejes, entradas, bloqueos) | `confirmado` | FotMob (`Periods`: `FirstHalf`, `SecondHalf`, `All`) / Opta |
| Recuperaciones por jugador (`32` participantes) y suma total de equipo (`62` CRC / `59` SKN; campo `57` / `52`) | `confirmado` | FotMob `playerStats` (`Recoveries`) |
| Corte separado `1T` y `2T` de recuperaciones por equipo | `no_disponible` | FotMob publica recuperaciones a nivel jugador en total partido, sin desglose por mitad |
| Estadísticas individuales de campo y portería (minutos, rating FotMob, tiros, pases, toques, chances, acciones defensivas, duelos, atajadas, errores) | `confirmado` | FotMob `playerStats` |
| Uniformes de Costa Rica campo, SKN campo y portero SKN (`#18 Archibald`) | `confirmado` | Verificación visual en fotografías directas del partido (`La Nación`, `La Teja`, `Teletica`, `FDP Radio`) |
| Color exacto del uniforme de portero usado por Patrick Sequeira (`#23 CRC`) el 06/06/2024 | `no_disponible` | Sin fotografía o parte oficial verificado de ese encuentro específico |
| Goles esperados (`xG`), asistencias esperadas (`xA`) y `shotmap` completo de los 28 tiros | `no_disponible` | `content.shotmap` vacío en FotMob y sin módulo `xG` en FIFA API |
| Distancia recorrida (`km`), velocidad máxima (`km/h`), cantidad de `sprints`, tracking `25 fps`, mapas de calor continuos, redes de pases y `PPDA` | `no_disponible` | Sin datos EPTS/tracking públicos en FIFA, Concacaf ni proveedores abiertos |

---

## 5. Registro de Discrepancias entre Fuentes

1. **Asistencia (`15,700` vs `5,150`):** `FIFA Live API`, `FotMob`, `ESPN` y `Wikipedia` confirman `15,700` espectadores (acorde con el cable de `EFE`: *"unos 15.000 aficionados"*). `Transfermarkt` muestra `5.150` porque la ficha `Stadium.CityName` dentro del JSON oficial de `FIFA API` contiene anómalamente el literal `"5150"`, valor que Transfermarkt importó como asistencia.
2. **Director técnico de San Cristóbal y Nieves (`Francisco Molina` vs `Austin Huggins`):** `FotMob` asigna el banquillo visitante a `Austin Huggins`; `FIFA Live API` (`IdCoach: 483207`), `Transfermarkt`, `EFE/Infobae`, `Everardo Herrera` y declaraciones de cancha recogidas por `Radio Columbia` confirman al mexicano **Francisco Molina**.
3. **Fecha calendario (`06/06/2024` vs `07/06/2024`):** En hora local de Costa Rica (`CST, UTC-6`), el partido inició a las `20:30` programadas (`20:39` real) del **6 de junio de 2024**. En horario `UTC` (`02:30Z`), varios listados europeos marcan **7 de junio de 2024**.
4. **Esquema táctico de San Cristóbal y Nieves (`5-4-1` vs `4-4-2 double 6`):** `FIFA`, `FotMob` y `ESPN` registran `5-4-1` (con `Sterling-James` y `Bristow` como laterales/carrileros flanqueando a tres centrales), consistente con las crónicas de bloque bajo de cinco atrás. `Transfermarkt` lo etiqueta como `4-4-2 double 6`.
5. **Redondeo de precisión de pases (`85% / 74%` vs `84% / 73%`):** Sobre idénticos totales (`483/571 = 84.59%` para Costa Rica y `221/300 = 73.67%` para San Cristóbal y Nieves), `FotMob` redondea al entero más cercano (`85%` y `74%`), mientras resúmenes web derivados de ESPN truncan la parte decimal (`84%` y `73%`).
6. **Minutos de goles y sustituciones:** `FIFA Timeline`, `ESPN` (con reloj exacto en segundos), `FotMob` y `Transfermarkt` coinciden en `40'`, `49'`, `82'` y `84'`, mientras el arreglo resumen `HomeTeam.Goals` de `FIFA API` trunca minutos al entero inferior (`39'`, `48'`, `82'`, `83'`) y algunos medios impresos citan `38'`/`39'` (1-0), `48'`/`50'` (2-0) o `81'`/`83'` (3-0). Algo equivalente ocurre con variaciones de 1–2 minutos en sustituciones entre el arreglo `Substitutions` de FIFA y el `Timeline` oficial.
7. **Medias de Costa Rica:** Una previa de *La Nación* describió el uniforme tradicional como *"medias azules"*; las fotografías directas del juego muestran medias **azul marino con banda horizontal roja en el borde superior**.
8. **Dorsales actuales en Concacaf Roster vs 06/06/2024:** La página vigente del plantel de Costa Rica en `concacaf.com` refleja convocatorias posteriores al 6 de junio de 2024 y asigna numeraciones actuales distintas a las actas oficiales de este partido (documentado en `datos/alineaciones.json` con los dorsales reales del 06/06/2024).
