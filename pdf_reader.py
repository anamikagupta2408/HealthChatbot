from pypdf import PdfReader

# Step 1: Open the PDF
reader = PdfReader("data/medical_documents/sample.pdf")

# Step 2: Count the pages
print("Total pages:", len(reader.pages))

# Step 3: Extract text from all pages
for page_number, page in enumerate(reader.pages, start=1):

    text = page.extract_text()

    print(f"\n----- Page {page_number} -----")

    if text:
        print(text)
    else:
        print("No extractable text found on this page.")