import random
import re

def math_tool(query: str):
    try:
        # Extract simple math expression
        expression = re.findall(r"[0-9+\-*/(). ]+", query)
        if expression:
            result = eval(expression[0])
            return f"The answer to {expression[0]} is {result} 🎉"
        else:
            return "Hmm, I couldn't find a math question in what you said. Try something like 'What is 12 + 4?'"
    except Exception as e:
        return f"Oops! I couldn't solve that math question: {e}"

def reminder_tool(query: str):
    reminder_text = query.replace("remind me", "", 1).strip()
    memory["reminders"].append(reminder_text)
    return f"Got it! I'll remember: '{reminder_text}' 📌"

def fun_fact_tool(_):
    facts = [
        "Did you know? Mount Kinabalu is the highest mountain in Malaysia! 🏔️",
        "The Malaysian flag is called the Jalur Gemilang 🇲🇾",
        "Durian is known as the 'King of Fruits' in Malaysia! 😄",
        "Roti canai is a popular Malaysian food that came from India 🍽️",
        "The Petronas Twin Towers in Kuala Lumpur were once the tallest buildings in the world! 🏙️"
    ]
    return random.choice(facts)