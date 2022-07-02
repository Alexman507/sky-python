from flask import Blueprint, jsonify, render_template, request
from werkzeug.exceptions import abort

from course3.bp_posts.dao.comment import Comment
from course3.bp_posts.dao.comment_dao import CommentDAO
from course3.bp_posts.dao.post import Post
from course3.bp_posts.dao.post_dao import PostDAO
from course3.config import DATA_PATH, COMMENTS_PATH
from course3.utils import get_posts_all, get_post_by_pk

# Blueprints
bp_posts = Blueprint('bp_posts', __name__, template_folder="templates")
blueprint_api = Blueprint("api", __name__, url_prefix='/api')

# Paths for data
post_dao = PostDAO(DATA_PATH)
comments_dao = CommentDAO(COMMENTS_PATH)


@bp_posts.route('/')
def main_page():
    """Главная страница лентой"""
    posts = post_dao.get_all()

    return render_template('index.html', posts=posts)


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
    "Просмота постаница"""
    search: str = request.args.get('search', '')

    if search == '':
        posts: list = []
    else:
        posts = post_dao.search_in_content(search)

    return render_template('search.html',
                           search=search,
                           posts=posts
                           )


@bp_posts.route('/user/<user_name>')
def page_posts_by_user(user_name: str):
    "Посты пользователя"
    posts: list[Post] = post_dao.get_by_poster(user_name)

    return render_template('user-feed.html',
                           posts=posts,
                           user_name=user_name)


@blueprint_api.route('/posts/')
def api_posts():
    posts = get_posts_all()
    return jsonify(posts)


@blueprint_api.route('/posts/<int:post_id>')
def api_post_id(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)
