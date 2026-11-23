import json
import os

# Step 1: Define the history file
HISTORY_FILE = "chat_history.json"


# Step 2: Load previous conversation
def load_history():

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r") as file:
            history = json.load(file)

        print("Previous conversation loaded!")

        return history

    return []


# Step 3: Save conversation
def save_history(history):

    with open(HISTORY_FILE, "w") as file:

        json.dump(history, file, indent=4)

    print("Conversation saved successfully!")


# Step 4: Load existing history
chat_history = load_history()


# Step 5: Start conversation
while True:

    question = input("\nYou: ")

    if question.lower() == "exit":

        save_history(chat_history)

        print("Goodbye!")
        break

    # Store user message
    chat_history.append({
        "role": "user",
        "content": question
    })

    answer = input("Chatbot: ")

    # Store chatbot response
    chat_history.append({
        "role": "assistant",
        "content": answer
    })

    # Save updated history
    save_history(chat_history)