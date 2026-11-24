# 🏥 HealthChatbot – Medical RAG Chatbot

An AI-powered medical information chatbot built using Retrieval-Augmented Generation (RAG), FAISS, Hugging Face embeddings, and Google's Gemini API.

## 📌 About the Project

HealthChatbot is an educational project designed to answer medical information questions using content retrieved from medical PDF documents.

It combines document retrieval with a Large Language Model (LLM) to generate context-based responses.

## 🎯 Project Objectives

- Understand Retrieval-Augmented Generation (RAG).
- Process and extract information from medical PDF documents.
- Generate embeddings using Hugging Face.
- Store and retrieve document embeddings using FAISS.
- Generate responses using Google's Gemini API.
- Maintain conversational history.

## 🛠️ Technologies Used

- Python
- LangChain
- Hugging Face
- Sentence Transformers
- FAISS
- Google Gemini API
- PyPDF
- Streamlit (planned frontend)

## ⚙️ Project Architecture

Medical PDF Documents  
↓  
Text Extraction  
↓  
Text Cleaning and Chunking  
↓  
Hugging Face Embeddings  
↓  
FAISS Vector Database  
↓  
User Question  
↓  
Relevant Document Retrieval  
↓  
Gemini LLM  
↓  
Context-Based Answer

## 📂 Project Structure

```text
HealthChatbot/
│
├── data/
│   └── medical_documents/
│
├── app.py
├── ingest.py
├── retrieval.py
├── rag.py
├── rag_chat.py
├── rag_chat_persistent.py
├── chat_memory.py
├── chat_memory_gemini.py
├── chat_storage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/anamikagupta2408/HealthChatbot.git
```

### 2. Navigate to the project

```bash
cd HealthChatbot
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Gemini API

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Never share your API key publicly.

### 7. Add medical documents

Place your permitted medical PDF documents inside:

```text
data/medical_documents/
```

### 8. Build the vector database

```bash
python ingest.py
```

### 9. Run the chatbot

```bash
python rag.py
```

## 🔮 Future Improvements

- Streamlit-based interactive interface.
- Multiple PDF document support.
- Improved retrieval accuracy.
- Better conversational memory.
- Chat history management.
- Testing and evaluation.
- Cloud deployment.

## ⚠️ Disclaimer

This project is intended for educational and informational purposes only.

It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns.

