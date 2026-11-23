from langchain_huggingface import HuggingFaceEmbeddings

# Step 1: Load the embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 2: Create sample sentences
sentences = [
    "Diabetes affects blood sugar levels.",
    "Insulin helps regulate glucose in the body.",
    "The weather is pleasant today."
]

# Step 3: Convert sentences into vectors
vectors = embeddings.embed_documents(sentences)

# Step 4: Display the vectors
for i, vector in enumerate(vectors, start=1):

    print(f"\nSentence {i}: {sentences[i-1]}")

    print("Vector dimensions:", len(vector))

    print("First 5 vector values:", vector[:5])