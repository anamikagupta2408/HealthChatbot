from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store=FAISS.load_local("vectorstore",embeddings,allow_dangerous_deserialization=True)

print("Vector database loaded successfully!")

query=input("\nAsk a medical question:")

results = vector_store.similarity_search(query,k=3) 

print("\nRelevant information found:\n")

for i,document in enumerate(results,start=1):
    print(f"---- Result {i} ---")
    print(document.page_content)    
    print()