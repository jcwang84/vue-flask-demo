from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'bookName': '金瓶梅',
        'author': '兰陵笑笑生',
        'read': True
    }, {
        'bookName': '西游记',
        'author': '吴承恩',
        'read': False
    },
    {
        'bookName': '三国演义',
        'author': '罗贯中',
        'read': True
    }

]


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('Greetings from the python backend !')


# @app.route('/girls', methods=['GET'])
# def get_all_books():
#     return jsonify({
#         'status': 'success',
#         'allBooks': BOOKS
#     })

@app.route('/', methods=['GET'])
def welcome():
    return 'Welcome to server'


@app.route('/books', methods=['GET', 'POST'])
def get_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'bookName': post_data.get('bookName'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS

    return jsonify(response_object)

@app.route('/home')
def home():
    return 'Login success!'


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run()
