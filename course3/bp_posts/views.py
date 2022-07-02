from flask import Blueprint, render_template, request
from werkzeug.exceptions import abort

from course3.bp_posts.dao.comment import Comment
from course3.bp_posts.dao.comment_dao import CommentDAO
from course3.bp_posts.dao.post import Post
from course3.bp_posts.dao.post_dao import PostDAO
from course3.config import DATA_PATH, COMMENTS_PATH

bp_posts = Blueprint('bp_posts', __name__, template_folder="templates")

# Paths for data
post_dao = PostDAO(DATA_PATH)
comments_dao = CommentDAO(COMMENTS_PATH)


@bp_posts.route('/')
def main_page():
    """Главная страница лентой"""
    posts = post_dao.get_all()

    return render_template('index.html',
                           posts=posts,
                           )


@bp_posts.route('/posts/<int:pk>')
def view_post(pk: int):
    """Просмотр поста"""
    post: Post | None = post_dao.get_by_pk(pk)
    comments: list[Comment] = comments_dao.get_comments_by_post_id(pk)

    if post is None:
        abort(404)

    return render_template('post.html',
                           post=post,
                           comments=comments
                           )


@bp_posts.route('/search/')
def search_posts():
    """Поиск по постам"""
    query: str = request.args.get('s', '')

    if query == "":
        posts: list = []
    else:
        posts = post_dao.search_in_content(query)

    return render_template('search.html',
                           query=query,
                           posts=posts
                           )


@bp_posts.route('/users/<user_name>')
def page_posts_by_user(user_name: str):
    "Посты пользователя"
    posts: list[Post] = post_dao.get_by_poster(user_name)

    if not posts:
        abort(404, "User not found")

    return render_template('user-feed.html',
                           posts=posts,
                           user_name=user_name)