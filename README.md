# 🧠 AI Agent for Malaysian School Kids 🇲🇾

Welcome to the **Future ICT Coders** AI Agent!  
This is a simple, smart assistant designed especially for **Malaysian school children** to explore fun and helpful AI tools — safely and interactively.

---

## 🚀 What It Does

This conversational AI can:
- 🧮 **Solve math problems** (e.g. "What is 12 + 4?")
- ⏰ **Set reminders** (e.g. "Remind me to do homework at 8PM")
- 🎉 **Share fun facts** about Malaysia (e.g. "Tell me something interesting!")
- 🌤️ (Optional) **Get live weather updates** using real APIs

---

## 🛠️ How It Works

🔧 The assistant uses **Groq** as the underlying LLM and routes special requests to **tools** via simple logic or LLM output in JSON.  
Each tool handles a specific type of task like math or reminders.

The interaction is done through the terminal using:

```bash
python app.py
