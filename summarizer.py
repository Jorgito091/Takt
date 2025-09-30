from transformers import pipeline

def generar_resumen(texto, max_length=50, min_length=20):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    resultado = summarizer(texto, max_length=max_length, min_length=min_length, do_sample=False)
    return resultado[0]['summary_text']