import streamlit as st
from summarizer import summarize
from developer import expand

st.set_page_config(page_title="AI Generator: Summarize or Expand", layout="centered")

st.title("📝 AI Thing")
st.write("Choose if you want to summarize or expand your text using artificial intelligence.")

mode = st.selectbox("What do you want to do?", ["Summarize", "Expand"])
text = st.text_area("Text:", height=200)

if st.button("Process"):
    if text.strip():
        with st.spinner("Processing..."):
            if mode == "Summarize":
                result = summarize(text)
                st.subheader("Generated summary:")
            else:
                result = expand(text)
                st.subheader("Expanded text:")
        st.success(result)
    else:
        st.warning("Please enter some text to process.")