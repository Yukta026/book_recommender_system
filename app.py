from flask import Flask, render_template, request
import os
import pickle
import joblib
import numpy as np
import pandas as pd
import logging

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.DEBUG)

try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(script_dir, 'popular.pkl')
    pt_path = os.path.join(script_dir, 'pt.pkl')
    books_path = os.path.join(script_dir, 'books.pkl')
    similarity_scores_path = os.path.join(script_dir, 'similarity_scores.pkl')
    with open(model_path, 'rb') as file:
            popular = pickle.load(file)
    with open(pt_path, 'rb') as file:
            pt = pickle.load(file)
    with open(books_path, 'rb') as file:
            books = pickle.load(file)
    with open(similarity_scores_path, 'rb') as file:
            similarity_scores = pickle.load(file)
except Exception as e:
        logging.error(f"Error loading pickle file: {str(e)}")
    
@app.route('/')
def index():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)



