from dotenv import load_dotenv
from google import genai
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Step 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

client = genai.Client(api_key=api_key)


# Step 2: Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Step 3: Load FAISS database
vector_store = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Medical database loaded successfully!")


# Step 4: Create conversation history
chat_history = []

print("\nMedical Chatbot Started!")
print("Type 'exit' to stop.\n")


# Step 5: Start conversation
while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Chatbot: Goodbye!")
        break


    # Step 6: Prepare conversation history
    history_text = ""

    for message in chat_history:
        history_text += (
            message["role"] + ": " +
            message["content"] + "\n"
        )


    # Step 7: Understand the current question
    rewrite_prompt = f"""
    You are a question understanding assistant.

    Previous conversation:
    {history_text}

    Current question:
    {question}

    Rewrite the current question as a standalone
    question that can be searched in medical documents.

    Use previous conversation only when necessary
    to understand references such as "it", "its",
    "they", or "those".

    Do not answer the question.
    Return only the rewritten question.
    """

    rewrite_response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=rewrite_prompt
    )

    search_query = rewrite_response.text.strip()

    print("\nSearch Query:", search_query)


    # Step 8: Retrieve medical documents
    results = vector_store.similarity_search(
        search_query,
        k=3
    )

    context = "\n\n".join(
        [document.page_content for document in results]
    )


    # Step 9: Generate final answer
    prompt = f"""
    You are a responsible medical information assistant.

    Previous conversation:
    {history_text}

    Medical context:
    {context}

    User's current question:
    {question}

    Instructions:

    1. Answer using only the provided medical context.
    2. Use simple and clear language.
    3. Do not invent medical facts.
    4. If the context is insufficient, say so.
    5. Do not diagnose diseases or prescribe medicines.
    6. For personal medical concerns, recommend
       consulting a qualified healthcare professional.

    Answer:
    """

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    answer = response.text

    print("\nChatbot:", answer)


    # Step 10: Save conversation
    chat_history.append({
        "role": "user",
        "content": question
    })

    chat_history.append({
        "role": "assistant",
        "content": answer
    })


    # Step 11: Display document sources
    print("\nSources:")

    for i, document in enumerate(results, start=1):

        source = document.metadata.get("source", "Unknown")
        page = document.metadata.get("page", "Unknown")

        print(f"{i}. {source} - Page {page}")