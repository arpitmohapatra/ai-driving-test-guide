import os
from dotenv import load_dotenv
from utils.rag import RAGQuestionAnswerer

# Load environment variables
load_dotenv()

def main():
    print("Starting document ingestion process...")
    
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set")
        print("Please create a .env file with your OpenAI API key")
        return False
    
    # Initialize RAG system
    rag = RAGQuestionAnswerer()
    
    # Check if data directory exists and has PDFs
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"Created data directory at {data_dir}")
        print(f"Please add PDF files to the {data_dir} directory and run this script again")
        return False
    
    pdf_files = [f for f in os.listdir(data_dir) if f.endswith('.pdf')]
    if not pdf_files:
        print(f"No PDF files found in {data_dir} directory")
        print(f"Please add PDF files to the {data_dir} directory and run this script again")
        return False
    
    print(f"Found {len(pdf_files)} PDF files in {data_dir} directory")
    
    # Ingest documents
    success = rag.ingest_documents()
    
    if success:
        print("Document ingestion completed successfully!")
        print("You can now run the Flask app to ask questions about the ingested documents")
    else:
        print("Document ingestion failed")
    
    return success

if __name__ == "__main__":
    main()