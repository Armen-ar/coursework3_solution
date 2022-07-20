from app.api.views import post_all, post_one


# def test_post_all():
#     posts = posts_dao.get_all()
#     response = post_all.test_client().get('/api/posts/', query_string=posts)
#     assert response.status_code == 200
#     assert len(response.json) == 7


def test_app():
    response = post_all.test_client().get('/')
    assert response.json.get[0]("poster_name") == "Leo", "Имя получено неверно"
    """
    Чтобы вытащить ответ в формате JSON нужен response.json
    И для получения имени get("name") == "Алиса", иначе .......
    """
# def test_post_one():
#     params = {"s": "новичков"}
#     response = post_one.test_client().get('/api/posts/3/', query_string=params)
#     print(response.json)
#     assert response.status_code == 200
#     assert len(response.json) == 1
#
#
# def test_post_none():
#     params = {"s": "java"}
#     response = post_all.test_client().get('/', query_string=params)
#     print(response.json)
#     assert response.status_code == 200
#     assert len(response.json) == 0
