import pytest

from app.posts.dao.posts_dao import PostsDao


class TestsPostsDao:

    @pytest.fixture  # фикстура для тестирования
    def post_dao(self):
        return PostsDao('../data/posts.json')

    @pytest.fixture  # фикстура для тестирования
    def keys_expected(self):
        return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

    """Получение всех постов"""

    def test_get_all_check_type(self, post_dao):
        posts = post_dao.get_all()
        assert type(posts) == list, "Посты должны быть списком"
        assert type(posts[0]) == dict, "Каждый пост должен быть словарём"

    def test_get_all_has_keys(self, post_dao, keys_expected):
        posts = post_dao.get_all()
        first_post = posts[0]
        first_post_keys = set(first_post.keys())  # не зависимо от порядка, превращает во множество
        assert first_post_keys == keys_expected

    """Получение одного поста"""

    def test_get_one_check_type(self, post_dao):
        post = post_dao.get_by_pk(1)
        assert type(post) == dict, "Пост должен быть словарём"

    def test_get_one_has_keys(self, post_dao, keys_expected):
        post = post_dao.get_by_pk(1)
        post_keys = set(post.keys())
        assert post_keys == keys_expected, "Полученные ключи неверны"

    parameters_to_get_by_pk = [1, 2, 3, 4, 5, 6, 7, 8]

    @pytest.mark.parametrize('post_pk', parameters_to_get_by_pk)
    def test_get_one_check_type_has_correct_pk(self, post_dao, post_pk):
        post = post_dao.get_by_pk(post_pk)
        assert post['pk'] == post_pk, "Номер полученного поста не соответствует запрошенному номеру"

    """Получение поста по пользователю"""

    post_parameters_by_user = [('leo', {1, 5}), ('larry', {4, 8}), ('hank', {3, 7})]

    @pytest.mark.parametrize('poster_name, post_pks_correct', post_parameters_by_user)
    def test_get_posts_by_user(self, post_dao, poster_name, post_pks_correct):
        posts = post_dao.get_by_user(poster_name)
        post_pks = set()
        for post in posts:
            post_pks.add(post['pk'])

        assert post_pks == post_pks_correct, "Поиск по пользователю работает некорректно"

    """Поиск постов"""

    # post_parameters_search = [('погулять', {2}), ('бассейна', {4}), ('фотка', {5})]
    #
    # @pytest.mark.parametrize('query, post_pks_correct', post_parameters_search)
    # def test_search_for_posts(self, post_dao, query, post_pks_correct):
    #     posts = post_dao.search(query)
    #     post_pks = set()
    #     for post in posts:
    #         post_pks.add(post['pk'])
    #
    #     assert post_pks == post_pks_correct, "Поиск работает некорректно"
    