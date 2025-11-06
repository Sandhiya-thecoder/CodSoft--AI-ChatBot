# CodSoft--AI-ChatBot

<h1 align="center">🤖 ChatBuddy — Simple Python Chatbot</h1>

<p align="center">
A beginner-friendly, rule-based chatbot built in Python using <b>if–else logic</b> and <b>pattern matching</b> 💬  
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Type-Rule--Based%20Chatbot-brightgreen" alt="Chatbot Type">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Project Status">
</p>

---

## 📘 Overview
**ChatBuddy** is a lightweight chatbot built using Python’s `if–elif–else` statements.  
It responds to greetings, small talk, and basic queries like **time** or **weather**, while maintaining a friendly conversational tone.  

This project is perfect for beginners learning Python and the basics of chatbot logic.

---

## 🧠 How It Works
1. Converts user input to lowercase for consistent comparison.  
2. Matches text patterns using `if–elif–else` conditions.  
3. Returns pre-defined responses for recognized phrases.  
4. Replies with a fallback message if the input isn’t understood.  

---

## 💻 Features
- 🗣️ Responds to greetings and casual conversation  
- ⏰ Displays the current time  
- ☀️ Talks about the weather (mock response)  
- 🤖 Introduces itself as “ChatBuddy”  
- 🚪 Gracefully exits on “bye”, “exit”, or “quit”  
- ⚡ Runs entirely on core Python (no external libraries)  

---

## 🧩 Technologies Used
- **Language:** Python 3.x  
- **Module:** `datetime` (for showing current time)  
- **IDE/Editor:** Any Python-supported IDE (VS Code, PyCharm, IDLE, etc.)

---

## 📜 Code Example
```python
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! 😊 How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a bot, but I’m doing great! How about you?"

    elif "i am fine" in user_input:
        return "That's great to hear! 😊 What can I assist you with today?"

    elif "your name" in user_input:
        return "I’m ChatBuddy 🤖 — your friendly Python chatbot!"

    elif "what can you do" in user_input:
        return "I can chat with you, answer simple questions, and keep you company! 😊"

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time} ⏰"

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! 👋 Have a great day ahead!"

    else:
        return "Hmm, I'm not sure I understand that. Could you try rephrasing?"
