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


CREATE_TABLE = ("CREATE TABLE note ("
                "id integer PRIMARY KEY, "
                "text varchar(300), "
                "author varchar(300))")

INSERT_ROWS = ("INSERT INTO note"
               "('text', 'author') VALUES "
               "('test_text', 'test_author'),"
               "('second_test_text', 'second_test_author')")


class PatchTestCase(SkyproTestCase,
                    SchemaTestsMixin,
                    ResponseTestsMixin):

    @classmethod
    def setUpClass(cls) -> None:
        cls.method = "PATCH"
        cls.url = "notes/1"
        cls.patch_author = {
            "author": "Новый автор"
        }
        cls.patch_text = {
            "text": "Новый текст заметки"
        }

    def setUp(self):
        self.student_app_patch = main.app.test_client().patch
        self.author_app_patch = solution.app.test_client().patch
        self.db = main.db
        if self.db.session.is_active:
            self.db.session.close()
        self.db.drop_all()
        with self.db.session.begin():
            self.db.session.execute(text(CREATE_TABLE))
            self.db.session.execute(text(INSERT_ROWS))

    def test_patch_method_with_id_is_available_and_works_correct(self):
        test_options = {
            "url": self.url,
            "method": self.method,
            "code": [204],
            "student_response": self.student_app_patch(
                self.url, json=self.patch_author),
            "author_response":
            self.author_app_patch(self.url, json=self.patch_author),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_patch_method_without_id_returns_404(self):
        self.url = "notes/900"
        response = self.student_app_patch(self.url, json=self.patch_author)
        self.assertEqual(
            response.status_code, 404,
            (f"%@ Проверьте, что при {self.method}-запросе на адрес {self.url}"
             "(с несуществующим id) в ответе возвращается код 404")
        )

    def test_instance_is_patched_in_list(self):
        self.student_app_patch(self.url, json=self.patch_author)
        note = main.Note.query.get(1)
        self.assertTrue(
            self.patch_author['author'] == note.author,
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " корректно изменяет автора заметки")
        )
        self.student_app_patch(self.url, json=self.patch_text)
        note = main.Note.query.get(1)
        self.assertTrue(
            self.patch_text['text'] == note.text,
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " корректно изменяет текст заметки")
        )

    def tearDown(self):
        self.db.session.close()


class PutTestCase(SkyproTestCase,
                  SchemaTestsMixin,
                  ResponseTestsMixin):

    @classmethod
    def setUpClass(cls) -> None:
        cls.method = "PUT"
        cls.url = "notes/1"
        cls.put_instance = {
            "author": "Новый автор",
            "text": "Новый текст заметки"
        }

    def setUp(self):
        self.student_app_put = main.app.test_client().put
        self.author_app_put = solution.app.test_client().put
        self.db = main.db
        if self.db.session.is_active:
            self.db.session.close()
        self.db.drop_all()
        with self.db.session.begin():
            self.db.session.execute(text(CREATE_TABLE))
            self.db.session.execute(text(INSERT_ROWS))

    def test_put_method_with_id_is_available_and_works_correct(self):
        test_options = {
            "url": self.url,
            "method": self.method,
            "code": [204],
            "student_response": self.student_app_put(
                self.url, json=self.put_instance),
            "author_response":
            self.author_app_put(self.url, json=self.put_instance),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_patch_method_without_id_returns_404(self):
        self.url = "notes/900"
        response = self.student_app_put(self.url, json=self.put_instance)
        self.assertEqual(
            response.status_code, 404,
            (f"%@ Проверьте, что при {self.method}-запросе на адрес {self.url}"
             "(с несуществующим id) в ответе возвращается код 404")
        )

    def test_instance_is_fully_updated_in_list(self):
        self.student_app_put(self.url, json=self.put_instance)
        note = main.Note.query.get(1)
        self.assertTrue(
            self.put_instance.get('author') == note.author,
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " изменяет автора заметки")
        )
        self.assertTrue(
            self.put_instance.get('text') == note.text,
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " изменяет автора заметки")
        )

    def tearDown(self):
        self.db.session.close()


class DeleteTestCase(SkyproTestCase,
                     SchemaTestsMixin,
                     ResponseTestsMixin):

    @classmethod
    def setUpClass(cls) -> None:
        cls.method = "DELETE"
        cls.url = "notes/1"

    def setUp(self):
        self.student_app_delete = main.app.test_client().delete
        self.author_app_delete = solution.app.test_client().delete
        self.db = main.db
        if self.db.session.is_active:
            self.db.session.close()
        self.db.drop_all()
        with self.db.session.begin():
            self.db.session.execute(text(CREATE_TABLE))
            self.db.session.execute(text(INSERT_ROWS))

    def test_delete_method_with_id_is_available_and_works_correct(self):
        test_options = {
            "url": self.url,
            "method": self.method,
            "code": [204],
            "student_response": self.student_app_delete(self.url),
            "author_response": self.author_app_delete(self.url),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_delete_method_without_id_returns_404(self):
        self.url = "notes/900"
        response = self.student_app_delete(self.url)
        self.assertEqual(
            response.status_code, 404,
            (f"%@ Проверьте, что при {self.method}-запросе на адрес {self.url}"
             "(с несуществующим id) в ответе возвращается код 404")
        )

    def test_instance_is_fully_updated_in_list(self):
        self.student_app_delete(self.url)
        note = {}
        note = main.Note.query.get(1)
        self.assertFalse(
            note,
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " удаляет запись из листа")
        )

    def tearDown(self):
        self.db.session.close()


if __name__ == "__main__":
    unittest.main()
