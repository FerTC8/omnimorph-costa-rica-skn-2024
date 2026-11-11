# Análisis y Paquete Narrativo RAG — Costa Rica 4–0 San Cristóbal y Nieves (6 de junio de 2024)

Documento base del encuentro **Costa Rica 4–0 San Cristóbal y Nieves** por la Jornada 1 del Grupo B en la Segunda Ronda de las Eliminatorias Concacaf rumbo al Mundial 2026, disputado el **6 de junio de 2024** (hora local CST) en el Estadio Nacional de Costa Rica, San José.

Cada bloque de este archivo es autocontenido para facilitar la fragmentación (`chunking`) en el chatbot de OMNIMORPH. Todas las métricas mantienen su etiqueta de origen: `confirmado`, `estimacion_tactica` o `no_disponible`.

---

## 1. Ficha Técnica, Contexto Clasificatorio y Condiciones de Juego — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)

### 1.1 Datos generales y horarios del partido Costa Rica vs. San Cristóbal y Nieves (06/06/2024)
- **Partido:** Costa Rica 4–0 San Cristóbal y Nieves (`confirmado`).
- **Competición:** Eliminatorias Concacaf rumbo a la Copa Mundial de la FIFA 2026 — Segunda Ronda, Grupo B, Jornada 1 (`confirmado`).
- **Fecha y hora local (Costa Rica, CST / UTC-6):** Jueves **6 de junio de 2024**; inicio programado a las `20:30`, pitazo inicial real a las `20:39:53` (~10 minutos de retraso según el cronómetro oficial de FIFA Timeline) (`confirmado`).
- **Fecha y marcas horarias UTC:** Viernes **7 de junio de 2024** en horario universal; inicio real `02:39:53.53Z`, fin del primer tiempo `03:29:01.167Z`, inicio del segundo tiempo `03:46:27.89Z` y cierre oficial a las `04:35:52.893Z` (`confirmado`).
- **Tiempo añadido:** `+4'` señalados en el primer tiempo (jugado hasta `45'+5'`) y `+4'` señalados en el segundo tiempo (jugado hasta `90'+5'`) (`confirmado`).
- **Marcadores:** Medio tiempo `Costa Rica 1–0 San Cristóbal y Nieves`; parcial del segundo tiempo `3–0`; marcador final `Costa Rica 4–0 San Cristóbal y Nieves` (`confirmado`).
- **Estadio:** Estadio Nacional de Costa Rica, Parque Metropolitano La Sabana, San José (`35,100` de capacidad de referencia, césped natural, sin techo) (`confirmado`).
- **Asistencia oficial:** `15,700` espectadores (`confirmado` en FIFA Live API, FotMob, ESPN y Wikipedia; el cable de EFE reportó *"unos 15.000 aficionados"*, mientras Transfermarkt muestra `5,150` por un dato erróneo en `Stadium.CityName` de FIFA API).
- **Terna arbitral (Guatemala):** Árbitro central `Julio Luna Guzmán`; Asistente 1 `Jorge Ordóñez`; Asistente 2 `Cristian Esau Alvarado de León`; Cuarto árbitro `Cristhofer Corado` (`confirmado`).
- **Directores técnicos:** `Gustavo Alfaro` (Argentina) en Costa Rica y `Francisco Molina` (México) en San Cristóbal y Nieves (`confirmado` en FIFA API, Transfermarkt, EFE, Everardo Herrera y Radio Columbia; FotMob atribuye erróneamente el banquillo visitante a Austin Huggins).
- **Capitanes:** `Francisco Calvo` (`#15`, Costa Rica) y `Julani Archibald` (`#18`, San Cristóbal y Nieves) (`confirmado`).
- **Identificadores externos del partido:** FIFA Match ID `400017724` (Competición `520`, Temporada `288301`, Etapa `288302`), Concacaf UUID `94968cbf476d4bfeb2a75732b5a38ef5`, FotMob `4416441`, ESPN `698147`, Transfermarkt `4343320` (`confirmado`).

### 1.2 Contexto clasificatorio en el Grupo B (Costa Rica vs. San Cristóbal y Nieves, 06/06/2024)
- **Formato de la Segunda Ronda Concacaf:** 6 grupos de 5 selecciones; cada selección disputa 4 partidos (2 de local y 2 de visita) y avanzan las 2 primeras de cada grupo a la Tercera Ronda (`confirmado`).
- **Integrantes del Grupo B:** Costa Rica, Trinidad y Tobago, San Cristóbal y Nieves, Granada y Bahamas (`confirmado`).
- **Ubicación previa en el sorteo (Ranking FIFA de diciembre de 2023):** Costa Rica llegaba en el puesto **#52** (Bombo 1) y San Cristóbal y Nieves en el puesto **#147** (Bombo 3) (`confirmado`).
- **Resultado paralelo de la Jornada 1:** El 5 de junio de 2024, Trinidad y Tobago y Granada empataron `2–2` en Puerto España. Con el `4–0` ante San Cristóbal y Nieves, Costa Rica tomó el primer lugar del Grupo B con **3 puntos** y **+4** de diferencia de gol (`confirmado`).

### 1.3 Clima, estado de la cancha y uniformes verificados (Costa Rica vs. San Cristóbal y Nieves, 06/06/2024)
- **Condiciones climáticas cualitativas (`confirmado`):** Lluvia intensa y constante (aguacero) durante la noche en La Sabana, con viento y césped natural rápido, pesado y resbaladizo que dificultó el traslado de balón en el arranque.
- **Temperatura, humedad y viento exactos (`no_disponible`):** El campo estructurado `Weather` de la API de FIFA figura como nulo y no hay parte meteorológico oficial con grados Celsius o velocidad del viento en km/h.
- **Uniforme de campo de Costa Rica (`confirmado` por fotos del partido):** Modelo Adidas 2024; camiseta roja con patrón frontal en azul oscuro/vino inspirado en las carretas típicas, cuello redondo azul marino, tres franjas azul marino en hombros, paneles laterales azul marino, dorsales blancos y parches oficiales Concacaf/FIFA; pantaloneta azul marino con franja lateral diagonal roja; medias azul marino con logotipo Adidas blanco y banda superior horizontal roja.
- **Uniforme del portero de Costa Rica (`no_disponible`):** No existe fotografía verificada de Patrick Sequeira (`#23`) correspondiente al 6 de junio de 2024 ni parte de utilería oficial que confirme el color exacto usado esa noche.
- **Uniforme de campo de San Cristóbal y Nieves (`confirmado` por fotos del partido):** Camiseta verde brillante con banda diagonal negra al frente (con tres pequeñas estrellas/puntos decorativos), cuello redondo amarillo con ribete blanco, ribete blanco sobre hombros y dorsales negros en la espalda; pantaloneta verde con detalle amarillo en el borde inferior izquierdo; medias verdes.
- **Uniforme del portero de San Cristóbal y Nieves (`confirmado` por fotos del partido):** Julani Archibald (`#18`, capitán) vistió buzo de manga larga naranja fluorescente con dorsal negro, brazalete blanco/amarillo en la manga derecha, pantaloneta negra sobre licra térmica negra, medias naranjas y guantes negros.

