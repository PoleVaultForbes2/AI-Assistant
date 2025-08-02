# from langchain.tools import Tool

NOTES_FILE = "data/notes.txt"


def save_note(note: str) -> str:
    if not note.strip():
        return "You must provide a note to save."

    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(note.strip() + "\n")

    return "Note saved successfully."


def read_notes(_: str = "") -> str:
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            notes = f.readlines()
        return "Here are your notes:\n" + "".join(notes)
    except FileNotFoundError:
        return "No notes found yet."
