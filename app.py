from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback


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
        embeddings = OpenAIEmbeddings()

        # Build the vector store
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Chat functionality
        user_input = st.text_input("Ask a question about your PDF:")
        if user_input:
            docs = knowledge_base.similarity_search(user_input)

            chain = load_qa_chain(OpenAI(), chain_type="stuff")

            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_input)
                print(cb)

            st.write(response)


if __name__ == '__main__':
    main()
