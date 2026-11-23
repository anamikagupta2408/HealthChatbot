chat_history = []

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    chat_history.append({
        "role": "user",
        "content": question
    })

    print("\nChat History:")

    for message in chat_history:
        print(message["role"], ":", message["content"])