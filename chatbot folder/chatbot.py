def chatbot():
    print("Chatbot: Hello! I'm ChatBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot, your virtual assistant.")

        elif "help" in user_input:
            print("Chatbot: Sure! I can answer simple questions like greetings, name, time, and date.")

        elif "time" in user_input:
            from datetime import datetime
            print("Chatbot: The current time is", datetime.now().strftime("%H:%M:%S"))

        elif "date" in user_input:
            from datetime import datetime
            print("Chatbot: Today's date is", datetime.now().strftime("%Y-%m-%d"))

        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        else:
            print("Chatbot: I'm not sure how to respond to that. Can you ask something else?")

# Run the chatbot
chatbot()