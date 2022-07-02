import pytest


def check_fields(post):
    fields = ["poster_name", "poster_avatar", "pic", "content", ""]

    for field in fields:
        assert hasattr(post, field), f"Нет поля {field}"


class TestPostsDAO:

    @pytest.fixture
    def post_dao(self):
        post_dao_instance = PostDAO("./bp_posts/tests/post_mock.json")
        return post_dao_instance

    def test_get_all_types(self, post_dao):
        posts = post_dao.get_all()
        assert type(posts) == list, "Incorrect type for result"
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_all()
        post = post_dao.get_all()[0]
        check_fields(post)

    def test_get_all_correct_ids(self, post_dao):
        posts = post_dao.get_all()

        correct_pks = {1, 2, 3}
        pks = set([post.pk for post in posts])