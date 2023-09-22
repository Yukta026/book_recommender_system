from flask import Flask,render_template,request
import os
import pickle
import joblib
import numpy as np
import pandas as pd
import logging

app = Flask(__name__)

log_dir = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'app.log')

logging.basicConfig(filename=log_file, level=logging.DEBUG)

try:
    popular_path = os.path.join(os.path.dirname(__file__), 'popular.pkl')
    pt_path = os.path.join(os.path.dirname(__file__), 'pt.pkl')
    books_path = os.path.join(os.path.dirname(__file__), 'books.pkl')
    similarity_scores_path = os.path.join(os.path.dirname(__file__), 'similarity_scores.pkl')

    with open(popular_path, 'rb') as file1, open(pt_path, 'rb') as file2, open(books_path, 'rb') as file3, open(similarity_scores_path, 'rb') as file4:
        popular = pickle.load(file1)
        pt = pickle.load(file2)
        books = pickle.load(file3)
        similarity_scores = pickle.load(file4)
    # Define your Flask routes and use the loaded models as needed.
except Exception as e:
    logging.error(f"Error during initialization: {str(e)}")
    raise  # Reraise the exception to trigger an application error response


app =Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name = list(popular['Book-Title'].values),
                           author=list(popular['Book-Author'].values),
                           image=list(popular['Image-URL-M'].values),
                           votes=list(popular['num_ratings'].values),
                           rating=list(popular['avg_ratings'].values)
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

