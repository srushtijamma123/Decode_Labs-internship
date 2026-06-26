print("🤖 AI Chatbot Started!")
print("Type 'bye' to exit.\n")

responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! How can I help you?",
    "how are you": "I am doing great!",
    "Who are you":"I am a Rule-Based AI Chatbot.",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "good morning": "Good Morning! ☀️",
    "good night": "Good Night! 🌙",
    "thanks": "You're welcome!",
    "who created you": "I was created by Srushti.",
    "what is ai": "AI means Artificial Intelligence.",
    "favorite color": "I like blue.",
    "bye": "Goodbye! Have a nice day!",
}

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    reply = responses.get(
        user_input,
        "Sorry, I don't understand that."
    )

    print("Bot:", reply)