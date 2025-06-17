import streamlit as st

# Configuración inicial de página
st.set_page_config(page_title="Simulador Análisis de Mercado", layout="wide")

# Título y descripción
st.title("🧠 Simulador de Análisis de Mercado")
st.markdown("""
Este simulador te ayudará a comprender cómo realizar un análisis de mercado mediante el uso de herramientas estratégicas.
Identificarás fortalezas, debilidades, oportunidades y amenazas, y aprenderás a generar estrategias cruzadas efectivas.
""")

# Inicialización de session_state si no existe
if 'fortalezas' not in st.session_state:
    st.session_state.fortalezas = []
if 'debilidades' not in st.session_state:
    st.session_state.debilidades = []
if 'oportunidades' not in st.session_state:
    st.session_state.oportunidades = []
if 'amenazas' not in st.session_state:
    st.session_state.amenazas = []

# Selector de modo (empresa ficticia o libre)
modo = st.selectbox("Selecciona el modo:", ["Modo Libre", "Modo Empresa Ficticia"])

# Datos predefinidos para el modo ficticio
if modo == "Modo Empresa Ficticia":
    st.markdown("### 🏢 Empresa Ficticia: *H&M*")
    st.markdown("Sector: Retail.")
    st.markdown("Ingresa tus hallazgos basados en esta empresa.")

# Secciones por pestañas
tab1, tab2, tab3, tab4 = st.tabs(["🔍 Análisis Interno", "🌐 Análisis Externo", "🎯 Estrategias Cruzadas", "📚 Ejemplo Práctico"])

with tab1:
    st.subheader("🔹 Fortalezas")
    nueva_fortaleza = st.text_input("Agregar una fortaleza:")
    if st.button("➕ Añadir Fortaleza"):
        if nueva_fortaleza:
            st.session_state.fortalezas.append(nueva_fortaleza)

    st.write("Lista de fortalezas:")
    for f in st.session_state.fortalezas:
        st.write(f"- {f}")

    st.subheader("🔸 Debilidades")
    nueva_debilidad = st.text_input("Agregar una debilidad:")
    if st.button("➕ Añadir Debilidad"):
        if nueva_debilidad:
            st.session_state.debilidades.append(nueva_debilidad)

    st.write("Lista de debilidades:")
    for d in st.session_state.debilidades:
        st.write(f"- {d}")

with tab2:
    st.subheader("🔺 Oportunidades")
    nueva_oportunidad = st.text_input("Agregar una oportunidad:")
    if st.button("➕ Añadir Oportunidad"):
        if nueva_oportunidad:
            st.session_state.oportunidades.append(nueva_oportunidad)

    st.write("Lista de oportunidades:")
    for o in st.session_state.oportunidades:
        st.write(f"- {o}")

    st.subheader("🔻 Amenazas")
    nueva_amenaza = st.text_input("Agregar una amenaza:")
    if st.button("➕ Añadir Amenaza"):
        if nueva_amenaza:
            st.session_state.amenazas.append(nueva_amenaza)

    st.write("Lista de amenazas:")
    for a in st.session_state.amenazas:
        st.write(f"- {a}")

with tab3:
    st.subheader("🎯 Generador de Estrategias Cruzadas")

    # Estrategias ofensivas (F + O)
    if st.session_state.fortalezas and st.session_state.oportunidades:
        st.markdown("#### 🔥 Estrategias Ofensivas (Fortalezas + Oportunidades)")
        for f in st.session_state.fortalezas:
            for o in st.session_state.oportunidades:
                st.write(f"👉 Utilizar '{f}' para aprovechar '{o}'.")

    else:
        st.info("💡 Ingresa al menos una fortaleza y una oportunidad para ver estrategias ofensivas.")

    # Estrategias de orientación (D + O)
    if st.session_state.debilidades and st.session_state.oportunidades:
        st.markdown("#### 🧭 Estrategias de Orientación (Debilidades + Oportunidades)")
        for d in st.session_state.debilidades:
            for o in st.session_state.oportunidades:
                st.write(f"👉 Superar '{d}' mediante '{o}'.")

    else:
        st.info("💡 Ingresa al menos una debilidad y una oportunidad para ver estrategias de orientación.")

    # Estrategias defensivas (A + F)
    if st.session_state.amenazas and st.session_state.fortalezas:
        st.markdown("#### 🛡️ Estrategias Defensivas (Amenazas + Fortalezas)")
        for a in st.session_state.amenazas:
            for f in st.session_state.fortalezas:
                st.write(f"👉 Usar '{f}' para contrarrestar '{a}'.")

    else:
        st.info("💡 Ingresa al menos una amenaza y una fortaleza para ver estrategias defensivas.")

    # Estrategias de supervivencia (A + D)
    if st.session_state.amenazas and st.session_state.debilidades:
        st.markdown("#### 💀 Estrategias de Supervivencia (Amenazas + Debilidades)")
        for a in st.session_state.amenazas:
            for d in st.session_state.debilidades:
                st.write(f"⚠️ La combinación de '{d}' y '{a}' puede ser crítica.")

    else:
        st.info("💡 Ingresa al menos una amenaza y una debilidad para ver estrategias de supervivencia.")

with tab4:
    st.subheader("📚 Ejemplo Práctico")
    st.markdown("""
    Imagina que trabajas para *Tecnología Verde S.A.*, una empresa que fabrica dispositivos inteligentes para ahorrar energía en hogares.

    ### Ejemplo de DAFO:
    - **Fortalezas**: Innovación constante, marca reconocida.
    - **Debilidades**: Alto costo de producción.
    - **Oportunidades**: Subsidios gubernamentales para energías limpias.
    - **Amenazas**: Competencia internacional con precios más bajos.

    ### Estrategia Ofensiva:
    > "Usar nuestra innovación para aprovechar los subsidios y lanzar nuevos productos."

    ### Estrategia de Supervivencia:
    > "Reducir costos de producción para competir con empresas extranjeras."

    ¡Ahora prueba tú!
    """)

# Botón para reiniciar
if st.button("🔄 Reiniciar Análisis"):
    st.session_state.fortalezas.clear()
    st.session_state.debilidades.clear()
    st.session_state.oportunidades.clear()
    st.session_state.amenazas.clear()
    st.success("✅ Análisis reiniciado correctamente.")

# --- Footer con Copyright ---
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: #666; font-size: 0.9em;">
        © 2025 Simulador de Análisis de Mercado | Desarrollado por Wilton Torvisco  
        <br>
        
    </div>
""", unsafe_allow_html=True)