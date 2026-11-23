from langchain_text_splitters import RecursiveCharacterTextSplitter

# Sample medical text
text = """
Diabetes is a chronic health condition.

It affects how the body processes blood glucose.

Insulin is a hormone produced by the pancreas.

Type 1 diabetes occurs when the immune system
attacks insulin-producing cells.

Type 2 diabetes occurs when the body becomes
resistant to insulin.
"""

# Create a text splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

# Divide text into chunks
chunks = splitter.split_text(text)

# Display chunks
print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"\n----- Chunk {i} -----")
    print(chunk)