---

## 2. Alineaciones Completas, Capitanes, Tarjetas y Cambios — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)

### 2.1 Alineación completa de Costa Rica (DT: Gustavo Alfaro) — 06/06/2024
Esquema inicial registrado: `3-4-3` (FIFA/ESPN) / `3-4-2-1` (FotMob). Todos los datos de esta tabla tienen estado `confirmado` (base reglamentaria de `90` minutos para el cálculo de minutos jugados).

| Dorsal | Jugador | Posición | Rol táctico | Titular | Minutos | Goles | Asist. | Tarjetas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `23` | Patrick Sequeira | POR | Portero titular | Sí | `90` | `0` | `0` | — |
| `3` | Jeyland Mitchell | DEF | Defensa central derecho | Sí | `90` | `0` | `0` | — |
| `6` | Julio Cascante | DEF | Defensa central (líbero) | Sí | `90` | `0` | `0` | — |
| `15` | Francisco Calvo (C) | DEF | Defensa central izquierdo (Capitán) | Sí | `90` | `0` | `0` | — |
| `22` | Haxzel Quirós | MED | Carrilero derecho | Sí (sale `78'`) | `78` | `0` | `0` | — |
| `11` | Ariel Lassiter | MED | Carrilero izquierdo | Sí | `90` | `0` | `0` | — |
| `13` | Jefferson Brenes | MED | Mediocentro (contención derecho) | Sí (sale `64'`) | `64` | `0` | `1` | Amarilla `58'` |
| `14` | Orlando Galo | MED | Mediocentro (contención izquierdo, box-to-box) | Sí | `90` | `2` | `0` | — |
| `17` | Warren Madrigal | DEL | Mediapunta / extremo derecho | Sí (sale `65'`) | `65` | `0` | `0` | — |
| `21` | Álvaro Zamora | DEL | Mediapunta / extremo izquierdo | Sí (sale `78'`) | `78` | `0` | `0` | — |
| `9` | Manfred Ugalde | DEL | Delantero centro con movilidad | Sí (sale `81'`) | `81` | `0` | `1` | — |
| `10` | Brandon Aguilera | MED | Mediocentro / volante creativo | Suplente (entra `64'`) | `26` | `0` | `0` | — |
| `20` | Josimar Alcócer | DEL | Extremo / mediapunta derecho | Suplente (entra `65'`) | `25` | `1` | `0` | — |
| `2` | Gerald Taylor | DEF | Carrilero derecho | Suplente (entra `78'`) | `12` | `0` | `0` | — |
| `19` | Andy Rojas | DEL | Mediapunta / extremo izquierdo | Suplente (entra `78'`) | `12` | `1` | `0` | — |
| `12` | Joel Campbell | DEL | Delantero / mediapunta | Suplente (entra `81'`) | `9` | `0` | `1` | — |
| `1` | Kevin Chamorro | POR | Portero suplente | No jugó | `0` | `0` | `0` | — |
| `4` | Juan Pablo Vargas | DEF | Defensa central suplente | No jugó | `0` | `0` | `0` | — |
| `5` | Fernán Faerron | DEF | Defensa central suplente | No jugó | `0` | `0` | `0` | — |
| `7` | Anthony Contreras | DEL | Delantero suplente | No jugó | `0` | `0` | `0` | — |
| `8` | Joseph Mora | DEF | Lateral / carrilero izquierdo suplente | No jugó | `0` | `0` | `0` | — |
| `16` | Alejandro Bran | MED | Mediocentro suplente | No jugó | `0` | `0` | `0` | — |
| `18` | Aarón Cruz | POR | Portero suplente | No jugó | `0` | `0` | `0` | — |

### 2.2 Alineación completa de San Cristóbal y Nieves (DT: Francisco Molina) — 06/06/2024
Esquema inicial registrado: `5-4-1` (FIFA/FotMob/ESPN; Transfermarkt lo cataloga como `4-4-2 double 6`). DT confirmado: `Francisco Molina` (FotMob atribuye por error el puesto a Austin Huggins). Todos los datos de esta tabla tienen estado `confirmado`.

