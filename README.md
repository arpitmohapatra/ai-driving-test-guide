# AI Driving Test Guide

An AI-powered application to help users prepare for driving tests using RAG (Retrieval Augmented Generation) technology. This application allows users to upload driving test guides and regulations in PDF format and then ask questions about them.

## Features

- Upload driving test manuals and regulations as PDF files
- Process and index document content using vector embeddings
- Ask natural language questions about driving tests and regulations
- Get AI-generated answers based on the uploaded documents
- Web interface for easy interaction

## Technology Stack

- **Backend**: Python, Flask
- **AI/ML**: LangChain, OpenAI API, FAISS vector database
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Document Processing**: PyPDF2

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/arpitmohapatra/ai-driving-test-guide.git
   cd ai-driving-test-guide
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:
   ```
   cp .env.example .env
   ```
   Edit the `.env` file and add your OpenAI API key.

## Usage

### 1. Add Documents

Place your driving test guide PDF documents in the `data/` directory:
```
mkdir -p data
# Copy your PDF files to the data directory
```

### 2. Ingest Documents

Process and index the documents:
```
python ingest.py
```

### 3. Run the Web Application

Start the Flask web server:
```
python app.py
```

Access the application in your web browser at `http://localhost:5000`.

### 4. Ask Questions

- Use the web interface to ask questions about driving tests and regulations
- The AI will retrieve relevant information from your documents and generate answers

## Project Structure

```
ai-driving-test-guide/
├── app.py                 # Main Flask application
├── ingest.py              # Document ingestion script
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore file
├── README.md              # Project documentation
├── data/                  # Directory for PDF documents
├── templates/             # HTML templates
│   └── index.html         # Main web interface
├── utils/                 # Utility modules
│   └── rag.py             # RAG implementation
└── vector_store/          # FAISS vector database (generated)
```

## Customization

- Adjust chunk size and overlap in `utils/rag.py` for different document types
- Modify the UI in `templates/index.html` to change the look and feel
- Add additional routes in `app.py` for more functionality

## Troubleshooting

- If you encounter an error related to the OpenAI API key, make sure it's correctly set in your `.env` file
- If document ingestion fails, check that your PDF files are in the correct format and readable
- For vector storage issues, try deleting the `vector_store` directory and re-running the ingestion process

## License

This project is open source and available under the MIT License.

## Acknowledgements

- OpenAI for providing the API for embeddings and completions
- LangChain for the RAG framework
- FAISS for efficient vector similarity search