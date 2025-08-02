# ollama_model.py
from langchain_ollama import OllamaLLM


def get_ollama_model():
    return OllamaLLM(model="mistral")  # Or whatever model you use