| Dorsal | Jugador | Posición | Rol táctico | Titular | Minutos | Goles | Asist. | Tarjetas |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `18` | Julani Archibald (C) | POR | Portero titular (Capitán) | Sí | `90` | `0` | `0` | — |
| `22` | Omari Sterling-James | DEF | Carrilero / lateral derecho | Sí (sale `85'`) | `85` | `0` | `0` | Amarilla `26'` |
| `4` | Andre Burley | DEF | Defensa central derecho | Sí | `90` | `0` | `0` | — |
| `6` | Lois Maynard | DEF | Defensa central (líbero) | Sí | `90` | `0` | `0` | Amarilla `63'` |
| `5` | Jameel Ible | DEF | Defensa central izquierdo | Sí | `90` | `0` | `0` | Amarilla `45'+4'` |
| `3` | Ethan Bristow | DEF | Carrilero / lateral izquierdo | Sí | `90` | `0` | `0` | — |
| `11` | Kimaree Rogers | DEL | Volante / extremo derecho | Sí (sale `53'`) | `53` | `0` | `0` | — |
| `15` | Mervin Lewis | MED | Mediocentro derecho | Sí | `90` | `0` | `0` | — |
| `14` | Tyquan Terrell | MED | Mediocentro izquierdo | Sí (sale `77'`) | `77` | `0` | `0` | — |
| `10` | Tyrese Shade | DEL | Volante / extremo izquierdo | Sí (sale `77'`) | `77` | `0` | `0` | — |
| `19` | Romaine Sawyers | MED | Delantero centro / enlace adelantado | Sí (sale `77'`) | `77` | `0` | `0` | — |
| `9` | Harrison Panayiotou | DEL | Extremo / delantero derecho | Suplente (entra `53'`) | `37` | `0` | `0` | — |
| `8` | Yohannes Mitchum | MED | Mediocentro | Suplente (entra `77'`) | `13` | `0` | `0` | — |
| `20` | Diego Edwards | DEL | Delantero centro | Suplente (entra `77'`) | `13` | `0` | `0` | — |
| `7` | G'Vaune Amory | MED | Volante ofensivo / extremo izquierdo | Suplente (entra `77'`) | `13` | `0` | `0` | — |
| `21` | Nequan Browne | MED | Carrilero / volante derecho | Suplente (entra `85'`) | `5` | `0` | `0` | — |
| `1` | Kai Trotman | POR | Portero suplente | No jugó | `0` | `0` | `0` | — |
| `2` | Malique Roberts | DEF | Defensa suplente | No jugó | `0` | `0` | `0` | — |
| `12` | Tyrique Davis | DEF | Defensa suplente | No jugó | `0` | `0` | `0` | — |
| `13` | Jal'Den Myers | DEF | Defensa suplente | No jugó | `0` | `0` | `0` | — |
| `16` | Yusuf Saunders | DEF | Defensa suplente | No jugó | `0` | `0` | `0` | — |
| `17` | Gabriel Vanterpool | DEL | Delantero suplente | No jugó | `0` | `0` | `0` | — |
| `23` | Vibert Stephen | POR | Portero suplente | No jugó | `0` | `0` | `0` | — |

### 2.3 Tarjetas y sustituciones cronológicas — Costa Rica vs. San Cristóbal y Nieves (06/06/2024)
- **Tarjetas rojas (`confirmado`):** `0` en todo el partido.
- **Penales (`confirmado`):** `0` cobrados en todo el partido.
- **Tarjetas amarillas (`4` en total, `confirmado`):**
  1. `26'` — **Omari Sterling-James** (`#22`, San Cristóbal y Nieves): falta sobre Álvaro Zamora en la banda izquierda de Costa Rica (FIFA Bookings registra `25'`).
  2. `45'+4'` — **Jameel Ible** (`#5`, San Cristóbal y Nieves): amonestado en reposición del primer tiempo por reclamo/protesta según Transfermarkt (FIFA Bookings registra `45'+3'`).
  3. `58'` — **Jefferson Brenes** (`#13`, Costa Rica): amonestado por reclamo/protesta según Transfermarkt.
  4. `63'` — **Lois Maynard** (`#6`, San Cristóbal y Nieves): falta sobre Warren Madrigal (FIFA Bookings registra `62'`).
- **Sustituciones (`10` en total, `5` por selección, `confirmado`):**
  1. `53'` (SKN): Entra `#9 Harrison Panayiotou` por `#11 Kimaree Rogers` (`52'` en arreglo resumen FIFA).
  2. `64'` (CRC): Entra `#10 Brandon Aguilera` por `#13 Jefferson Brenes` (`63'` en arreglo resumen FIFA).
  3. `65'` (CRC): Entra `#20 Josimar Alcócer` por `#17 Warren Madrigal` (`63'` en arreglo resumen FIFA).
  4. `77'` (SKN): Entra `#8 Yohannes Mitchum` por `#14 Tyquan Terrell` (`76'` en arreglo resumen FIFA).
  5. `77'` (SKN): Entra `#20 Diego Edwards` por `#19 Romaine Sawyers` (`75'` en arreglo resumen FIFA).
  6. `77'` (SKN): Entra `#7 G'Vaune Amory` por `#10 Tyrese Shade` (`75'` en arreglo resumen FIFA).
  7. `78'` (CRC): Entra `#2 Gerald Taylor` por `#22 Haxzel Quirós` (`76'` en arreglo resumen FIFA).
  8. `78'` (CRC): Entra `#19 Andy Rojas` por `#21 Álvaro Zamora` (`76'` en arreglo resumen FIFA).
  9. `81'` (CRC): Entra `#12 Joel Campbell` por `#9 Manfred Ugalde`.
  10. `85'` (SKN): Entra `#21 Nequan Browne` por `#22 Omari Sterling-James` (`84'` en arreglo resumen FIFA).

---

## 3. Cronología de los 4 Goles y Acciones Clave — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)

Convención oficial de coordenadas IFES/Opta (`confirmado`): `x_0_100` va de `0` (línea de gol propia) a `100` (línea de gol rival); `y_0_100` va de `0` (banda derecha) a `50` (centro) y `100` (banda izquierda), mirando hacia la portería rival.

### 3.0 Resumen de los 4 goles y asistencias — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)
1. **`40'` (`1–0`, `2344 s`):** **Orlando Galo** (`#14`, cabeza) con asistencia de **Jefferson Brenes** (`#13`) tras centro desde la derecha (`confirmado`).
2. **`49'` (`2–0`, `2926 s`):** **Orlando Galo** (`#14`, pie izquierdo) con asistencia de **Manfred Ugalde** (`#9`) tras pase atrasado al borde del área (`confirmado`).
3. **`82'` (`3–0`, `4904 s`):** **Josimar Alcócer** (`#20`, pie derecho) **sin asistencia**, tras presionar y bloquear el despeje de Julani Archibald (`confirmado`).
4. **`84'` (`4–0`, `5006 s`):** **Andy Rojas** (`#19`, pie derecho) con asistencia de **Joel Campbell** (`#12`) mediante pase filtrado en profundidad (`confirmado`).

