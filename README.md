# AI Driving Test Guide

A RAG (Retrieval-Augmented Generation) chatbot application that answers questions about driving tests based on PDF knowledge.

## Features

- PDF document ingestion and processing
- Vector database for efficient retrieval
- AI-powered question answering using RAG technique
- Simple web interface for asking questions

## Installation

1. Clone this repository:
```bash
git clone https://github.com/arpitmohapatra/ai-driving-test-guide.git
cd ai-driving-test-guide
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Create a `.env` file with your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Place your driving test PDF document in the `data` folder.

2. Ingest the PDF into the vector database:
```bash
python ingest.py --file data/your_driving_manual.pdf
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
.
├── app.py              # Main Flask application
├── ingest.py           # Script for ingesting PDFs into the vector database
├── requirements.txt    # Project dependencies
├── .env                # Environment variables (create this file, not tracked in git)
├── .gitignore          # Gitignore file
├── data/               # Folder for storing PDF documents
├── static/             # Static files for the web interface
│   ├── css/
│   └── js/
├── templates/          # HTML templates
└── utils/              # Utility functions
    ├── __init__.py
    ├── embedding.py    # Functions for creating and managing embeddings
    ├── pdf_loader.py   # Functions for loading and processing PDFs
    └── rag.py          # RAG implementation for question answering
```

## Technologies Used

- Python
- OpenAI API
- LangChain
- FAISS for vector storage
- PyPDF2 for PDF processing
- Flask for the web interface

## License

MIT