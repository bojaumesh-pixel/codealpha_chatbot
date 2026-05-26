def chatbot():
    print("Hello! I'm a simple chatbot")
    while True:
        USER_input = input("YOU: ").lower()
        if USER_input == "hello":
            print("CHATBOT: Hi!")
        elif USER_input == "how are you":
            print("CHATBOT: I'm fine, thanks!")
        elif USER_input == "bye":
            print("CHATBOT: Goodbye!")
            break
        else:
            print("CHATBOT:Sorry, I don't understand.")
#Run the chatbot
chatbot() 