### 3.1 Gol 1 (1–0) — Orlando Galo al minuto 40' (Costa Rica vs. San Cristóbal y Nieves, 06/06/2024)
- **Minuto oficial:** `40'` (reloj ESPN: `2344 s`; timestamp FIFA UTC: `2024-06-07T03:18:58.151Z`) (`confirmado`). *Variantes en prensa/resumen: `39'` en arreglo FIFA Goals, La Nación y Puro Periodismo; `38'` en La Teja.*
- **Autor:** `#14 Orlando Galo` (Costa Rica) (`confirmado`).
- **Asistencia:** `#13 Jefferson Brenes` (Costa Rica) (`confirmado`).
- **Parte del cuerpo:** Cabeza (`confirmado`).
- **Ubicación oficial (`confirmado`):** Cabezazo desde el sector izquierdo del área chica hacia la esquina inferior izquierda; coordenadas IFES/Opta `(x=95.1, y=56.3)`.
- **Zona aproximada (`estimacion_tactica`):** Área pequeña, sector centro-izquierdo (~5 m de la línea de gol).
- **Cómo nació la jugada (`confirmado`):** Luego de un saque de banda en campo visitante (reportado por SKNFA), Jefferson Brenes lanzó un centro largo desde la banda derecha; la salida del portero Julani Archibald quedó corta y Orlando Galo apareció desde segunda línea para conectar de cabeza al fondo.

### 3.2 Gol 2 (2–0) — Orlando Galo al minuto 49' (Costa Rica vs. San Cristóbal y Nieves, 06/06/2024)
- **Minuto oficial:** `49'` (reloj ESPN: `2926 s`; timestamp FIFA UTC: `2024-06-07T03:50:14.677Z`) (`confirmado`). *Variantes: `48'` en arreglo FIFA Goals, La Nación, La Teja y Puro Periodismo; `50'` en SKNFA, Everardo Herrera, EFE y Wikipedia.*
- **Autor:** `#14 Orlando Galo` (Costa Rica — doblete) (`confirmado`).
- **Asistencia:** `#9 Manfred Ugalde` (Costa Rica) (`confirmado`).
- **Parte del cuerpo:** Pie izquierdo (`confirmado`).
- **Ubicación oficial (`confirmado`):** Remate con pie izquierdo desde fuera del área hacia la esquina inferior izquierda; coordenadas IFES/Opta `(x=79.6, y=60.5)`.
- **Zona aproximada (`estimacion_tactica`):** Frontal / media luna del área, cargado ligeramente hacia el perfil centro-izquierdo.
- **Cómo nació la jugada (`confirmado`):** Ataque armado por el sector derecho; Manfred Ugalde recibió de espaldas/en apoyo y cedió un pase atrasado al borde del área para la llegada de frente de Orlando Galo, quien sacó un zurdazo raso junto al palo izquierdo.

### 3.3 Gol 3 (3–0) — Josimar Alcócer al minuto 82' (Costa Rica vs. San Cristóbal y Nieves, 06/06/2024)
- **Minuto oficial:** `82'` (reloj ESPN: `4904 s`; timestamp FIFA UTC: `2024-06-07T04:23:12.273Z`) (`confirmado`). *Variantes: `83'` en SKNFA/Wikipedia; `81'` en Puro Periodismo.*
- **Autor:** `#20 Josimar Alcócer` (Costa Rica — entró al `65'`) (`confirmado`).
- **Asistencia:** Ninguna (`sin asistencia`) (`confirmado`).
- **Parte del cuerpo:** Pie derecho (`confirmado`).
- **Ubicación oficial (`confirmado`):** Remate de pierna derecha desde el centro del área al centro de la portería; coordenadas IFES/Opta `(x=94.2, y=48.5)`.
- **Zona aproximada (`estimacion_tactica`):** Zona central del área pequeña frente al arco rival.
- **Cómo nació la jugada (`confirmado`):** Presión alta inmediata de Josimar Alcócer sobre Julani Archibald cuando el arquero visitante intentaba despejar; Archibald estrelló el balón en el cuerpo del extremo costarricense (jugada computada en Opta/FotMob como `error_derivado_en_gol: 1` para Archibald) y Alcócer empujó el balón al arco abierto. Fue el primer gol internacional de Alcócer con la selección mayor de Costa Rica.

### 3.4 Gol 4 (4–0) — Andy Rojas al minuto 84' (Costa Rica vs. San Cristóbal y Nieves, 06/06/2024)
- **Minuto oficial:** `84'` (reloj ESPN: `5006 s`; timestamp FIFA UTC: `2024-06-07T04:24:53.911Z`) (`confirmado`). *Variante: `83'` en arreglo resumen FIFA Goals.*
- **Autor:** `#19 Andy Rojas` (Costa Rica — entró al `78'`, debutante de 18 años) (`confirmado`).
- **Asistencia:** `#12 Joel Campbell` (Costa Rica — entró al `81'`) (`confirmado`).
- **Parte del cuerpo:** Pie derecho (`confirmado`).
- **Ubicación oficial (`confirmado`):** Remate de pierna derecha desde el centro del área hacia la esquina inferior derecha; coordenadas IFES/Opta `(x=86.5, y=41.5)`.
- **Zona aproximada (`estimacion_tactica`):** Interior centro-derecho del área grande.
- **Cómo nació la jugada (`confirmado`):** Pase filtrado en profundidad de Joel Campbell entre una defensa fatigada de San Cristóbal y Nieves; Andy Rojas atacó el espacio en velocidad y definió cruzado y raso de derecha.

### 3.5 Acciones clave sin gol — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)
- **`21'` (`confirmado`):** Primer remate de Costa Rica en todo el partido: disparo de `#17 Warren Madrigal` bloqueado desde fuera del área tras descarga de `#21 Álvaro Zamora`.
- **`24'` (`confirmado`):** Primer poste de Costa Rica: cabezazo de `#15 Francisco Calvo` al travesaño tras tiro de esquina y centro de `#11 Ariel Lassiter` (FIFA Timeline pos: `93.9, 45.0`).
- **`39'` (`confirmado`):** Remate lejano de derecha de `#9 Manfred Ugalde` atajado por `#18 Julani Archibald` abajo a la derecha.
- **`44'` (`confirmado`):** Pausa breve por atención médica al arquero visitante Julani Archibald.
- **`52'` (`confirmado`):** Cabezazo de `#14 Orlando Galo` en el centro del área tras pase de Ugalde, atajado por Archibald.
- **`71'` (`confirmado`):** Tiro lejano de `#21 Álvaro Zamora` al ángulo superior derecho desviado al córner por Archibald.
- **`73'` (`confirmado`):** Único remate a puerta de San Cristóbal y Nieves en todo el encuentro: disparo de `#19 Romaine Sawyers` desde fuera del área atajado abajo por `#23 Patrick Sequeira`.
- **`74'` (`confirmado`):** Segundo travesaño de Costa Rica: remate de derecha de `#9 Manfred Ugalde` desde el centro del área tras pase de `#22 Haxzel Quirós` (FIFA Timeline pos: `86.4, 42.5`).
- **`76'` (`confirmado`):** Ocasión clara fallada por `#21 Álvaro Zamora`: mano a mano desde el sector izquierdo del área que pasa desviado al segundo palo tras pase filtrado de `#10 Brandon Aguilera`.

