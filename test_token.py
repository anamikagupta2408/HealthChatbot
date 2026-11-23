from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env", override=True)

HF_TOKEN = os.getenv("HF_TOKEN")

if HF_TOKEN:
    print("Hugging Face token loaded successfully!")
else:
    print("Token not found. Check your .env file.")