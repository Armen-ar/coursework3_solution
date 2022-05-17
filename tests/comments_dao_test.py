import pytest

from app.posts.dao.comments_dao import CommentsDao


class TestsCommentsDao:

    @pytest.fixture
    def comments_dao(self):
        return CommentsDao('tests/mock/comments.json')  # если тест через интерфейс, тогда путь должен начинат. с '../'

    @pytest.fixture
    def keys_expected(self):
        return {"post_pk", "commenter_name", "comment", "pk"}

    """Получение комментариев"""

    def test_get_by_post_check_type(self, comments_dao):
        comments = comments_dao.get_by_post_pk(1)
        assert type(comments) == list, "Комментарии должны быть списком"
        assert type(comments[0]) == dict, "Каждый комментарии должен быть словарём"

    def test_get_by_post_check_has_keys(self, comments_dao, keys_expected):
        comment = comments_dao.get_by_post_pk(1)[0]
        comment_keys = set(comment.keys())
        assert comment_keys == keys_expected, "Полученные ключи неверны"

    parameters_for_comments = [(1, {1, 7}), (2, {13}), (0, set())]

    @pytest.mark.parametrize('post_pk, correct_comments_pks', parameters_for_comments)
    def test_get_by_post_pk_check_math(self, comments_dao, post_pk, correct_comments_pks):
        comments = comments_dao.get_by_post_pk(post_pk)
        comment_pks = set([comment['pk'] for comment in comments])
        assert comment_pks == correct_comments_pks, f"pk не совпадает для поста {post_pk}"
