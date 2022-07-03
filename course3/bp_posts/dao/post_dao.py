import json
from json import JSONDecodeError

from course3.bp_posts.dao.post import Post
from course3.exceptions.data_exceptions import DataSourceError


class PostDAO:
    """
    Менеджер постов - загрузка, поиск и передача по pk и пользователю
    """

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """Загрузка из JSON и возврат список словарей"""
        try:
            with open(self.path, 'r', encoding='utf8') as file:
                posts_data = json.load(file)
        except (FileNotFoundError, JSONDecodeError):
            raise DataSourceError(f"Не удается получить данные из файла {self.path}")

        return posts_data

    def _load_posts(self):
        """Возвращает список экземпляров Post"""

        posts_data = self._load_data()
        list_of_posts = [Post(**post_data) for post_data in posts_data]
        return list_of_posts

    def get_all(self):
        """
        Получает все посты, возвращает список всех экземпляров класса Post
        """
        posts = self._load_posts()
        return posts

    def get_by_pk(self, pk):
        """Возвращает список всех экземпляров класса Post"""

        if type(pk) != int:
            raise TypeError("pk must be an integer")

        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):
        """Ищет посты на соответствие substring"""

        if type(substring) != str:
            raise TypeError('Substring must be a string')
        substring = substring.lower()
        posts = self._load_posts()

        matching_posts = [post for post in posts if substring in post.content.lower()]

        return matching_posts

    def get_by_poster(self, user_name):
        """Поиск по автору"""
        if type(user_name) != str:
            raise TypeError('Substring must be a string')

        user_name = str(user_name).lower()
        posts = self._load_posts()
        matching_posts = [post for post in posts if post.poster_name.lower() == user_name]

        return matching_posts
