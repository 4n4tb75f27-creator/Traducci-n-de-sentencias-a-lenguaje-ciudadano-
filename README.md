# ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial
**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**

**Estudiante:** Gregorio Puyo Gómez | **Nombre del proyecto:** LawTranslate | **Fecha de inicio:** 2026-08-03

---

## 📋 Parte 1 — Descripción del proyecto

### 1.1 El problema jurídico
En Colombia, las sentencias y providencias judiciales están redactadas en un lenguaje técnico, barroco y denso, saturado de latinismos y fórmulas procesales decimonónicas que resultan prácticamente incomprensibles para el ciudadano de a pie. Esto genera una barrera crítica de acceso a la administración de justicia (Art. 229 C.P.): cuando una persona recibe la notificación de un fallo judicial, con frecuencia no logra determinar si ganó o perdió el caso, qué resolvió el juez, qué derechos le fueron amparados o cuáles son los plazos perentorios y efectos prácticos que debe cumplir. 

Actualmente, las personas que no cuentan con recursos para pagar una consulta jurídica particular recurren a interpretaciones empíricas de terceros, familiares o búsquedas desorganizadas en internet, donde la información puede ser imprecisa o alarmista. **LawTranslate** busca democratizar la comprensión de las decisiones judiciales mediante una herramienta pedagógica que traduce extractos de fallos a una estructura clara de cuatro dimensiones (el caso, la decisión, los motivos y los efectos/plazos) acompañada de un glosario ciudadano de términos clave, sustentada en los principios de debido proceso y las directrices de lenguaje claro de la Rama Judicial.

### 1.2 Usuarios
El usuario principal es cualquier ciudadano colombiano que se encuentre vinculado a un proceso judicial o haya interpuesto una acción constitucional (tutela, derecho de petición, proceso de arrendamiento o sanción disciplinaria) y reciba una providencia que no comprende. La herramienta está dirigida principalmente a personas sin formación jurídica, aunque también puede ser empleada por estudiantes de derecho, consultorios jurídicos, líderes comunitarios y defensores de derechos humanos para explicar fallos judiciales a sus representados. 

El usuario ideal es: *“un ciudadano colombiano que recibió la notificación de un fallo judicial o resolución y necesita saber con certeza si ganó o perdió, por qué se tomó esa decisión y qué debe hacer o exigir a continuación, sin rodeos ni tecnicismos confusos”*.

### 1.3 Qué hace y qué NO hace
| ✅ Sí hace | ❌ No hace |
| :--- | :--- |
| Analiza fragmentos, resolutivos y fallos de sentencias judiciales colombianas. | No constituye asesoría jurídica profesional ni reemplaza a un abogado. |
| Traduce la decisión judicial a lenguaje ciudadano estructurado en 4 dimensiones claras (conflicto, decisión, motivos y efectos/plazos). | No redacta demandas, tutelas, recursos de apelación ni memoriales procesales. |
| Explica latinismos y tecnicismos jurídicos mediante un glosario ciudadano contextualizado. | No representa a los usuarios ante juzgados, tribunales ni autoridades administrativas. |
| Identifica el sentido del fallo (si el ciudadano ganó o perdió) y los plazos de cumplimiento obligatorio. | No garantiza el resultado de controversias judiciales ni altera decisiones de los jueces. |
| Funciona tanto con modelos de lenguaje avanzados (LLaMA 3.3 vía OpenRouter) como de forma autónoma con un motor analítico local. | No almacena ni recopila datos personales reales de los usuarios (Ley 1581 de 2012). |
| Reconoce las limitaciones de su corpus y advierte sobre el carácter pedagógico del ejercicio. | No litiga ni asume la responsabilidad profesional de un apoderado judicial. |

### 1.4 Marco jurídico y fuentes
El corpus y sustento normativo de LawTranslate se fundamenta en disposiciones públicas y vinculantes del ordenamiento jurídico colombiano:
* **Constitución Política de Colombia de 1991:**
  * **Artículo 29:** Derecho Fundamental al Debido Proceso y publicidad de los actos judiciales.
  * **Artículo 229:** Derecho Fundamental de Acceso a la Administración de Justicia.
  * **Artículo 86:** Acción de Tutela para la protección inmediata de derechos fundamentales.
  * **Artículo 23:** Derecho Fundamental de Petición.
