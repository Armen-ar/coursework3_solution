import json


class PostsDao:
    """Класс для работы со всеми постами"""

    def __init__(self, path):
        self.path = path

    def _load_posts(self):
        """Открывает json файл и сохраняет в виде списка словарей"""
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def get_all(self):
        """Возвращает все посты"""
        return self._load_posts()

    def get_by_pk(self, pk):
        """Возвращает пост по номеру"""
        posts = self.get_all()

        for post in posts:
            if post["pk"] == pk:
                return post

    def get_by_user(self, user_name):
        """Возвращает пост по имени"""
        posts = self.get_all()
        posts_by_user = []

        for post in posts:
            if post["poster_name"] == user_name:
                posts_by_user.append(post)

        return posts_by_user

    def search(self, query):
        """Возвращает пост по вхождению"""
        posts = self.get_all()
        matching_posts = []
        query_lower = query.lower

        for post in posts:
            if query_lower in post['content'].lower:
                matching_posts.append(post)

        return matching_posts
