## AI Sales Assistant (RAG-based)

An end-to-end Retrieval-Augmented Generation (RAG) AI application that allows users to upload documents and ask contextual questions using Large Language Models.

🔗 Live App: https://ai-sales-assistant-wp8oavwsq5sjavwxkeutrq.streamlit.app/
🔗 GitHub Repo: https://github.com/anilkotian59-DS/ai-sales-assistant

## Project Overview:

This project demonstrates a production-style implementation of a multi-document RAG pipeline using modern LLM tooling.
Users can:
- Upload multiple PDF documents
- Ask questions in a chat interface
- Receive context-aware answers grounded in document content

## RAG improves accuracy by retrieving relevant context before generating responses, reducing hallucinations

## Architecture

User Query

    ↓
    

Streamlit UI (Chat Interface)

    ↓
    
Document Loader (PDF)

    ↓
    
Text Chunking

    ↓
    
Embeddings (HuggingFace)

    ↓
    
Vector Database (FAISS)

    ↓
    
Retriever (Similarity Search)

    ↓
    
LLM (Groq - LLaMA 3.1)

    ↓
    
Final Answer

## 🛠️ Tech Stack

Frontend/UI: Streamlit
LLM: Groq (LLaMA 3.1)
Framework: LangChain
Embeddings: HuggingFace
Vector DB: FAISS
Deployment: Streamlit Cloud

## ⚙️ Features
- Multi-document PDF upload
- ChatGPT-style interface
- Context-aware answers (RAG)
- Fast inference via Groq
- Secure API handling (Streamlit secrets)
- Business Use Case
- Sales document analysis
- Resume screening
- Knowledge base Q&A

## Similar RAG assistants are used in real systems to extract insights from business data and customer interactions

## Run Locally
- git clone https://github.com/anilkotian59-DS/ai-sales-assistant.git
- cd ai-sales-assistant
- pip install -r requirements.txt
- streamlit run app.py

## 👤 Author
Anil Kotian
AI + Analytics + Business Background
