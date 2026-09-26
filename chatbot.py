print("=" * 50)
print("             BASIC PYTHON CHATBOT")
print("=" * 50)
print("Created by: Mohd Monis")
print("Python Internship Project")
print("=" * 50)

print("\nHello Monis! I am your basic chatbot.")
print("You can talk to me using simple messages.")
print("Type 'bye' whenever you want to exit.\n")

while True:
    user = input("You: ").strip().lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm fine, thank you! How are you?")

    elif user in ["what is your name", "your name"]:
        print("Bot: My name is Basic Python Chatbot.")

    elif user in ["who created you", "who made you"]:
        print("Bot: I was created by Mohd Monis using Python.")

    elif user in ["what can you do", "help"]:
        print("Bot: I can respond to some basic questions and greetings.")

    elif user in ["what is python", "python"]:
        print("Bot: Python is a popular programming language.")

    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome! I'm happy to help.")

    elif user in ["good morning", "morning"]:
        print("Bot: Good morning! Have a great day.")

    elif user in ["good night", "night"]:
        print("Bot: Good night! Take care.")

    elif user == "bye":
        print("\nBot: Goodbye, Mohd Monis!")
        print("Bot: Thank you for chatting with me.")
        print("=" * 50)
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Try saying hello, asking my name, or typing help.")