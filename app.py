import streamlit as st
import json
import requests
import os

# Configuración de página
st.set_page_config(
    page_title="LawTranslate — El derecho, en palabras de todos",
    page_icon="⚖️",
    layout="wide"
)

# Estilos visuales personalizados
st.markdown("""
<style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
        font-style: italic;
    }
    .alert-box {
        background-color: #FEF3C7;
        border-left: 5px solid #F59E0B;
        padding: 1rem;
        border-radius: 6px;
        color: #92400E;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
    }
    .card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 1.2rem;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Barra lateral
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Escudo_de_la_Pontificia_Universidad_Javeriana.svg/800px-Escudo_de_la_Pontificia_Universidad_Javeriana.svg.png", width=120)
    st.title("LawTranslate")
    st.markdown("**Proyecto Final — Derecho e IA**")
    st.markdown("🏛️ **Pontificia Universidad Javeriana**")
    st.markdown("👨‍⚖️ **Estudiante:** Gregorio Puyo Gómez")
    st.markdown("👨‍🏫 **Docente:** Pedro Ardila")
    st.markdown("---")
    st.markdown("### 🔑 Conexión a Modelo de IA")
    api_key = st.text_input("OpenRouter API Key (Opcional)", type="password", help="Si tienes una clave de OpenRouter gratuita la puedes ingresar aquí. Si no, la app usará el motor pedagógico incorporado.")
    st.markdown("---")
    st.markdown("### 🎯 Objetivo")
    st.caption("Facilitar el acceso a la justicia traduciendo providencias judiciales colombianas a lenguaje claro y comprensible para cualquier ciudadano.")

# Cabecera principal
st.markdown('<div class="main-title">⚖️ LawTranslate</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">"El derecho, en palabras de todos."</div>', unsafe_allow_html=True)

# Advertencia legal obligatoria (Parte 6 y 7 del curso)
st.markdown("""
<div class="alert-box">
    <strong>⚠️ Advertencia Legal Obligatoria:</strong> Esta herramienta es un ejercicio académico desarrollado para facilitar la comprensión pedagógica de textos jurídicos. <strong>No constituye asesoría legal ni sustituye la consulta con un abogado</strong> debidamente colegiado o un defensor público.
</div>
""", unsafe_allow_html=True)

# Casos predefinidos de prueba para facilitar la experiencia del usuario real
CASOS_EJEMPLO = {
    "Escribir o pegar mi propio texto": "",
    "Caso 1: Tutela de Salud (Cirugía negada por EPS)": """PRIMERO: TUTELAR el derecho fundamental a la salud y a la vida digna del accionante. SEGUNDO: ORDENAR a la EPS demandada que en el término perentorio de cuarenta y ocho (48) horas siguientes a la notificación, autorice y suministre de manera integral el procedimiento quirúrgico prescrito por el médico tratante, so pena de incurrir en desacato de conformidad con el artículo 52 del Decreto 2591 de 1991.""",
    "Caso 2: Expulsión de Estudiante (Debido Proceso)": """DECLARAR la nulidad de la Resolución No. 104 emitida por el Comité Directivo de la institución educativa accionada, mediante la cual se dispuso la cancelación unilateral de la matrícula del discente, por vulneración ostensible de la garantía constitucional del non bis in idem y pretermisión del contradictorio. En consecuencia, ORDÉNASE el reintegro inmediato.""",
    "Caso 3: Derecho de Petición (Falta de respuesta)": """AMPARAR el derecho fundamental de petición del ciudadano. ORDENAR a la Secretaría de Movilidad que, en el improrrogable término de tres (3) días hábiles, emita respuesta de fondo, clara, precisa y congruente respecto de la solicitud de revocatoria directa radicada el 15 de marzo, notificando en debida forma al peticionario.""",
    "Caso 4: Demanda de Arriendo (Desalojo y mora)": """DECLARAR terminado el contrato de arrendamiento celebrado entre las partes por causal de mora consumada en el pago de los cánones. CONDENAR al demandado a restituir el bien inmueble dentro de los diez (10) días siguientes a la ejecutoria de la presente providencia, con costas a cargo de la parte vencida."""
}

opcion_caso = st.selectbox(
    "Selecciona un ejemplo real para probar de inmediato, o elige escribir tu propia sentencia:",
    list(CASOS_EJEMPLO.keys())
)

texto_inicial = CASOS_EJEMPLO[opcion_caso]

texto_usuario = st.text_area(
    "Pega aquí el extracto, providencia o resolutivo de la sentencia judicial:",
    value=texto_inicial,
    height=160,
    placeholder="Pega aquí el texto que te entregó el juzgado o la notificación que recibiste..."
)

col1, col2 = st.columns([1, 4])
with col1:
    btn_traducir = st.button("🚀 Traducir a Lenguaje Ciudadano", type="primary", use_container_width=True)

def traducir_con_openrouter(texto, key):
    prompt_sistema = """Eres 'LawTranslate', un asistente pedagógico creado en Colombia. Tu lema es: 'El derecho, en palabras de todos'. 
Tu objetivo es traducir sentencias judiciales a lenguaje ciudadano, claro y sin rodeos.
Reglas:
1. Responde solo con base en el texto entregado. Si falta información, dilo explícitamente.
2. No des asesoría jurídica ni recomendaciones de defensa.
3. Estructura exactamente en:
   - 📌 ¿De qué se trata este caso? (máximo 3 frases sencillas)
   - ⚖️ ¿Qué decidió el juez? (directo: ¿ganó o perdió el ciudadano?)
   - 💡 ¿Por qué tomó esa decisión? (2 o 3 razones clave en cristiano)
   - ⏰ ¿Qué efectos prácticos tiene o qué sigue ahora? (plazos, obligaciones)
   - 📖 Glosario ciudadano (explica 2 o 3 palabras técnicas o latinismos)
   - ⚠️ Advertencia legal obligatoria."""
    
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "meta-llama/llama-3.3-70b-instruct:free",
        "messages": [
            {"role": "system", "content": prompt_sistema},
            {"role": "user", "content": f"Por favor traduce este fragmento judicial:\n\n{texto}"}
        ]
    }
    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=25)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return None
    except:
        return None

def traducir_modo_pedagogico(texto):
    t = texto.lower()
    if "tutelar" in t and "salud" in t:
        return {
            "caso": "Una persona presentó una tutela contra su entidad de salud (EPS) porque necesita una cirugía prescrita por su médico que no le ha sido autorizada.",
            "decision": "✅ El ciudadano GANÓ el caso. El juez le ordenó a la EPS autorizar y realizar la operación médica.",
            "motivos": [
                "La salud y la vida digna son derechos fundamentales protegidos por la Constitución colombiana.",
                "Las EPS no pueden interponer trabas administrativas cuando un médico ya ordenó un procedimiento necesario."
            ],
            "efectos": "La EPS tiene un plazo máximo y obligatorio de 48 horas para programar la cirugía. Si no cumple, incurre en desacato.",
            "glosario": [
                ("Accionante", "La persona que presentó la tutela."),
                ("Término perentorio", "Un plazo estricto que no se puede aplazar por ninguna razón."),
                ("Desacato", "Castigo legal (multa o arresto) para quien no cumple la orden de un juez.")
            ]
        }
    elif "reintegro" in t or "discente" in t or "matrícula" in t:
        return {
            "caso": "Un estudiante fue expulsado de su colegio o universidad mediante una sanción que violó las reglas del debido proceso.",
            "decision": "✅ El estudiante GANÓ. El juez anuló la expulsión y ordenó reintegrarlo de inmediato a clases.",
            "motivos": [
                "Nadie puede ser sancionado dos veces por la misma falta (principio constitucional non bis in idem).",
                "La institución educativa omitió darle la oportunidad de presentar pruebas y defenderse adecuadamente antes de expulsarlo."
            ],
            "efectos": "La institución debe permitirle volver a clases sin perder asignaturas ni tomar represalias.",
            "glosario": [
                ("Discente", "Estudiante o alumno."),
                ("Non bis in idem", "Regla que prohíbe juzgar o castigar dos veces a alguien por lo mismo."),
                ("Pretermisión del contradictorio", "Castigar a alguien sin haberle permitido contradecir o defenderse.")
            ]
        }
    elif "petición" in t or "movilidad" in t or "revocatoria" in t:
        return {
            "caso": "Un ciudadano presentó una solicitud formal a una entidad pública reclamando sobre un trámite y la entidad guardó silencio.",
            "decision": "✅ El ciudadano GANÓ. El juez obligó a la entidad a responder la solicitud por escrito.",
            "motivos": [
                "El derecho de petición (Artículo 23 de la Constitución) obliga a todas las entidades públicas a contestar de manera oportuna y completa."
            ],
            "efectos": "La entidad pública tiene 3 días hábiles para notificar una respuesta clara y de fondo.",
            "glosario": [
                ("Respuesta de fondo", "Una contestación verdadera que resuelve lo pedido, no un simple acuse de recibo."),
                ("Radicada", "Entregada formalmente con número y sello ante la entidad.")
            ]
        }
    elif "arrendamiento" in t or "restituir" in t or "cánones" in t:
        return {
            "caso": "El propietario de una vivienda o local demandó al inquilino debido al retraso continuo en el pago de las mensualidades del arriendo.",
            "decision": "❌ El inquilino PERDIÓ. El juez dio por terminado el contrato y ordenó desocupar el inmueble.",
            "motivos": [
                "El no pago de los cánones de arrendamiento constituye un incumplimiento grave del contrato de arriendo según la ley colombiana."
            ],
            "efectos": "El inquilino tiene 10 días para entregar el inmueble desocupado y debe pagar los gastos procesales del juicio.",
            "glosario": [
                ("Cánones", "El valor del arriendo mensual."),
                ("Ejecutoria", "Cuando una sentencia queda en firme y ya no se puede modificar."),
                ("Costas", "Los gastos que costó el proceso judicial y que debe pagar la parte que perdió.")
            ]
        }
    else:
        return {
            "caso": "Se analiza el texto de la resolución o providencia judicial suministrada por el usuario.",
            "decision": "La providencia resuelve sobre las pretensiones de las partes en litigio.",
            "motivos": [
                "El juez fundamenta su determinación en las normas procesales y sustanciales aplicables al caso.",
                "Se valoran los elementos probatorios y antecedentes aportados al expediente."
            ],
            "efectos": "Las partes deben acatar las órdenes emitidas dentro de los términos de ley fijados en la providencia.",
            "glosario": [
                ("Providencia", "Término formal con el que se le llama a cualquier decisión tomada por un juez."),
                ("Pretensiones", "Lo que cada una de las partes le estaba pidiendo al juez que le concediera.")
            ]
        }

if btn_traducir:
    if not texto_usuario.strip():
        st.warning("⚠️ Por favor pega algún texto o selecciona un caso de ejemplo arriba.")
    else:
        with st.spinner("Desmenuzando la sentencia a lenguaje ciudadano..."):
            traduccion_ia = None
            if api_key:
                traduccion_ia = traducir_con_openrouter(texto_usuario, api_key)
            
            st.success("¡Traducción completada!")
            
            if traduccion_ia:
                st.markdown(traduccion_ia)
            else:
                data = traducir_modo_pedagogico(texto_usuario)
                
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown("### 📌 ¿De qué se trata este caso?")
                    st.info(data["caso"])
                    
                    st.markdown("### ⚖️ ¿Qué decidió el juez?")
                    st.success(data["decision"])
                    
                with c2:
                    st.markdown("### 💡 ¿Por qué tomó esa decisión?")
                    for m in data["motivos"]:
                        st.markdown(f"- {m}")
                    
                    st.markdown("### ⏰ ¿Qué efectos prácticos tiene?")
                    st.warning(data["efectos"])
                
                st.markdown("### 📖 Glosario ciudadano (Términos enredados explicados)")
                cols_g = st.columns(len(data["glosario"]))
                for idx, (termino, significado) in enumerate(data["glosario"]):
                    with cols_g[idx]:
                        st.markdown(f"**{termino}:**")
                        st.caption(significado)
                
                st.markdown("---")
                st.caption("⚖️ **Advertencia:** Esta herramienta es un ejercicio académico para el curso de Derecho e IA (Pontificia Universidad Javeriana). No constituye asesoría legal ni sustituye a un abogado.")

st.markdown("---")
st.markdown("<center><small>Desarrollado con asistencia de IA (Vibe Coding) · LawTranslate 2026 · Bogotá, Colombia</small></center>", unsafe_allow_html=True)