---

## 4. Estadísticas Verificadas (1T, 2T, Total e Individuales) — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)

### 4.1 Estadísticas colectivas comparadas por mitad y total (`confirmado`)
Fuente principal: FotMob / Opta (`match 4416441`), complementada con la posesión oficial de FIFA Live API v3 (`65.3%` vs `34.7%`). Toda fila de esta tabla tiene estado `confirmado` y cumple `1T + 2T == Total` en los conteos absolutos.

| Métrica | CRC Total | SKN Total | CRC 1T | SKN 1T | CRC 2T | SKN 2T |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Posesión oficial FIFA (%) | `65.3%` | `34.7%` | `no_disponible` | `no_disponible` | `no_disponible` | `no_disponible` |
| Posesión FotMob (%) | `65%` | `35%` | `68%` | `32%` | `63%` | `37%` |
| Tiros totales | `23` | `5` | `10` | `3` | `13` | `2` |
| Tiros a puerta | `7` | `1` | `2` | `0` | `5` | `1` |
| Tiros fuera | `8` | `3` | `4` | `2` | `4` | `1` |
| Tiros bloqueados | `8` | `1` | `4` | `1` | `4` | `0` |
| Tiros al poste | `2` | `0` | `1` | `0` | `1` | `0` |
| Tiros dentro del área | `10` | `1` | `3` | `1` | `7` | `0` |
| Tiros fuera del área | `13` | `4` | `7` | `2` | `6` | `2` |
| Grandes ocasiones | `5` | `0` | `1` | `0` | `4` | `0` |
| Grandes ocasiones falladas | `2` | `0` | `0` | `0` | `2` | `0` |
| Toques en área rival | `29` | `7` | `11` | `4` | `18` | `3` |
| Pases intentados | `571` | `300` | `282` | `134` | `289` | `166` |
| Pases precisos | `483` | `221` | `229` | `87` | `254` | `134` |
| Precisión de pases (FotMob) | `85%` | `74%` | `81%` | `65%` | `88%` | `81%` |
| Pases precisos campo propio | `244` | `116` | `129` | `56` | `115` | `60` |
| Pases precisos campo rival | `239` | `105` | `100` | `31` | `139` | `74` |
| Balones largos precisos (%) | `14 (33%)` | `24 (39%)` | `7 (26%)` | `9 (25%)` | `7 (47%)` | `15 (58%)` |
| Centros precisos (%) | `6 (32%)` | `2 (17%)` | `4 (29%)` | `1 (20%)` | `2 (40%)` | `1 (14%)` |
| Saques de banda | `19` | `15` | `11` | `8` | `8` | `7` |
| Tiros de esquina | `5` | `3` | `3` | `2` | `2` | `1` |
| Fueras de juego | `2` | `3` | `0` | `2` | `2` | `1` |
| Atajadas | `1` | `3` | `0` | `1` | `1` | `2` |
| Entradas (tackles) | `20` | `10` | `5` | `3` | `15` | `7` |
| Intercepciones | `7` | `14` | `2` | `6` | `5` | `8` |
| Bloqueos defensivos | `1` | `6` | `1` | `3` | `0` | `3` |
| Despejes | `9` | `19` | `5` | `12` | `4` | `7` |
| Duelos ganados | `57` | `38` | `30` | `18` | `27` | `20` |
| Duelos en el suelo ganados (%) | `37 (57%)` | `28 (43%)` | `16 (62%)` | `10 (38%)` | `21 (54%)` | `18 (46%)` |
| Duelos aéreos ganados (%) | `20 (67%)` | `10 (33%)` | `14 (64%)` | `8 (36%)` | `6 (75%)` | `2 (25%)` |
| Regates exitosos (%) | `4 (44%)` | `9 (41%)` | `4 (80%)` | `4 (50%)` | `0 (0%)` | `5 (36%)` |
| Faltas cometidas | `11` | `13` | `4` | `7` | `7` | `6` |
| Tarjetas amarillas | `1` | `3` | `0` | `2` | `1` | `1` |
| Tarjetas rojas | `0` | `0` | `0` | `0` | `0` | `0` |

- **Recuperaciones totales (`confirmado`) y corte `1T`/`2T` (`no_disponible`):** La suma de recuperaciones individuales (`Recoveries` en FotMob) arroja **`62`** para Costa Rica (`57` jugadores de campo + `5` Patrick Sequeira) y **`59`** para San Cristóbal y Nieves (`52` jugadores de campo + `7` Julani Archibald). No existe corte publicado separado por primer tiempo (`1T`) y segundo tiempo (`2T`) para recuperaciones (`no_disponible`).

