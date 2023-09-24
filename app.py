logging.basicConfig(filename='app.log', level=logging.DEBUG)

# Define a function to load pickle files
def load_pickle(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = pickle.load(file)
        return data
    except Exception as e:
        logging.error(f"Error loading pickle file: {str(e)}")
        return None

# Define the paths to your pickle files
script_dir = os.path.dirname(os.path.abspath(__file__))
popular_path = os.path.join(script_dir, 'popular.pkl')
pt_path = os.path.join(script_dir, 'pt.pkl')
books_path = os.path.join(script_dir, 'books.pkl')
similarity_scores_path = os.path.join(script_dir, 'similarity_scores.pkl')
# Load the pickle files
popular = load_pickle(popular_path)
pt = load_pickle(pt_path)
books = load_pickle(books_path)
similarity_scores = load_pickle(similarity_scores_path)


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