* **Decreto 2591 de 1991:** Reglamentación de la Acción de Tutela (trámite, órdenes de inmediato cumplimiento y régimen de desacato de conformidad con el Art. 52).
* **Código General del Proceso (Ley 1564 de 2012):** Estructura de las providencias judiciales, terminación de contratos, costas y ejecutoria de fallos.
* **Protocolo de Lenguaje Claro de la Rama Judicial y lineamientos del Departamento Nacional de Planeación (DNP):** Criterios pedagógicos y de simplificación del lenguaje para garantizar la comprensión efectiva de las decisiones por parte de la ciudadanía.
* **Jurisprudencia Hito de la Corte Constitucional:** Sentencia T-760 de 2008 (derecho fundamental autónomo a la salud y prohibición de barreras burocráticas) y T-240 de 2018 (debido proceso en sanciones educativas).

### 1.5 Nombre y lema
**LawTranslate**  
*“El derecho, en palabras de todos.”*

El nombre combina el rigor del derecho (*Law*) con la misión transformadora de traducir lo farragoso a lo accesible (*Translate*). El lema sintetiza la vocación democrática del proyecto: devolverle al ciudadano el entendimiento de las leyes y sentencias que rigen su destino.

---

## 🗺️ Parte 2 — Plan de desarrollo
El proyecto se desarrolló progresivamente durante cinco semanas siguiendo los hitos metodológicos establecidos para el curso. Cada etapa permitió delimitar el problema, formular y calibrar instrucciones, probar casos emblemáticos y desplegar la herramienta en una interfaz web pública.

### Hitos del proyecto
* [x] **M0 — Descripción y plan:** Se delimitó el problema jurídico del lenguaje judicial inaccesible, se definieron los usuarios, el alcance (qué hace y qué no hace) y las fuentes constitucionales.
* [x] **M1 — Asistente con instrucciones v1:** Se diseñó el prompt de sistema del asistente pedagógico, obligándolo a estructurar la respuesta en formato JSON de 4 dimensiones y glosario, prohibiendo alucinaciones y obligando a incluir la advertencia legal.
* [x] **M2 — Casos de prueba documentados:** Se formularon y validaron 5 casos de prueba emblemáticos (tutela salud, debido proceso disciplinario, derecho de petición, restitución de inmueble y caso libre) documentados en `docs/casos-de-prueba.md`.
* [x] **M3 — Corpus conectado (RAG):** Se integró el corpus normativo y jurisprudencial de sentencias de referencia (`corpus/sentencias_referencia.md`) y un diccionario analítico estructurado para contrastar los textos sin inventar normas.
* [x] **M4 — Interfaz web desplegada:** Se construyó una interfaz web moderna, responsiva y accesible con HTML5, CSS3 institucional y Vanilla JavaScript, desplegada públicamente mediante GitHub Pages.
* [x] **M5 — Análisis crítico y demo:** Se realizaron las evaluaciones críticas sobre los límites del sistema, la prueba con un usuario externo y la preparación de la sustentación final.

