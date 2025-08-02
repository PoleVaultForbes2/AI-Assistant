from typing import Dict
from ollama_model import get_ollama_model
from tools.calendar_tool import add_event_to_calendar
import json


llm = get_ollama_model()


def add_event_to_calendar_node(state: Dict) -> Dict:
    input_text = state.get("input", "")

    prompt = f"""
    You are an assistant that creates calendar events. 
    Extract the event title, date/time, and duration from the user's input.

    Respond ONLY with a JSON object in this format:
    {{
      "title": "...",
      "start_time": "...",      # ISO 8601 preferred, or a date/time string like "August 3rd, 3pm"
      "duration_minutes": 60
    }}

    User input: "{input_text}"
        """

    response = llm.invoke(prompt)

    try:
        event_data = json.loads(response)
        result = add_event_to_calendar(
            title=event_data["title"],
            start_time=event_data["start_time"],
            duration_minutes=event_data["duration_minutes"]
        )
        return {"output": result}
    except json.JSONDecodeError as e:
        return {"output": f"❌ Failed to parse calendar input: {e}"}
    except Exception as e:
        return {"output": f"❌ Unexpected error: {e}"}
