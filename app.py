from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Your PDF", page_icon="🗂️")
    st.title("Ask Your PDF 💬")

    # Upload the file
    pdf = st.file_uploader("Upload your PDF", type=["pdf"])

    # Extract text from the uploaded file
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
        # Create chunks
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(text)

        # Create the embeddings
        embeddings = OpenAIEmbeddings(chunks)

        # Build the vector store
        knowledge_base = FAISS.from_texts(chunks, embeddings)


if __name__ == '__main__':
    main()
