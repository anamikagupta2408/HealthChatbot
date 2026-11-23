from dotenv import load_dotenv
from google import genai
import os

# Step 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Step 2: Connect to Gemini
client = genai.Client(api_key=api_key)

# Step 3: Create conversation history
chat_history = []

print("Medical Chatbot Started!")
print("Type 'exit' to stop.\n")

# Step 4: Start conversation
while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    # Step 5: Convert previous messages into text
    history_text = ""

    for message in chat_history:
        history_text += (
            message["role"] + ": " +
            message["content"] + "\n"
        )

    # Step 6: Create prompt
    prompt = f"""
    You are a helpful medical information assistant.

    Previous Conversation:
    {history_text}

    Current User Question:
    {question}

    Answer in simple language.
    Use previous conversation to understand
    follow-up questions.

    Do not diagnose diseases or prescribe medicines.
    Recommend consulting a qualified healthcare
    professional for personal medical advice.
    """

    # Step 7: Generate Gemini response
    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    answer = response.text

    print("\nChatbot:", answer)

    # Step 8: Save user question
    chat_history.append({
        "role": "user",
        "content": question
    })

    # Step 9: Save Gemini response
    chat_history.append({
        "role": "assistant",
        "content": answer
    })

    print("\nConversation messages stored:",
          len(chat_history))