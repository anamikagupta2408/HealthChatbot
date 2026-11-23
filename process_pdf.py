from pypdf import PdfReader
from text_cleaner import clean_text

# Open PDF
reader = PdfReader("data/medical_documents/sample.pdf")

# Store extracted text
full_text = ""

# Extract text from every page
for page in reader.pages:

    text = page.extract_text()

    if text:
        full_text += text + "\n"

# Clean extracted text
cleaned_text = clean_text(full_text)

# Display results
print("Original text length:", len(full_text))
print("Cleaned text length:", len(cleaned_text))

print("\nCleaned Medical Text:\n")
print(cleaned_text)