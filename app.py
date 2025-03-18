from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from utils.rag import RAGQuestionAnswerer

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize RAG system
rag = RAGQuestionAnswerer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    
    if not question:
        return jsonify({'answer': 'Please ask a question'})
    
    # Get answer using RAG
    answer = rag.answer_question(question)
    
    return jsonify({'answer': answer})

@app.route('/status')
def status():
    # Check if vector store exists
    has_vectors = rag.check_vectors_exist()
    return jsonify({'has_vectors': has_vectors})

if __name__ == '__main__':
    app.run(debug=True)