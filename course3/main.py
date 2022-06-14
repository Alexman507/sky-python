from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.get('/')
def main_page():
    """Главная страница лентой"""

    return render_template('index.html')


@app.get('/posts/<postid>')
def comment_by_post(postid):
    """Просмотр поста"""
    comment = utils.get_comments_by_post_id(postid)

    return render_template('post.html', post=comment)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
