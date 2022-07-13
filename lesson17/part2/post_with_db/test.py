import main
import sys
import solution
import unittest
from pathlib import Path
from sqlalchemy import text
import os

BASENAME = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import (        # noqa: E402
    ResponseTestsMixin, SchemaTestsMixin)


class SerializationTestCase(SkyproTestCase,
                            SchemaTestsMixin,
                            ResponseTestsMixin):
    @classmethod
    def setUpClass(cls) -> None:
        cls.INSTANCE = {
            "text": "Текст заметки идет здесь",
            "author": "Кто ты?"
        }
        cls.URL = '/notes/'
        cls.CREATE_TABLE_SQL = ("CREATE TABLE note ("
                                "id integer PRIMARY KEY, "
                                "text varchar(300), "
                                "author varchar(300))")

    def setUp(self):
        self.student_app = main.app.test_client()
        self.author_app = solution.app.test_client()
        self.db = main.db
        if self.db.session.is_active:
            self.db.session.close()
        self.db.drop_all()
        with self.db.session.begin():
            self.db.session.execute(text(self.CREATE_TABLE_SQL))

    def test_view_notes_is_available_and_works_correct(self):
        test_options = {
            "url": self.URL,
            "method": "POST",
            "code": [201],
            "student_response": self.student_app.post(
                self.URL, json=self.INSTANCE),
            "author_response":
            self.author_app.post(self.URL, json=self.INSTANCE),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_create_add_row_to_db(self):
        js = self.INSTANCE
        self.student_app.post(self.URL, json=self.INSTANCE)
        result = self.db.session.execute(
            "SELECT `text`, `author` from note").fetchall()
        self.assertTrue(
            result == [(js['text'], js['author'])],
            "%@Проверьте что функция create создает объект в базе данных"
        )

    def tearDown(self):
        self.db.session.close()


if __name__ == "__main__":
    unittest.main()
