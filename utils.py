from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_groq import ChatGroq


def load_and_process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = text_splitter.split_documents(documents)
    return chunks


def create_vector_store(chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore


def ask_question(vectorstore, query, api_key, chat_history):
    retriever = vectorstore.as_retriever()

    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    # Combine chat history
    history_text = "\n".join(
        [f"{msg['role']}: {msg['content']}" for msg in chat_history[-5:]]
    )

    llm = ChatGroq(
        api_key=api_key,
        model_name="llama-3.1-8b-instant"
    )

    prompt = f"""
    You are an AI assistant helping analyze documents professionally.

    Use the context and chat history to answer.

    Chat History:
    {history_text}

    Context:
    {context}

    Instructions:
    - Be clear and structured
    - Use bullet points if needed
    - Keep answer relevant to document

    Question:
    {query}
    """

    response = llm.invoke(prompt)

    return response.content