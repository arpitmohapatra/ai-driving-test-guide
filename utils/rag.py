import os
import faiss
import numpy as np
from typing import List, Dict, Any
from PyPDF2 import PdfReader
from tqdm import tqdm
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores.base import VectorStore
from langchain.schema import Document
from langchain.chat_models import ChatOpenAI

class RAGQuestionAnswerer:
    def __init__(self, vector_store_path="vector_store", data_dir="data"):
        self.vector_store_path = vector_store_path
        self.data_dir = data_dir
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = None
        
        # Load vector store if it exists
        if os.path.exists(self.vector_store_path) and os.path.isdir(self.vector_store_path):
            try:
                self.vector_store = FAISS.load_local(
                    self.vector_store_path, self.embeddings
                )
                print("Loaded existing vector store")
            except Exception as e:
                print(f"Error loading vector store: {e}")
        
    def check_vectors_exist(self) -> bool:
        """Check if vector store exists and is populated"""
        return self.vector_store is not None
    
    def ingest_documents(self):
        """Ingest documents from the data directory into the vector store"""
        # Create directories if they don't exist
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.vector_store_path, exist_ok=True)
        
        # Check for PDF files
        pdf_files = [f for f in os.listdir(self.data_dir) if f.endswith('.pdf')]
        
        if not pdf_files:
            print(f"No PDF files found in {self.data_dir}")
            return False
        
        # Extract text from PDFs
        documents = []
        for pdf_file in tqdm(pdf_files, desc="Processing PDFs"):
            pdf_path = os.path.join(self.data_dir, pdf_file)
            try:
                pdf = PdfReader(pdf_path)
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text.strip():  # Only add non-empty pages
                        documents.append(
                            Document(
                                page_content=text,
                                metadata={"source": pdf_file, "page": i}
                            )
                        )
            except Exception as e:
                print(f"Error processing {pdf_file}: {e}")
        
        if not documents:
            print("No text extracted from PDF files")
            return False
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        texts = text_splitter.split_documents(documents)
        
        # Create vector store
        self.vector_store = FAISS.from_documents(texts, self.embeddings)
        
        # Save vector store
        self.vector_store.save_local(self.vector_store_path)
        
        print(f"Ingested {len(texts)} document chunks into vector store")
        return True
    
    def answer_question(self, question: str) -> str:
        """
        Answer a question using the RAG system
        """
        if not self.check_vectors_exist():
            return "Please ingest documents first using the ingest.py script"
        
        # Create a retrieval chain
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(search_kwargs={"k": 5})
        )
        
        try:
            # Get answer
            result = qa_chain({"query": question})
            return result["result"]
        except Exception as e:
            return f"Error generating answer: {str(e)}"