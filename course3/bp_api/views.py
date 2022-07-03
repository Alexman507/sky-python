from flask import Blueprint, jsonify

from course3.utils import get_posts_all, get_post_by_pk

blueprint_api = Blueprint("api", __name__, url_prefix='/api')


@blueprint_api.route('/posts/')
def api_posts():
    posts = get_posts_all()
    return jsonify(posts)


@blueprint_api.route('/posts/<int:post_id>')
def api_post_id(post_id):
    post = get_post_by_pk(post_id)
    return jsonify(post)
