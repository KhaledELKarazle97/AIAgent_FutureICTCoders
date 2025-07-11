import os
from dotenv import load_dotenv
import requests
import json
from groq import Groq
from tools import use_tool
load_dotenv()

# Set your Groq API key here or via environment variable. Can get an API key from  https://groq.com/
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

# Basic memory for reminders
memory = {
    "reminders": []
}

# === Tool Mapper. Can add more tools to tools/use_tool.py file ===
TOOLS = {
    "math": use_tool.math_tool,
    "reminder": use_tool.reminder_tool,
    "fun_fact": use_tool.fun_fact_tool,  # 🔧 This was missing
}


# === Groq API Call ===
def call_groq(system_prompt, user_message):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message},
    ]

    # Call Groq (using OpenAI-compatible SDK)
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct", # I like Llama but you can try other models. THEY ALL FREE!😍😍
        messages=messages,
        temperature=0.4,
        top_p=0.8,
        max_tokens=600,  # NOTE: use `max_tokens`, not `max_completion_tokens`
        stream=False      # Set to True only if you're handling a stream properly
    )

    return completion.choices[0].message.content

# === Main Conversational Agent ===
def main():
    print("🧠 AI Agent is ready! Type 'exit' to quit.\n")
    system_prompt = (
        "You are a smart assistant for Malaysian school children. "
        "You can use these tools to help with tasks:\n\n"
        "Tools:\n"
        "- math: for simple calculations (e.g., 'What is 12 + 5?')\n"
        "- reminder: to set reminders (e.g., 'Remind me to drink water at 3pm')\n"
        "- fun_fact: to share a random Malaysia-themed fact\n\n"
        "If the user wants to use a tool, reply ONLY in this JSON format:\n"
        "{ \"use_tool\": \"tool_name\", \"query\": \"what the user asked\" }\n\n"
        "Otherwise, respond normally like a friendly AI assistant."
    )

    while True:
        user_input = input("You: ")

        if user_input.strip().lower() == "exit":
            print("👋 Bye Bye!")
            break

        ai_response = call_groq(system_prompt, user_input)

        # Try parsing as JSON (tool call)
        try:
            tool_signal = json.loads(ai_response)

            if isinstance(tool_signal, dict) and "use_tool" in tool_signal:
                tool_name = tool_signal["use_tool"]
                query = tool_signal["query"]
                if tool_name in TOOLS:
                    tool_result = TOOLS[tool_name](query)
                    print(f"[Tool - {tool_name}] {tool_result}")
                else:
                    print(f"🤖 The tool '{tool_name}' is not available.")
            else:
                print(f"AI: {ai_response}")

        except json.JSONDecodeError:
            # If response is not JSON, just print it as normal text
            print(f"AI: {ai_response}")

if __name__ == "__main__":
    main()
