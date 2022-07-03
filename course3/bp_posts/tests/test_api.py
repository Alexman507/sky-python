import random

from course3.main import app
from lesson10.hw10.utils import load_data


class TestAPI:
    def test_api_posts(self):
        response = app.test_client().get("/api/posts", follow_redirect=True)
        assert response.status_code == 200
        assert type(response.data) == list
        assert len(response.data) != 0

    def test_api_post(self):
        posts_data = load_data()
        rand_data = random.choice(posts_data)

        response = app.test_client().ger(f"/api/posts/{rand_data['pk']}", follow_redirect=True)
        assert response.status_code == 200
        assert type(response.data) == dict
        assert response.json.keys() == {"poster_name",
                                        "poster_avatar",
                                        "pic", "content",
                                        "views_count", "likes_count"}