### 4.2 Líderes y registros individuales destacados (FotMob / Opta, `confirmado`) — CRC 4–0 SKN (06/06/2024)
- **Mejor calificación FotMob:** `#14 Orlando Galo` (`9.17`), seguido por `#9 Manfred Ugalde` (`8.24`), `#21 Álvaro Zamora` (`8.12`), `#15 Francisco Calvo` (`8.04`), `#13 Jefferson Brenes` (`7.77`) y `#20 Josimar Alcócer` (`7.6`). En San Cristóbal y Nieves el rating más alto fue `#15 Mervin Lewis` (`6.65`), seguido de `#14 Tyquan Terrell` (`6.48`) y `#8 Yohannes Mitchum` (`6.29`); el más bajo fue `#18 Julani Archibald` (`4.25`).
- **Volumen de pases y control:** `#15 Francisco Calvo` lideró toques (`101`) y pases precisos (`74/87`, `11` en último tercio), seguido de `#6 Julio Cascante` (`63/68` pases, `77` toques) y `#14 Orlando Galo` (`51/60`, `78` toques). `#9 Manfred Ugalde` completó `35/39` (`89.7%`) pese a jugar como referencia ofensiva.
- **Creación de juego:** `#21 Álvaro Zamora` lideró ocasiones creadas (`4`, más `11` pases al último tercio y `4` tiros), `#9 Manfred Ugalde` sumó `3` ocasiones creadas (`1` gran ocasión, `1` asistencia) y `#13 Jefferson Brenes` dio `14` pases en el último tercio en apenas `64` minutos (`1` gran ocasión creada, `1` asistencia). Desde el banco, `#10 Brandon Aguilera` (`2` ocasiones creadas en `26'`) y `#12 Joel Campbell` (`2` ocasiones creadas, `8` pases al último tercio y `1` asistencia en `9'`) tuvieron incidencia inmediata.
- **Acciones defensivas y duelos:** En Costa Rica, `#3 Jeyland Mitchell` lideró tackles (`5/5` acciones defensivas `6`, `7/10` duelos) y `#6 Julio Cascante` ganó `9/11` duelos aéreos (`9/14` duelos totales, `4` despejes). `#15 Francisco Calvo` sumó `9` recuperaciones y `9` duelos ganados (`5/7` aéreos), y `#14 Orlando Galo` registró `8` recuperaciones y `8` duelos ganados. En San Cristóbal y Nieves, `#6 Lois Maynard` lideró acciones defensivas (`10`: `5` intercepciones, `2` bloqueos, `3` despejes) y recuperaciones (`10`); `#3 Ethan Bristow` registró `9` acciones defensivas y `#4 Andre Burley` `8` (`5` despejes, `2` bloqueos). `#19 Romaine Sawyers` peleó `17` duelos (`7` ganados, `5/12` aéreos).
- **Porteros:** `#23 Patrick Sequeira` (CRC) registró `1` atajada en estirada, `5` recuperaciones, `15/17` pases y portería en cero (`rating 7.03`). `#18 Julani Archibald` (SKN) sumó `3` atajadas (`2` en estirada, `1` dentro del área), `2` despejes de puños, `6/25` balones largos, `4` goles concedidos y `1` error directo derivado en gol (`rating 4.25`).

---

## 5. Datos NO Disponibles Públicamente (`no_disponible`) — Guía Anti-Alucinación para el Chatbot (Costa Rica 4–0 San Cristóbal y Nieves, 06/06/2024)

Cuando un usuario pregunte por cualquiera de las siguientes métricas sobre el partido **Costa Rica 4–0 San Cristóbal y Nieves (6 de junio de 2024)**, el chatbot debe responder explícitamente que la métrica figura como `no_disponible` en el paquete y que **no existe registro público verificado** en FIFA, Concacaf, Opta/FotMob ni ESPN:

- **Distancia recorrida (kilómetros recorridos o km por jugador / por equipo):** `no_disponible` (sin datos EPTS / tracking GPS públicos para ningún futbolista ni equipo).
- **Velocidad máxima (km/h) y cantidad de sprints:** `no_disponible` (sin datos de tracking físico públicos).
- **Mapas de calor continuos y tracking posicional a 25 fps:** `no_disponible` (ni FIFA ni FotMob publican tracking EPTS o heatmaps para este encuentro).
- **Goles esperados (`xG`) y asistencias esperadas (`xA`):** `no_disponible` (sin módulo `xG/xA` publicado en FotMob, ESPN ni FIFA API para este partido).
- **Shotmap completo de los `28` remates (`23` CRC + `5` SKN):** `no_disponible` (el campo `content.shotmap` de FotMob está vacío; únicamente existen coordenadas IFES/Opta confirmadas para los `4` goles y las acciones clave registradas en FIFA Timeline/ESPN).
- **Redes de pases (matriz jugador a jugador) y `PPDA` (intensidad de presión):** `no_disponible` (sin archivo de eventos posicionales completo pase a pase).
- **Corte separado `1T` y `2T` de recuperaciones por equipo:** `no_disponible` (FotMob solo publica recuperaciones por jugador para el total del partido: `62` CRC vs `59` SKN).
- **Temperatura exacta en °C, humedad (%) y velocidad del viento en km/h:** `no_disponible` (el campo `Weather` de FIFA llega nulo; solo está confirmada cualitativamente la lluvia intensa y la cancha rápida).
- **Color exacto del uniforme de portero de Patrick Sequeira (`#23` Costa Rica):** `no_disponible` (sin fotografía verificada de ese partido específico).

---

## 6. Análisis Táctico Completo — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)

Nota metodológica: los datos numéricos citados dentro de este análisis son `confirmado`, mientras que la interpretación de comportamientos colectivos, intenciones y ajustes tiene estado `estimacion_tactica`.

### 6.1 Esquema inicial y evolución táctica por fases (`estimacion_tactica` apoyada en datos `confirmado`)
- **Parado inicial de Costa Rica (`3-4-3` / `3-4-2-1` en ataque, `5-2-3` / `5-4-1` sin balón):** Gustavo Alfaro salió con tres centrales (`Jeyland Mitchell`, `Julio Cascante`, `Francisco Calvo`), dos carrileros encargados de dar amplitud (`Haxzel Quirós` por derecha y `Ariel Lassiter` por izquierda), doble pivote (`Jefferson Brenes` y `Orlando Galo`), dos mediapuntas por carriles interiores (`Warren Madrigal` y `Álvaro Zamora`) y `Manfred Ugalde` como nueve móvil.
- **Parado inicial de San Cristóbal y Nieves (`5-4-1` en bloque bajo):** Francisco Molina protegió la frontal con tres centrales (`Andre Burley`, `Lois Maynard`, `Jameel Ible`), carrileros muy hundidos (`Omari Sterling-James` y `Ethan Bristow`), una segunda línea de cuatro (`Kimaree Rogers`, `Mervin Lewis`, `Tyquan Terrell`, `Tyrese Shade`) y `Romaine Sawyers` descolgado para recibir largo.
- **Tramo `0'–23'` (posesión estéril bajo lluvia):** Bajo un aguacero constante que volvió rápida y resbaladiza la gramilla, Costa Rica alcanzó el `79%` de posesión en los primeros `20` minutos (según La Nación), pero se precipitó buscando envíos largos y centros forzados. La selección nacional pasó `20` minutos sin rematar hasta el disparo bloqueado de Madrigal (`21'`) y el cabezazo al travesaño de Calvo en córner (`24'`).
- **Tramo `24'–63'` (paciencia rasante y ventaja `2–0`):** Alfaro pidió desde la banda bajar el ritmo de pases largos, circular a ras de césped y atacar los intervalos con llegadores de segunda línea. Ese ajuste abrió el cerrojo: primero con el cabezazo de Orlando Galo al `40'` y luego, nada más volver del descanso, con el zurdazo del propio Galo al `49'`.
- **Tramo `64'–90'+5'` (relevos, desgaste físico visitante y cierre `4–0`):** Con el `2–0`, el ingreso de `Brandon Aguilera` (`64'`) y `Josimar Alcócer` (`65'`) aceleró la circulación y la presión tras pérdida. Aunque San Cristóbal y Nieves encontró su único tiro a puerta al `73'` (Sawyers), Costa Rica estrelló otro balón en el poste (`74'`, Ugalde), falló un mano a mano (`76'`, Zamora) y aprovechó el quiebre físico visitante tras el triple cambio de Molina al `77'` para liquidar con los ingresos de `Gerald Taylor` (`78'`), `Andy Rojas` (`78'`) y `Joel Campbell` (`81'`): goles de Alcócer (`82'`) y Rojas (`84'`).