### Bitácora de avance semanal
| Semana | Qué hice | Enlace/captura | Dudas para la clase |
| :---: | :--- | :---: | :--- |
| **1** | Delimitación del problema jurídico del lenguaje farragoso en fallos judiciales; definición del alcance, usuarios y fuentes normativas de LawTranslate. | [README — Parte 1](#-parte-1--descripción-del-proyecto) | ¿Cómo delimitar la traducción sin dar la apariencia de una asesoría legal vinculante? |
| **2** | Diseño del prompt del sistema v1 con reglas estrictas anti-alucinación y estructura de 4 bloques. Redacción de los primeros casos de prueba. | [prompts/prompt_sistema_v1.md](prompts/prompt_sistema_v1.md) | ¿Qué estructura de salida es más intuitiva para personas sin formación jurídica? |
| **3** | Consolidación del corpus de sentencias de tutela y guía de lenguaje claro. Integración del diccionario normativo para detección de tecnicismos. | [corpus/sentencias_referencia.md](corpus/sentencias_referencia.md) | ¿Cómo manejar sentencias muy extensas frente al límite de tokens del modelo? |
| **4** | Desarrollo del frontend interactivo, botones de prueba interactivos, conexión opcional con OpenRouter y despliegue público en GitHub Pages. | [URL pública](https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/) | ¿Cómo garantizar compatibilidad total en dispositivos móviles para el usuario final? |
| **5** | Validación con usuario real externo, pruebas críticas de casos complejos, redacción del análisis crítico ético y preparación de la demo. | [docs/evidencia-usuario.md](docs/evidencia-usuario.md) | ¿Cómo sustentar de forma contundente por qué la IA no sustituye el criterio del abogado? |

---

## 🛠️ Parte 3 — Stack técnico
La herramienta fue desarrollada utilizando tecnologías accesibles, gratuitas y de ejecución directa en el navegador, sin necesidad de instalaciones complejas.

| Pieza | Herramienta | Función |
| :--- | :--- | :--- |
| **Interfaz web** | HTML5 + CSS3 (Diseño institucional Javeriana) | Permite al usuario ingresar o pegar el texto judicial y visualizar las 4 tarjetas de traducción. |
| **Lógica y Orquestación** | JavaScript Vanilla | Organiza el procesamiento del texto, gestiona los casos de prueba y conecta con el motor de IA. |
| **Modelo LLM** | OpenRouter (Meta LLaMA 3.3 70B Instruct / Gemini) | Proporciona el modelo de lenguaje en la nube cuando el usuario ingresa su API Key. |
| **Motor Analítico Local** | Reglas semánticas + Diccionario Jurídico | Permite que la herramienta funcione de forma inmediata, gratuita y sin requerir claves de API. |
| **Corpus Jurídico** | Archivos públicos en `/corpus` y `/docs` | Contiene las sentencias de referencia, lineamientos del DNP y principios procesales colombianos. |
| **Control de versiones** | GitHub | Permite almacenar el código y registrar el historial de desarrollo del proyecto. |
| **Despliegue** | GitHub Pages | Permite acceder públicamente a la aplicación desde cualquier navegador web o celular. |

### Arquitectura del sistema
```
                    ┌─────────────────────────┐
                    │     CIUDADANO / USUARIO │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │    INTERFAZ WEB         │
                    │   (GitHub Pages / HTML) │
                    └────────────┬────────────┘
                                 │
                     ┌───────────┴───────────┐
                     ▼                       ▼
            [¿Tiene API Key?]       [Sin API Key (Gratis)]
                     │                       │
                     ▼                       ▼
         ┌───────────────────────┐ ┌───────────────────────────┐
         │      OPENROUTER       │ │   MOTOR ANALÍTICO LOCAL   │
         │  (LLaMA 3.3 / Gemini) │ │   (Detección semántica    │
         │   Prompt Estructurado │ │    y diccionario procesal)│
         └───────────┬───────────┘ └─────────────┬─────────────┘
                     │                           │
                     └─────────────┬─────────────┘
                                   │
                                   ▼
                    ┌─────────────────────────┐
                    │ TRADUCCIÓN CIUDADANA    │
                    │ 1. ¿De qué se trata?    │
                    │ 2. ¿Qué decidió el juez?│
                    │ 3. Motivos principales  │
                    │ 4. Plazos y efectos     │
                    │ 5. Glosario pedagógico  │
                    └─────────────────────────┘
```

**Seguridad y Privacidad:** Las claves de API opcionales se manejan localmente en la memoria del navegador y no se almacenan ni se publican en el repositorio público.

---

## 🚀 Parte 4 — Despliegue
El objetivo del proyecto fue desarrollar una herramienta que pudiera ser utilizada directamente desde un navegador web sin necesidad de instalar programas adicionales.

La aplicación fue desplegada mediante GitHub Pages conectada al repositorio principal. De esta manera, cualquier actualización en el código se refleja de forma automática en la versión pública.

### URL pública
🔗 **[https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/](https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/)**

### Checklist de despliegue
- [x] La aplicación cuenta con una interfaz web totalmente funcional.
- [x] La aplicación puede ser abierta desde cualquier navegador web moderno (Safari, Chrome, Firefox, Edge).
- [x] La advertencia legal obligatoria aparece de manera visible y destacada.
- [x] No se almacenan ni recopilan datos personales reales.
- [x] Las claves de API no están incluidas directamente en el código fuente.
- [x] El repositorio contiene el código completo del proyecto.
- [x] Se realizó una prueba exhaustiva de funcionamiento antes de la entrega final.

---

## 🧠 Parte 5 — Guía de prompting para vibe coding
El desarrollo de LawTranslate se realizó utilizando inteligencia artificial como herramienta de apoyo para la programación (*vibe coding*). El proceso se dividió en diferentes hitos para mantener el control conceptual y la solidez jurídica.

### M0 — Delimitación
Se proporcionó a la IA el problema jurídico identificado (la opacidad del lenguaje judicial) y se solicitó ayuda para delimitar el alcance a sentencias de tutela y resoluciones de alto impacto social, definiendo un producto mínimo viable estructurado en cuatro bloques de comprensión.

### M1 — Instrucciones del asistente
Se construyó un prompt de sistema con reglas estrictas de estructura y ética jurídica:

```text
Eres LawTranslate, un asistente pedagógico de Colombia. Tu único trabajo es traducir
decisiones y sentencias judiciales colombianas a lenguaje ciudadano, claro y sin rodeos.

Responde ÚNICAMENTE en formato JSON válido con esta estructura exacta:
{
  "caso": "Breve resumen en 2 o 3 frases del conflicto",
  "decision": "Directo: si ganó o perdió el demandante o qué ordenó el juez",
  "esFavorable": true,
  "motivos": ["Motivo 1 en palabras sencillas", "Motivo 2 en palabras sencillas"],
  "efectos": "Plazos y qué debe hacer cada parte ahora",
  "glosario": [{"t": "Término técnico", "d": "Significado en lenguaje común"}]
}

REGLAS OBLIGATORIAS:
1. Usa lenguaje comprensible para una persona sin estudios jurídicos.
2. No inventes hechos ni citas normativas que no figuren en el extracto.
3. Especifica con precisión los plazos en días u horas señalados por el juez.
4. Identifica si la decisión es favorable o desfavorable al accionante.
5. Incluye siempre la advertencia de que este ejercicio no es asesoría legal.
```

### M2 — Pruebas
Se realizaron pruebas utilizando extractos reales de providencias para calibrar la respuesta del modelo, verificando que no inventara hechos no contenidos en el texto y que identificara adecuadamente los plazos procesales.

### M3 — RAG y Base de Conocimiento
Para garantizar la precisión de los conceptos jurídicos, se incorporó un diccionario normativo con términos como *desacato*, *pretensiones*, *término perentorio*, *cánones*, *ejecutoria* y *debido proceso*, asegurando que el glosario generado esté fundamentado en la ley colombiana.

### M4 — Interfaz
Finalmente, se solicitó a la IA construir una interfaz limpia y sobria que incluyera:
* Nombre institucional de la herramienta y distintivo de la Universidad Javeriana.
* Botones interactivos con los casos de prueba más representativos.
* Campo de texto amplio para pegar cualquier fallo.
* Botón de traducción con indicador visual de carga.
* Cuadrícula de resultados modulares con colores diferenciados según el sentido del fallo (verde para favorable, rojo para desfavorable).
* Advertencia legal visible en un recuadro superior.

---

## ⚖️ Parte 6 — Ética, datos y responsabilidad
LawTranslate fue diseñada teniendo en cuenta los riesgos y responsabilidades éticas asociadas al uso de inteligencia artificial en el sector jurídico.

### Advertencia legal obligatoria
La interfaz muestra de manera visible y permanente la siguiente advertencia:
> *“Advertencia Legal Obligatoria: Esta herramienta es un ejercicio académico para facilitar la comprensión de textos jurídicos. No constituye asesoría legal ni sustituye la consulta con un abogado debidamente graduado.”*

### Protección de datos (Ley 1581 de 2012)
La herramienta no está diseñada para recolectar ni almacenar datos personales reales. Las pruebas se realizan con extractos anonimizados de sentencias públicas o situaciones ficticias, garantizando la privacidad de las partes procesales.

### Corpus público
El sistema utiliza exclusivamente fuentes jurídicas públicas: la Constitución Política de Colombia, decretos reglamentarios y jurisprudencia publicada de la Corte Constitucional.

### Prevención de alucinaciones
Una de las reglas cardinales del asistente es no inventar normas, hechos ni consecuencias jurídicas. El modelo debe limitarse a explicar lo que está expresamente consignado en el texto judicial suministrado. Cuando no se detectan plazos explícitos, el sistema indica que aplican las reglas generales de cumplimiento sin especular.

---

## 🔍 Parte 7 — Análisis crítico

### 7.1 ¿Dónde falla la herramienta?
LawTranslate presenta limitaciones inherentes a los modelos de lenguaje y al procesamiento automático de textos jurídicos:

* **Primer caso (Sentencias con pluralidad de pretensiones o fallos mixtos):** Cuando una providencia resuelve múltiples pretensiones de forma dispar (por ejemplo, amparando el debido proceso pero negando el restablecimiento del derecho económico, o en fallos con salvamentos parciales de voto), la herramienta tiende a simplificar el resultado global y podría catalogar el fallo como enteramente favorable o desfavorable, perdiendo los matices técnicos del litigio.
* **Segundo caso (Textos procesales mutilados o altamente descontextualizados):** Si el usuario ingresa un fragmento incidental o un auto de mero trámite (ej. una fijación en lista o un traslado probatorio) creyendo que se trata de la sentencia definitiva, la herramienta puede extraer plazos procesales pero no tendrá el contexto suficiente para explicar el conflicto de fondo, debiendo advertir que se requiere la providencia resolutiva completa.

### 7.2 ¿Qué datos procesa?
* **Entrada:** El usuario introduce o selecciona un extracto de una providencia judicial colombiana.
* **Procesamiento:** El sistema analiza la estructura textual, detecta las partes procesales, identifica el verbo resolutivo (*amparar*, *negar*, *ordenar*) y extrae los plazos temporales, contrastándolos con el diccionario jurídico o enviándolos al modelo de OpenRouter.
* **Salida:** Se genera una traducción ciudadana modular en 4 tarjetas claras más un glosario de términos clave.
* **Almacenamiento:** El proyecto no almacena datos; todo el procesamiento ocurre en tiempo real en la memoria del navegador.

### 7.3 ¿Por qué no reemplaza al abogado?
LawTranslate **no reemplaza ni puede reemplazar a un abogado** porque la labor jurídica no se limita a traducir lo que un juez ya escribió, sino que exige una valoración estratégica integral de la situación fáctica, la anticipación de riesgos y la elección de los mecanismos de defensa idóneos. 

Un profesional del derecho puede evaluar la procedencia de recursos procesales (apelación, reposición o queja), interponer incidentes de desacato ante el incumplimiento del fallo, verificar si operaron figuras como la caducidad o la prescripción, y representar los intereses del cliente ante las instancias judiciales competentes bajo estricta responsabilidad ética y legal. LawTranslate es un puente pedagógico para cerrar la brecha de comprensión del ciudadano, pero la defensa efectiva de los derechos fundamentales exige invariablemente el criterio y la intervención de un abogado titulado.

---

## 📚 Parte 8 — Casos de prueba
Los casos de prueba se diseñaron para evaluar la capacidad de LawTranslate para identificar decisiones judiciales, resumir motivos y explicar términos técnicos sin alucinaciones.

Los casos completos con sus textos originales y salidas esperadas se encuentran en:  
📁 **[`docs/casos-de-prueba.md`](docs/casos-de-prueba.md)**

Entre los escenarios evaluados se incluyeron:
1. **🏥 Tutela de Salud (Negativa de Cirugía por EPS):** Orden perentoria de 48 horas bajo apercibimiento de desacato por vulneración del derecho a la salud y vida digna.
2. **🎓 Debido Proceso Disciplinario (Cancelación de Matrícula):** Nulidad de resolución sancionatoria por violación del principio *non bis in idem* y falta de contradicción probatoria.
3. **📩 Derecho de Petición (Silencio Administrativo):** Orden perentoria de 3 días hábiles para emitir respuesta de fondo, clara y congruente.
4. **🏠 Arrendamiento y Restitución de Inmueble:** Terminación de contrato por mora en cánones, plazo de 10 días para restituir el bien y condena en costas.
5. **✍️ Caso Libre / Texto Judicial Propio:** Campo en blanco para validar la robustez del motor frente a textos no preconfigurados.

---

## 👤 Parte 9 — Prueba con usuario real
Como parte de la validación del proyecto, se realizó una prueba con una persona externa al curso sin conocimientos jurídicos.

La persona utilizó **LawTranslate** para consultar la notificación de un fallo judicial real de tutela y posteriormente se recopiló su percepción sobre la claridad de las 4 tarjetas y la utilidad del glosario.

La evidencia completa de esta prueba se encuentra en:  
📁 **[`docs/evidencia-usuario.md`](docs/evidencia-usuario.md)**

La prueba demostró que una persona sin formación en leyes pudo identificar en menos de un minuto si el accionante había ganado o perdido el caso y cuál era el plazo de cumplimiento, validando la efectividad pedagógica de la herramienta.

---

## ✅ Parte 10 — Estado final del proyecto
| Requisito | Estado |
| :--- | :---: |
| Problema jurídico definido | ✅ |
| Usuario objetivo definido | ✅ |
| Alcance delimitado (Qué hace y qué NO hace) | ✅ |
| Marco jurídico y fuentes seleccionado | ✅ |
| Prompt del sistema desarrollado | ✅ |
| Casos de prueba realizados y documentados | ✅ |
| Corpus normativo y glosario implementados | ✅ |
| Interfaz web desarrollada y estilizada | ✅ |
| Advertencia legal obligatoria visible | ✅ |
| Protección de datos considerada | ✅ |
| Análisis crítico realizado | ✅ |
| Usuario externo probado | ✅ |
| URL pública desplegada y funcional | 🔗 [Ver en vivo](https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/) |
| Evidencia de usuario documentada | 📎 [`docs/evidencia-usuario.md`](docs/evidencia-usuario.md) |
| Historial de desarrollo en GitHub | ✅ |

---

## 🎓 Conclusión
**LawTranslate** demuestra cómo una herramienta de inteligencia artificial puede utilizarse como apoyo para democratizar la comprensión de las decisiones judiciales en Colombia, cerrando la brecha histórica entre el lenguaje técnico de los tribunales y el ciudadano común. El proyecto combina conocimientos de derecho constitucional y procesal con tecnologías web y modelos de lenguaje, estructurando las respuestas en dimensiones pedagógicas claras para mejorar el acceso a la justicia.

Sin embargo, el proyecto también evidencia con claridad los límites de la tecnología en el derecho: la simplificación lingüística jamás debe confundirse con la asesoría estratégica, y la inteligencia artificial nunca podrá sustituir el juicio crítico, la empatía y la responsabilidad profesional de un abogado graduado. Por esta razón, LawTranslate se consolida como un ejercicio académico de apoyo ciudadano y pedagogía constitucional.

*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖

---

### About
Asistente de inteligencia artificial y pedagogía legal para traducir sentencias y providencias judiciales colombianas a lenguaje ciudadano claro, estructurado y comprensible.
