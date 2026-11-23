import re

def clean_text(text):

    # Remove extra spaces and tabs
    text = re.sub(r'[ \t]+', ' ', text)

    # Remove unnecessary blank lines
    text = re.sub(r'\n+', '\n', text)

    # Remove spaces at the beginning and end
    text = text.strip()

    return text


# Sample text
sample_text = """
DIABETES


Diabetes    is a chronic health condition.


It affects how the body processes glucose.


"""

cleaned_text = clean_text(sample_text)

print("Original Text:")
print(sample_text)

print("\nCleaned Text:")
print(cleaned_text)