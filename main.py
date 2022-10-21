from flask import Flask
from markupsafe import escape

app = Flask(__name__)


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