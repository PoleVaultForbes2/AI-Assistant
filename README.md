<!-- Markdeep: README.md -->
<!-- Automatically formats with Markdeep in supported viewers -->

# 🧠 AI Assistant (Local, Private, Extendable)

> A locally running voice- and text-based AI assistant that helps you manage your email, calendar, and notes—all powered by [Ollama](https://ollama.com), [LangChain](https://www.langchain.com/), and [LangGraph](https://www.langchain.com/langgraph).

---

## 🚀 Features

- 🧾 **Email Summarization**  
  Ask the assistant to summarize your latest iCloud emails by speaking or typing a request like:  
  _“Summarize my last 5 emails.”_

- 📆 **Calendar Integration**  
  Add events naturally:  
  _“Schedule a haircut on Saturday at 3pm.”_

- 📝 **Quick Notes**  
  Save short-form thoughts or reminders:  
  _“Add a note that says I’m happy.”_

- 🤖 **Natural Language Routing**  
  LangGraph + Ollama help intelligently determine your intent without needing rigid commands.

- 🔒 **Fully Local & Private**  
  Nothing leaves your device. Your data stays yours.

---

## 🛠️ Tech Stack

| Component         | Description                                |
|------------------|--------------------------------------------|
| `Ollama + Mistral` | Local language model for natural language understanding |
| `LangChain`       | Orchestrates tools and agents             |
| `LangGraph`       | Manages flow control and state routing    |
| `SpeechRecognition + PyAudio` | Voice input via microphone    |
| `iCloud + IMAP`   | Access emails securely from iCloud        |
| `.ics / Calendar API` | Adds calendar events locally or to a service |
| `Plaintext or JSON` | Notes are stored in editable files       |

---

## 🧪 Example Usage

```
You: Summarize my last 4 emails  
AI:  
**Subject:** Meeting Follow-Up  
Summary: Here's a recap of yesterday's meeting and next steps...

**Subject:** Invoice #8294  
Summary: Your monthly invoice has been issued...
```

```
You: Add a calendar event: dentist appointment Friday at 10am  
AI: Event added to your calendar successfully.
```

```
You: Add a note that says “research Ollama fine-tuning”  
AI: Note saved successfully.
```

---

## 🧰 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/ai-assistant.git
cd ai-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

Make sure [Ollama](https://ollama.com/download) is installed and running:
```bash
ollama run mistral
```

### 4. Run the Assistant

```bash
python main.py
```

---

## 📁 Project Structure

```
ai-assistant/
│
├── main.py                     # Entry point
├── langgraph_agent.py          # LangGraph setup and flow
├── tools/                      # Email, notes, calendar tools
│   ├── email_tool.py
│   ├── notes_tool.py
│   ├── calendar_tool.py
│   └── __init__.py
├── nodes/                      # LangGraph-compatible nodes
│   ├── email_node.py
│   ├── notes_node.py
│   ├── calendar_node.py
│   └── router_node.py
├── ollama_model.py             # Mistral model setup
├── requirements.txt
└── README.md
```

---

## 💡 Future Ideas & Improvements

- ✅ Add fallback logic for unclear input ("pickles" → “Please give a real request.”)
- 🔊 Add voice **output** using TTS
- 🔐 Add local user authentication or passphrase protection
- 📥 Connect to Gmail or Outlook in addition to iCloud
- 🌐 Add simple web dashboard using Flask or FastAPI
- 🧠 Use memory/chains to enable back-and-forth conversations
- 📂 Save notes as Markdown files organized by date
- ✨ Add vector memory for semantic recall of past notes or events

---

## 🙌 Credits

- Built with [LangChain](https://www.langchain.com/), [LangGraph](https://www.langchain.com/langgraph), and [Ollama](https://ollama.com).
- Voice input via [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

---

## 📜 License

MIT License
