from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import request


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '2de9b21f898814dacea17bff17dac4d26d8c5c9c41ac6327'

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/mushrooms")
def mushrooms():
    return "<p>This is mushrooms</p>"


# http://localhost:5000/user/Dmytro
@app.route('/user/<usr>')
def show_user_profile(usr):
    # show the user profile for that user
    return f'User {escape(usr)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('home.html', name=name)

@app.route('/create', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        print(request.form['username'])
    return render_template('create.html')