### 6.2 Presión y recuperación tras pérdida — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024, `estimacion_tactica`)
- **Presión de Costa Rica:** Tras cada pérdida en campo contrario, Costa Rica activó un acoso inmediato con Ugalde, Zamora, Madrigal y los interiores para cortar la transición hacia Sawyers. En el segundo tiempo esa presión se intensificó: Costa Rica triplicó su número de entradas (`15` tackles en `2T` frente a `5` en `1T`, para `20` totales). La máxima expresión llegó al `82'`, cuando Josimar Alcócer apretó la salida con los pies de Julani Archibald y bloqueó su despeje para el `3–0`.
- **Postura sin balón de San Cristóbal y Nieves:** Renunció a la presión alta para no abrir espacios a la espalda de sus centrales. Mantuvo líneas juntas en propio campo, priorizando la intercepción (`14` totales vs `7` de Costa Rica) y el despeje (`19` vs `9`) por encima del robo agresivo arriba (`10` entradas en `90` minutos).

### 6.3 Salida de balón — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024, `estimacion_tactica`)
- **Construcción de Costa Rica desde atrás:** Con el `3+2` inicial (tres centrales + Brenes/Galo), Costa Rica dispuso de superioridad numérica limpia frente al único punta visitante (`Sawyers`). `Francisco Calvo` (`74/87` pases, `11` al último tercio) y `Julio Cascante` (`63/68`) llevaron el peso de la salida por izquierda y centro, apoyados por `Jeyland Mitchell` (`38/43`) por derecha. Cuando la lluvia frenó el juego en los primeros `20` minutos (`81%` de precisión en `1T`), Costa Rica mejoró en la segunda mitad hasta el `88%` (`254/289`) y elevó sus pases precisos en campo rival de `100` (`1T`) a `139` (`2T`).
- **Salida directa de San Cristóbal y Nieves:** Ante la presión posicional costarricense, la visita recurrió sistemáticamente al envío largo desde su portero y centrales: completó `24` balones largos (`39%`, frente a `14` de Costa Rica) y `Julani Archibald` intentó `25` lanzamientos largos (acertando solo `6`). El destino principal fue el juego aéreo de `Romaine Sawyers` (`12` duelos aéreos disputados, `5` ganados).

### 6.4 Bloque defensivo y control territorial — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024, `estimacion_tactica`)
- **Compactación visitante y erosión física:** El `5-4-1` de San Cristóbal y Nieves resistió casi `40` minutos sin conceder un gol gracias al trabajo de `Lois Maynard` (`10` acciones defensivas, `10` recuperaciones), `Ethan Bristow` (`9` acciones defensivas) y `Andre Burley` (`8` acciones defensivas, `5` despejes). Sin embargo, defender tan cerca de su propio arco (`29` toques de Costa Rica dentro del área visitante frente a `7` en el área tica) obligó a un desgaste continuo que terminó por romper las distancias entre líneas en los últimos `15` minutos.
- **Vigilancias de Costa Rica:** Con los carrileros altos en fase ofensiva, la línea de tres (`Mitchell`–`Cascante`–`Calvo`) ganó la mayoría de los duelos directos, especialmente por alto (`20` duelos aéreos ganados contra `10` de SKN, un `67%` de efectividad; Cascante `9/11` y Calvo `5/7`). Eso dejó a San Cristóbal y Nieves en `0` tiros a puerta en `1T` y solo `1` en todo el encuentro.

### 6.5 Transiciones defensa–ataque y ataque–defensa — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024, `estimacion_tactica`)
- **Transiciones de Costa Rica:** Cuando San Cristóbal y Nieves adelantó metros en la segunda parte para buscar descuento (`37%` de posesión y `166` pases en `2T`), dejó espacio a la espalda de sus carrileros. Ahí brillaron los ingresos frescos: `Joel Campbell` filtró entre líneas apenas tres minutos después de entrar para la diagonal en velocidad de `Andy Rojas` (`4–0`, `84'`). Además, el descenso constante de `Manfred Ugalde` arrastró a Maynard/Burley fuera de zona para abrir pasillos a Zamora y Galo.
- **Transiciones de San Cristóbal y Nieves:** Carecieron de continuidad por falta de apoyos cercanos a Sawyers tras recuperación. Sus intentos de ruptura llegaron más por regates individuales (`9` regates exitosos, `5` en `2T` incluyendo `2` de `G'Vaune Amory` tras su ingreso) que por combinaciones sostenidas (`1` solo remate dentro del área en `90` minutos).

