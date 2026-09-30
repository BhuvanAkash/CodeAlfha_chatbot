from datetime import datetime

def chatbot(user_input):
    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi! How can I help you?"

    elif "how are you" in user_input:
        return "I'm fine! Thanks for asking."

    elif "your name" in user_input:
        return "I'm a simple Python chatbot."

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        return "The current time is " + current_time

    elif "help" in user_input:
        return "You can ask me about my name, the time, or say hello!"

    elif "thanks" in user_input or "thank you" in user_input:
        return "You're welcome!"

    elif user_input == "bye" or user_input == "exit":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."


print("Bot: Hello! I'm your chatbot.")
print("Bot: Type 'help' to see what I can do.")

while True:
    user_input = input("You: ")

    response = chatbot(user_input)
    print("Bot:", response)

    if user_input.lower() == "bye" or user_input.lower() == "exit":
        break