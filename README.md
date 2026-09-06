# ⚖️🤖 Proyecto Final — Derecho e Inteligencia Artificial
**Pontificia Universidad Javeriana · 2026-II · Docente: Pedro Ardila**
> **Estudiante:** Gregorio Puyo Gómez 
> **Nombre del proyecto:** LawTranslate
> **Fecha de inicio:** 2026-08-23
---
Bienvenido/a a tu repositorio de proyecto. **Este archivo es tu tablero de mando**: aquí describes tu proyecto, planificas su desarrollo y dejas evidencia del avance. Lo vas a completar por partes, siguiendo el curso.
**No necesitas saber programar.** Todo el código lo construirás con asistencia de IA (*vibe coding*). Tu valor como estudiante de derecho está en el problema que eliges, las fuentes que alimentas, las instrucciones que diseñas y el juicio crítico con el que evalúas el resultado.
---
## 📋 Parte 1 — Descripción del proyecto
### 1.1 El problema jurídico
En Colombia, las sentencias y providencias judiciales están redactadas en un lenguaje técnico, barroco y denso, cargado de latinismos y formalismos procesales que resultan incomprensibles para el ciudadano de a pie. Esto genera una barrera crítica de acceso a la administración de justicia (Art. 229 C.P.): las personas no entienden si ganaron o perdieron un proceso, qué resolvió el juez, qué derechos les fueron reconocidos o qué obligaciones y plazos deben cumplir. Hoy en día, un ciudadano sin recursos económicos para pagar una consulta jurídica particular queda en total indefensión e incertidumbre, viéndose obligado a recurrir a interpretaciones erróneas de terceros o a resignarse sin entender la decisión que afecta su vida, patrimonio o libertad.
### 1.2 Usuarios
Cualquier ciudadano colombiano involucrado en un proceso judicial (o afectado por una decisión de tutela, juzgado de familia, civil o laboral) que recibe una providencia o sentencia y no cuenta con conocimientos jurídicos ni con recursos para pagarle a un abogado solo para que le traduzca qué resolvió el juez.
### 1.3 Qué hace y qué NO hace (alcance)
| ✅ Sí hace | ❌ No hace |
| --- | --- |
| Recibir fragmentos o resolutivos de sentencias y providencias judiciales colombianas. | NO da asesoría jurídica personalizada ni diseña estrategias procesales. |
| Traducir la decisión a lenguaje claro, estructurado en 4 puntos: hechos, decisión del juez, razones principales y efectos/plazos prácticos. | NO redacta demandas, tutelas, recursos ni memoriales legales. |
| Explicar términos jurídicos complejos o latinismos a través de un glosario ciudadano sencillo. | NO actúa en nombre del usuario ni reemplaza la consulta con un abogado o defensor público. |
| Citar con precisión las partes y fuentes de la providencia analizada sin inventar contenido. | NO garantiza resultados favorables ante los despachos judiciales. |
### 1.4 Marco jurídico y fuentes
- [x] **Fundamento Constitucional:** Artículos 29 (Debido Proceso y Derecho a la Defensa) y 229 (Garantía del Derecho de Acceso a la Administración de Justicia) de la Constitución Política de Colombia.
- [x] **Política Pública de Lenguaje Claro:** Protocolo de Lenguaje Claro de la Rama Judicial de Colombia y lineamientos del Departamento Nacional de Planeación (DNP) para la simplificación del lenguaje administrativo y judicial.
- [x] **Corpus piloto de prueba:** Selección de sentencias colombianas reales y públicas (en materia de tutela y derechos ciudadanos) para calibración y verificación de respuestas.
### 1.5 Nombre y lema
**LawTranslate** — *"El derecho, en palabras de todos."*
---
## 🗺️ Parte 2 — Plan de desarrollo
Marca cada hito cuando lo termines. Los hitos siguen las sesiones del curso.
- [x] **M0 — Descripción y plan** *(con Sesión 1)*: Partes 1 y 2 de este README completas.
- [x] **M1 — Asistente con instrucciones v1** *(Sesión 1–2)*: redactaste las instrucciones (prompt de sistema) de tu asistente y funcionan en una herramienta gratuita de chat. Guardado en `prompt_sistema_v1.md`.
- [x] **M2 — Casos de prueba documentados** *(Sesión 2)*: tienes al menos 5 casos de prueba con resultados guardados en `casos-de-prueba.md`.
- [x] **M3 — Corpus conectado (RAG)** *(Sesión 3)*: tu asistente cita la fuente normativa que usa y no inventa. Corpus cargado en `sentencias_referencia.md`.
- [x] **M4 — Interfaz web desplegada** *(Sesión 4)*: tu herramienta tiene **URL pública**: [https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/](https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/).
- [ ] **M5 — Análisis crítico y demo** *(Sesión 5)*: Parte 7 completada + presentación de 5 minutos.
### Bitácora de avance semanal
| Semana | Qué hice | Enlace/captura | Dudas para la clase |
| --- | --- | --- | --- |
| 1 | Delimitación del problema (LawTranslate) y creación de instrucciones v1 | [prompt_sistema_v1.md](prompt_sistema_v1.md) | Ninguna, alcance claro |
| 2 | Documentación de 5 casos de prueba reales | [casos-de-prueba.md](casos-de-prueba.md) | Formatos de sentencias |
| 3 | Preparación del corpus normativo de referencia | [sentencias_referencia.md](sentencias_referencia.md) | Despliegue en la nube |
| 4 | Despliegue de aplicación web interactiva en vivo | [LawTranslate Web App](https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/) | Funcionando en línea |
| 5 | | | |
---
## 🛠️ Parte 3 — Stack técnico recomendado
Todo es **gratuito y no exige tarjeta de crédito**. Tu proyecto final se estructuró así:

| Pieza | Herramienta | Para qué sirve |
| --- | --- | --- |
| **Interfaz web** | **HTML5 / GitHub Pages** | Lo que el usuario ve: botones interactivos, cajas de texto, tarjetas claras. |
| **Orquestación** | **Lógica pedagógica estructurada** | Toma la sentencia y la traduce a los 4 puntos clave más glosario. |
| **Modelo** | **Motor de Lenguaje Claro** | Simplificación y traducción al lenguaje cotidiano. |
| **Corpus de fuentes** | **Sentencias de referencia** | Casos de tutela, debido proceso y derecho de petición en `sentencias_referencia.md`. |
---
## 🚀 Parte 4 — Ruta de despliegue
### Checklist de despliegue ✅
- [x] URL pública funciona en el navegador de otra persona: [https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/](https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/)
- [x] La advertencia obligatoria es **visible** en la interfaz
- [x] No hay API keys ni secretos en el código
- [x] Anota la URL aquí: **`https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/`**
---
## ⚖️ Parte 5 y 6 — Ética, datos y responsabilidad
- **Advertencia visible obligatoria:**
  > *"Esta herramienta es un ejercicio académico que no constituye asesoría legal ni sustituye la consulta con un abogado."*
  - [x] Implementada y visible en la interfaz web
- **Protección de datos (Ley 1581 de 2012):** No recolecta ni almacena datos personales reales.
  - [x] Verificado: no guardo datos personales
- **Corpus público:** Solo providencias y fuentes públicas.
  - [x] Verificado
- **Anti-alucinaciones:** El asistente admite cuando la providencia no contiene el dato consultado.
  - [x] Verificado en casos de prueba
---
## 🔍 Parte 7 — Análisis crítico (insumo de tu sustentación final)
1. **¿Dónde falla tu herramienta?** Cuando se le ingresan sentencias sumamente extensas sin orden resolutivo claro, o cuando el usuario intenta pedirle asesoría sobre cómo demandar en vez de traducir una decisión existente.
2. **¿Qué datos procesa?** Entra el texto del fallo judicial pegado por el usuario, no se almacena ningún dato personal en servidores, y sale la traducción pedagógica estructurada.
3. **¿Por qué no reemplaza al abogado?** Porque la herramienta únicamente cumple una función explicativa y formativa para democratizar el entendimiento del fallo; la valoración de la estrategia jurídica, interposición de recursos y representación procesal requieren obligatoriamente del criterio, ética y habilitación profesional de un abogado.
---
## ✅ Parte 8 — Entregables finales (Definition of Done)
- [x] 🔗 **Solución funcionando**: resuelve el problema jurídico y está desplegada con URL pública: [https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/](https://4n4tb75f27-creator.github.io/Traducci-n-de-sentencias-a-lenguaje-ciudadano-/).
- [ ] 👤 **Usuario real**: al menos una persona externa al curso la usó, con evidencia (video corto o testimonio). Guarda la evidencia en `docs/evidencia-usuario.md`.
- [x] 📦 **Repositorio con historial**: este repo muestra tus avances semanales (commits + bitácora).
- [x] 🧠 **Análisis crítico**: Parte 7 completada.
- [x] 📋 Partes 1–7 de este README completas y al día.
---
*Construido con asistencia de IA — como se enseña en este curso.* 🧑‍⚖️🤖
