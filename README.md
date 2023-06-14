# Ask Your PDF

Ask Your PDF is a simple application that allows you to upload a PDF and ask questions about its content. It uses the OpenAI API to understand your questions and find the answers in the text of the PDF.

## Features

- **PDF Upload**: You can upload a PDF file to the application.
- **Text Extraction**: The application extracts the text from the uploaded PDF.
- **Question Answering**: You can ask questions about the content of the PDF, and the application will find the answers in the text.

## Usage

When you run the application, you will see an interface where you can upload a PDF file. After uploading the file, you can enter a question in the text input field. The application will then search the text of the PDF for the answer to your question and display the answer.

## Dependencies

The application depends on several Python libraries, including:

- `python-dotenv` for loading environment variables.
- `streamlit` for creating the application interface.
- `PyPDF2` for reading PDF files.
- `langchain` for text splitting, embeddings, vector stores, and question answering.

Please see the `requirements.txt` file for the exact versions of these dependencies.

## Installation

To install the application, first clone this repository:

```bash
git clone https://github.com/samz905/chat-with-pdfs.git
```

Then, navigate to the project directory and install the dependencies:

```bash
cd ask-your-pdf
pip install -r requirements.txt
```

Finally, run the application:

```bash
streamlit run main.py
```

## License

This project is licensed under the terms of the MIT license.
