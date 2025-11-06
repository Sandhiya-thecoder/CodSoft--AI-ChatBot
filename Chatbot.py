# Simple Chatbot using if-else and pattern matching

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for easier matching

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello there! 😊 How can I help you today?"

    elif "how are you" in user_input:
        return "I'm just a bot, but I’m doing great! How about you?"

    elif "I am fine" in user_input:
        return "That's great to hear! 😊 What can I assist you with today?"

    elif "your name" in user_input:
        return "I’m ChatBuddy 🤖 — your friendly Python chatbot!"
    
    elif "what is your name ?" in user_input:
        return "You have a nice name! 😊"
    
    elif "what can you do" in user_input:
        return "I can chat with you, answer simple questions, and keep you company! 😊"

    # Help or guidance
    elif "help" in user_input:
        return "Sure! I can help you with general queries. Try asking me about time, weather, or greetings."

    # Simple Q&A
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time} ⏰"

    elif "weather" in user_input:
        return "I can't check the weather right now, but I hope it's sunny wherever you are! ☀️"

    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        return "Goodbye! 👋 Have a great day ahead!"

    # Default fallback
    else:
        return "Hmm, I'm not sure I understand that. Could you try rephrasing?"

# Main chat loop
print("🤖 ChatBuddy: Hello! I'm your simple chatbot. Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("ChatBuddy:", response)

    if "bye" in user_input.lower() or "exit" in user_input.lower() or "quit" in user_input.lower():
        break
