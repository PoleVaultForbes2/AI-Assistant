# tools/ollama_tool.py
from ollama_model import get_ollama_model

llm = get_ollama_model()


def query_ollama(prompt: str) -> str:
    return llm.invoke(prompt)