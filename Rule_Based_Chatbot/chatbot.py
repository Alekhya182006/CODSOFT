def chatbot(input):
    input = input.lower()

    if input == "hi" or input == "hello":
        return "Hello! How can I help you?"

    elif "your name" in input:
        return "I am a simple rule-based chatbot."

    elif "how are you" in input:
        return "I'm doing good! Thanks for asking."

    elif "help" in input:
        return "Sure! Tell me what you need help with."

    elif "bye" in input or "exit" in input:
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I didn't understand that."


print("Chatbot: Hello! Type 'bye' to end the conversation.")

while True:
    user = input("You: ")
    response = chatbot(user)
    print("Chatbot:", response)

    if "bye" in user.lower() or "exit" in user.lower():
        break