### 6.6 Impacto táctico de los goles y los cambios — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024, `estimacion_tactica`)
- **Efecto del `1–0` (`40'`) y el `2–0` (`49'`):** El cabezazo de Galo antes del descanso evitó que San Cristóbal y Nieves cerrara el `1T` con el empate intacto y obligó a Molina a ajustar en el complemento (`53'`, `Panayiotou` por `Rogers`). El `2–0` apenas cuatro minutos después de reanudarse el juego desactivó cualquier intento de repliegue conservador visitante y dio control total a Costa Rica.
- **Impacto de las ventanas de cambio:**
  - `64'–65'` (CRC: `Aguilera` por `Brenes` [amonestado] y `Alcócer` por `Madrigal`): protegió a Brenes de una segunda amarilla, sumó último pase en la base (Aguilera dejó solo a Zamora al `76'` y puso `2` centros precisos) y agregó intensidad de presión en banda derecha con Alcócer (`3–0` al `82'`).
  - `77'` (SKN: triple cambio `Mitchum`, `Edwards`, `Amory` por `Terrell`, `Sawyers`, `Shade`): respondió al agotamiento del bloque visitante, pero desajustó temporalmente la coordinación defensiva justo cuando Costa Rica metía piernas frescas (`78'` `Taylor`/`Rojas`, `81'` `Campbell`). Entre el `82'` y el `84'` cayeron dos goles en `102` segundos de diferencia (`4904 s` a `5006 s`).

### 6.7 Jugadores destacados y motivo respaldado en métricas — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)
1. **Orlando Galo (`#14`, Costa Rica — Rating `9.17`):** Figura del partido siguiendo la indicación de Alfaro de pisar el área desde segunda línea. Anotó los dos goles que abrieron el cerrojo (`40'` de cabeza, `49'` de zurda), remató `5` veces (`3` a puerta), completó `51/60` pases, sumó `8` recuperaciones y ganó `8/11` duelos.
2. **Manfred Ugalde (`#9`, Costa Rica — Rating `8.24`):** Aunque no marcó y estrelló un remate en el travesaño (`74'`), fue el eje asociativo en tres cuartos: `35/39` pases (`89.7%`), `3` ocasiones creadas, `1` asistencia en el `2–0`, `4` toques en el área rival y `6` recuperaciones en `81` minutos.
3. **Álvaro Zamora (`#21`, Costa Rica — Rating `8.12`):** Principal motor ofensivo en los últimos metros con `4` ocasiones creadas, `4` remates, `11` pases al último tercio, `7` recuperaciones y `5/6` duelos ganados, aunque falló un mano a mano al `76'`.
4. **Francisco Calvo (`#15`, Costa Rica — Rating `8.04`):** Líder de salida y juego aéreo desde la izquierda: `101` toques, `74/87` pases (`11` al último tercio), `9` recuperaciones, `9` duelos ganados y un cabezazo al travesaño (`24'`).
5. **Jefferson Brenes (`#13`, Costa Rica — Rating `7.77`):** Clave en `64` minutos antes de salir amonestado: `14` pases al último tercio, `1` gran ocasión creada y la asistencia del `1–0` con centro desde la derecha.
6. **Josimar Alcócer (`#20`, `7.6`) y Andy Rojas (`#19`, `7.28`), con pase de Joel Campbell (`#12`):** Los tres suplentes ofensivos sentenciaron en `2` minutos (`82'` y `84'`). Alcócer firmó su primer gol en selección mayor por pura intensidad en la presión; Rojas debutó como goleador en eliminatoria con `18` años tras un pase filtrado de Campbell (`2` ocasiones creadas en `9` minutos).
7. **Referencia en San Cristóbal y Nieves:** `Mervin Lewis` (`#15`, `rating 6.65`, `6` acciones defensivas y `19/21` pases) y `Lois Maynard` (`#6`, `10` acciones defensivas y `10` recuperaciones) sostuvieron al equipo mientras resistió el físico. `Julani Archibald` (`#18`, `4.25`) combinó `3` atajadas de mérito (`39'`, `52'`, `71'`) con dudas en el centro del `1–0` y el error del `3–0`.

### 6.8 Conclusión del partido Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)
Costa Rica resolvió con autoridad un debut incómodo por la lluvia y el bloque `5-4-1` ultracerrado de San Cristóbal y Nieves. Superado el atasco de los primeros `20` minutos mediante circulación paciente por abajo, la llegada de segunda línea de Orlando Galo rompió el partido entre el `40'` y el `49'`. A partir de ahí, el dominio territorial (`65.3%` de posesión FIFA, `23–5` en tiros, `29–7` en toques en el área rival) y la profundidad de la banca costarricense convirtieron un `2–0` trabajado en un `4–0` contundente que dejó a Costa Rica en la cima del Grupo B desde la primera jornada.

---

## 7. Nota de Discrepancias entre Fuentes — Costa Rica 4–0 San Cristóbal y Nieves (06/06/2024)

Para evitar confusiones cuando el chatbot o el equipo contrasten bases externas sobre **Costa Rica 4–0 San Cristóbal y Nieves (6 de junio de 2024)**, las diferencias documentadas en [FUENTES.md](FUENTES.md) se resuelven así:
1. **Asistencia (`15,700` vs `5,150`):** Se adopta `15,700` (FIFA, FotMob, ESPN, Wikipedia). Transfermarkt muestra `5,150` por importar un literal anómalo cargado en `Stadium.CityName` dentro de FIFA API.
2. **DT de San Cristóbal y Nieves (`Francisco Molina` vs `Austin Huggins`):** Se adopta `Francisco Molina` (FIFA `IdCoach: 483207`, Transfermarkt, EFE, Everardo Herrera y declaraciones en Radio Columbia). FotMob atribuye el cargo erróneamente a Austin Huggins.
3. **Fecha (`06/06/2024` vs `07/06/2024`):** En San José (`CST, UTC-6`) inició el 6 de junio de 2024 a las `20:39`; en horario `UTC` (`02:39Z`) corresponde al 7 de junio.
4. **Esquema SKN (`5-4-1` vs `4-4-2 double 6`):** FIFA, FotMob y ESPN confirman línea de cinco (`5-4-1`); solo Transfermarkt lo lista como `4-4-2 double 6`.
5. **Porcentaje de pases (`85% / 74%` vs `84% / 73%`):** Sobre idénticos totales (`483/571 = 84.59%` y `221/300 = 73.67%`), FotMob redondea y algunos resúmenes web de ESPN truncan.
6. **Minutos de goles y cambios (`±1–2` min):** Este paquete adopta los minutos en curso de FIFA Timeline, ESPN (con reloj en segundos), FotMob y Transfermarkt (`40'`, `49'`, `82'`, `84'`). El arreglo resumen `Goals/Substitutions` de FIFA trunca al entero inferior (`39'`, `48'`, `82'`, `83'`), origen de variaciones en prensa.
