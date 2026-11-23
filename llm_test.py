from dotenv import load_dotenv
from google import genai
import os

print("Starting Gemini test...")

load_dotenv(override=True)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")

print("API key loaded!")

client = genai.Client(api_key=api_key)

print("Sending request to Gemini...")

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain diabetes in simple words."
)

print("\nGemini response:")
print(response.text)

print("\nTest completed!")