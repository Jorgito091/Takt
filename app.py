import streamlit as st
from summarizer import generar_resumen

st.set_page_config(page_title="Generador de Resúmenes IA", layout="centered")

st.title("📝 Generador de Resúmenes IA")
st.write("Ingresa un texto largo y obtén un resumen generado por inteligencia artificial.")

texto = st.text_area("Texto a resumir:", height=200)

if st.button("Generar resumen"):
    if texto.strip():
        with st.spinner("Procesando..."):
            resumen = generar_resumen(texto)
        st.subheader("Resumen generado:")
        st.success(resumen)
    else:
        st.warning("Por favor, ingresa algún texto para resumir.")