from transformers import pipeline

def expand(text, model_name="gpt2", max_length=100):
    generator = pipeline("text-generation", model=model_name)
    prompt = f"Expand the following text: {text}"
    result = generator(prompt, max_length=max_length, num_return_sequences=1)
    expanded_text = result[0]['generated_text'].replace(prompt, "").strip()
    return expanded_text