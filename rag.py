from dotenv import load_dotenv
from google import genai
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

# Step 1: Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

# Step 2: Connect to Gemini
client = genai.Client(api_key=api_key)

# Step 3: Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 4: Load FAISS database
vector_store = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("Medical database loaded successfully!")

# Step 5: Get user's question
question = input("\nAsk your medical question: ")

# Step 6: Retrieve documents with relevance scores
# Step 6: Retrieve documents using MMR
results = vector_store.max_marginal_relevance_search(
    question,
    k=3,
    fetch_k=10,
    lambda_mult=0.5
)

print("\nRetrieved Documents:")

for i, document in enumerate(results, start=1):
    print(f"\nDocument {i}:")
    print("Content:", document.page_content[:150])

# Step 7: Filter irrelevant documents


# Step 8: Extract context
context = "\n\n".join(
    [document.page_content for document in results]
)

# Step 9: Create prompt
prompt = f"""
You are a responsible medical information assistant.

Your task is to answer the user's question using
the medical context provided below.

FOLLOW THESE RULES:

1. Use only the information provided in the
   medical context.

2. Explain the answer in simple, clear language.

3. Organize the answer using bullet points
   wherever appropriate.

4. Do not invent facts or add unsupported
   medical information.

5. If the context does not contain enough
   information, clearly say:
   "The provided medical documents do not
   contain enough information to answer this
   question."

6. Do not diagnose diseases or prescribe
   medicines.

7. For personal medical concerns, recommend
   consulting a qualified healthcare professional.

MEDICAL CONTEXT:
{context}

USER QUESTION:
{question}

YOUR ANSWER:
"""

# Step 10: Generate answer using Gemini
try:
    response=client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )
    if response.text:
        print("\nChatbot Answer:")
        print(response.text)
    else:
        print("\nSorry,I could not generate an answer.")
except Exception as e:
    print("\nSomething went wrong while generating the answer.")
    print("Error:",e)