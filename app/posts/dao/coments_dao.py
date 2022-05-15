import json


class CommentsDao:
    """Класс для работы со всеми комментами"""

    def __init__(self, path):
        self.path = path

    def _load_comments(self):
        """Открывает json файл и сохраняет в виде списка словарей"""
        with open(f"{self.path}", "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def get_by_post_pk(self, post_pk):
        """Возвращает коммент по номеру"""
        comments = self._load_comments()
        comments_by_pk = []
        for comment in comments:
            if comment['post_pk'] == post_pk:
                comments_by_pk.append(comment)
        return comments_by_pk


