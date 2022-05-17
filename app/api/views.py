import logging

from flask import Blueprint, render_template, jsonify
from app.posts.dao.posts_dao import PostsDao
from app.posts.dao.comments_dao import CommentsDao

api_blueprint = Blueprint("api_blueprint", __name__, template_folder='templates')

posts_dao = PostsDao("data/posts.json")
comments_dao = CommentsDao("data/comments.json")

logger = logging.getLogger("basic")


@api_blueprint.route('/api/posts/')
def post_all():

    logger.debug("Запрошены все посты через API")
    posts = posts_dao.get_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_pk>/')
def post_one(post_pk):

    logger.debug(f"Запрошен пост {post_pk} через API")
    post = posts_dao.get_by_pk(post_pk)
    return jsonify(post)
