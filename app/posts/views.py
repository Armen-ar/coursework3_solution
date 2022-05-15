import logging

from flask import Blueprint, render_template
from app.posts.dao.posts_dao import PostsDao
from app.posts.dao.coments_dao import CommentsDao

posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder='templates')
posts_dao = PostsDao("data/posts.json")
comments_dao = CommentsDao("data/comments.json")

logger = logging.getLogger("basic")


@posts_blueprint.route('/')
def post_all():

    logger.debug("Запрошены все посты")
    try:
        posts = posts_dao.get_all()
        return render_template('index.html', posts=posts)
    except:
        return "Ошибка открытия всех постов"


@posts_blueprint.route('/posts/<int:post_pk>/')
def post_one(post_pk):

    logger.debug(f"Запрошен пост {post_pk}")
    try:
        post = posts_dao.get_by_pk(post_pk)
        comments = comments_dao.get_by_post_pk(post_pk)
        number_of_comments = len(comments)
        return render_template('post.html', post=post, comments=comments, number_of_comments=number_of_comments)
    except:
        return "Ошибка открытия одного поста с комментами"


@posts_blueprint.route('/search')
def post_search():
    return "Поиск поста"


@posts_blueprint.route('/users/<username>/')
def post_by_user(username):
    return "Поиск по имени"
