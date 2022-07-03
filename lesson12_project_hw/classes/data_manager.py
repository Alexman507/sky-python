import json
# from pprint import pprint as pp
import logging

from classes.exceptions import DataSourceBrokenException

logger = logging.getLogger("basic")

class DataManager:

    def __init__(self, path):
        self.path = path

    def _load_data(self):
        """Загрузка данных из файла для других методов"""
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):

            raise DataSourceBrokenException("Файл с данными повреждён")

        return data

    def _save_data(self, data):
        """Перезапись переданных данных в файл с данными"""
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def get_all(self):
        """Передача полного списка данных"""
        data = self._load_data()
        return data

    def search(self, substring):
        """Отдаёт посты, содержащие substring"""

        posts = self._load_data()
        substring = substring.lower()

        matching_posts = [post for post in posts if substring in post["content"].lower()]

        return matching_posts

    def add(self, post):
        """Добавляет определенный пост в хранилище"""

        if type(post) != dict:
            logger.warning("Передача не в формате словаря")
            raise TypeError("Можно добавлять только словари!")

        posts = self._load_data()
        posts.append(post)
        self._save_data(posts)


# dm = DataManager("../tests/mock_post.json")
#
# post = {"pic": "screen", "content": "amogus"}
#
# pp(dm.add(post))
