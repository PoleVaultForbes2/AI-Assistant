from typing import Dict
from tools.notes_tool import save_note
from tools.ollama_tool import query_ollama


def extract_note_with_llm(raw_input: str) -> str:
    prompt = f"""Extract the actual note content from the following user input. 
    Only return the exact text they wanted to save as the note. 
    Do not include any surrounding words or explanation.

    User input: "{raw_input}"
    Note content:"""

    response = query_ollama(prompt).strip()

    return response.strip('"')


def add_note_to_file_node(state: Dict) -> Dict:
    input_text = state["input"]

    try:
        note_content = extract_note_with_llm(input_text)
        save_note(note_content)
        state["output"] = "Note saved successfully."
    except Exception as e:
        state["output"] = f"Failed to save note: {e}"

    return state
