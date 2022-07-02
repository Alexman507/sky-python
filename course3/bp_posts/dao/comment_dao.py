import json
from json import JSONDecodeError

from course3.bp_posts.dao.comment import Comment
from course3.exceptions.data_exceptions import DataSourceError


class CommentDAO:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                comments_data = json.load(f)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из файла {self.path}")

        return comments_data

    def _load_comments(self):
        """Loader"""

        comments_data = self._load_data()
        list_of_comments = [Comment(**comment_data) for comment_data in comments_data]

        return list_of_comments

    def get_comments_by_post_id(self, post_pk: int) -> list[Comment]:
        """Получает все комменты к посту по его id"""

        comments_data: list[Comment] = self._load_comments()
        comments_match: list[Comment] = [c for c in comments_data if c.post_pk == post_pk]

        return comments_match
