import re
from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Step 1: Load PDF
pdf_path = "data/medical_documents/sample.pdf"

reader = PdfReader(pdf_path)

documents = []

# Step 2: Extract text page by page
for page_number, page in enumerate(reader.pages, start=1):

    text = page.extract_text()

    if text:

        # Clean text
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n+", "\n", text)
        text = text.strip()

        # Store text with metadata
        document = Document(
            page_content=text,
            metadata={
                "source": pdf_path,
                "page": page_number
            }
        )

        documents.append(document)


print("PDF extraction completed!")
print("Total pages with text:", len(documents))


# Step 3: Split documents into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print("Total chunks:", len(chunks))


# Step 4: Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Step 5: Create FAISS database
vector_store = FAISS.from_documents(
    chunks,
    embeddings,
    distance_strategy="COSINE"
)

# Step 6: Save database
vector_store.save_local("vectorstore")

print("FAISS database saved with page metadata!")