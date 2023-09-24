from flask import Flask,render_template,request
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
    return render_template('index.html',
                           book_name = list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_ratings'].values)
                           )
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/book-recommender-system')
def code():
    return render_template('book-recommender-system.html')

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')



@app.route('/recommend_books',methods=['post'])
def recommend():
    user_input = request.form.get('user_input')
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:6]
    data = []
    for i in similar_items:
        item = []
        #         print(pt.index[i[0]])
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

        data.append(item)
    print(data)

    return render_template('recommend.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)



