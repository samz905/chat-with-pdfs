from dotenv import load_dotenv
import streamlit as st

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Your PDF", page_icon="🗂️")
    st.title("Ask Your PDF 💬")

    st.file_uploader("Upload your PDF", type=["pdf"])

if __name__ == '__main__':
    main()
