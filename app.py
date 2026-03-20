import streamlit as st
from utils import load_and_process_pdf, create_vector_store, ask_question

st.set_page_config(page_title="AI Sales Assistant", layout="wide")

st.title("🤖 AI Sales Assistant (Advanced)")

# ---------------- Sidebar ----------------
st.sidebar.title("⚙️ Controls")

groq_api_key = st.secrets["GROQ_API_KEY"]

uploaded_files = st.sidebar.file_uploader(
    "Upload PDFs", type="pdf", accept_multiple_files=True
)

if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.success("Chat cleared!")

# ---------------- Session State ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# ---------------- Process Files ----------------
if uploaded_files and groq_api_key:
    with st.spinner("Processing documents..."):
        all_chunks = []

        for file in uploaded_files:
            file_path = f"data/{file.name}"
            with open(file_path, "wb") as f:
                f.write(file.read())

            chunks = load_and_process_pdf(file_path)
            all_chunks.extend(chunks)

        st.session_state.vectorstore = create_vector_store(all_chunks)

    st.success("✅ All documents processed! Start chatting.")

# ---------------- Chat Display ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- Chat Input ----------------
if prompt := st.chat_input("Ask something about your documents..."):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    if st.session_state.vectorstore and groq_api_key:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = ask_question(
                    st.session_state.vectorstore,
                    prompt,
                    groq_api_key,
                    st.session_state.messages
                )
                st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )
    else:
        st.warning("⚠️ Please upload documents and enter API key.")