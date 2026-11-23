from dotenv import load_dotenv
from google import genai
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

import os
import json


# STEP 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

client = genai.Client(api_key=api_key)


# STEP 2: Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# STEP 3: Load FAISS database
vector_store = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Medical database loaded successfully!")


# STEP 4: Define JSON history file
HISTORY_FILE = "chat_history.json"


# STEP 5: Load previous conversation
def load_history():

    if os.path.exists(HISTORY_FILE):

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


# STEP 6: Save conversation
def save_history(history):

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:

        json.dump(history, file, indent=4)


# STEP 7: Load existing history
chat_history = load_history()

print("\nMedical Chatbot Started!")

if chat_history:
    print("Previous conversation loaded!")
else:
    print("Starting a new conversation!")

print("Type 'exit' to stop.")


# STEP 8: Start chatbot
while True:

    question = input("\nYou: ")

    if question.strip().lower() == "exit":
        print("Chatbot: Goodbye!")
        break


    # STEP 9: Prepare conversation history
    history_text = ""

    for message in chat_history:

        history_text += (
            message["role"] + ": " +
            message["content"] + "\n"
        )


    # STEP 10: Rewrite follow-up question
    rewrite_prompt = f"""
    You are a question understanding assistant.

    Previous conversation:
    {history_text}

    Current question:
    {question}

    Rewrite the current question as a standalone
    question suitable for searching medical documents.

    Use previous conversation when necessary.

    Do not answer the question.
    Return only the rewritten question.
    """

    rewrite_response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=rewrite_prompt
    )

    search_query = rewrite_response.text.strip()

    print("\nSearch Query:", search_query)


    # STEP 11: Retrieve medical information
    results = vector_store.similarity_search(
        search_query,
        k=3
    )

    context = "\n\n".join(
        [document.page_content for document in results]
    )


    # STEP 12: Generate final answer
    prompt = f"""
    You are a responsible medical information assistant.

    Previous conversation:
    {history_text}

    Medical context:
    {context}

    Current user question:
    {question}

    Instructions:

    1. Answer using only the provided medical context.
    2. Use simple and clear language.
    3. Do not invent medical facts.
    4. If the context is insufficient, say so.
    5. Do not diagnose diseases or prescribe medicines.
    6. Recommend consulting a qualified healthcare
       professional for personal medical advice.

    Answer:
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    answer = response.text

    print("\nChatbot:", answer)


    # STEP 13: Store conversation
    chat_history.append({
        "role": "user",
        "content": question
    })

    chat_history.append({
        "role": "assistant",
        "content": answer
    })


    # STEP 14: Save conversation to JSON
    save_history(chat_history)

    print("\nConversation saved successfully!")


    # STEP 15: Display sources
    print("\nSources:")

    for i, document in enumerate(results, start=1):

        source = document.metadata.get("source", "Unknown")
        page = document.metadata.get("page", "Unknown")

        print(f"{i}. {source} - Page {page}")