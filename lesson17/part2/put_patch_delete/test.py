import main
import sys
import solution
import unittest
from pathlib import Path
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


NOTES = {
    1: {
        "id": 1,
        "text": "this is my super secret note",
        "author": "me"
    },
    2: {
        "id": 2,
        "text": "oh, my note",
        "author": "me"
    }
}


class PatchTestCase(SkyproTestCase,
                    SchemaTestsMixin,
                    ResponseTestsMixin):

    def setUp(self):
        self.student_app_patch = main.app.test_client().patch
        self.author_app_patch = solution.app.test_client().patch
        main.notes = {
            1: {
                "id": 1,
                "text": "this is my super secret note",
                "author": "me"
            }
        }
        self.patch_author = {
            "author": "Новый автор"
        }
        self.patch_text = {
            "text": "Новый текст заметки"
        }
        self.method = "PATCH"
        self.url = "notes/1"

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
        note = main.notes.get(1)
        self.assertTrue(
            self.patch_author['author'] == note.get('author'),
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " корректно изменяет автора заметки")
        )
        self.student_app_patch(self.url, json=self.patch_text)
        note = main.notes.get(1)
        self.assertTrue(
            self.patch_text['text'] == note.get('text'),
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " корректно изменяет текст заметки")
        )


class PutTestCase(SkyproTestCase,
                  SchemaTestsMixin,
                  ResponseTestsMixin):

    def setUp(self):
        self.student_app_put = main.app.test_client().put
        self.author_app_put = solution.app.test_client().put
        main.notes = {
            1: {
                "id": 1,
                "text": "this is my super secret note",
                "author": "me"
            }
        }
        self.put_instance = {
            "author": "Новый автор",
            "text": "Новый текст заметки"
        }
        self.method = "PUT"
        self.url = "notes/1"

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
        note = main.notes.get(1)
        self.assertTrue(
            self.put_instance.get('author') == note.get('author'),
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " изменяет автора заметки")
        )
        self.assertTrue(
            self.put_instance.get('text') == note.get('text'),
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " изменяет автора заметки")
        )


class DeleteTestCase(SkyproTestCase,
                     SchemaTestsMixin,
                     ResponseTestsMixin):

    def setUp(self):
        self.student_app_delete = main.app.test_client().delete
        self.author_app_delete = solution.app.test_client().delete
        main.notes = {
            1: {
                "id": 1,
                "text": "this is my super secret note",
                "author": "me"
            }
        }
        self.method = "DELETE"
        self.url = "notes/1"

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
        note = main.notes.get(1)
        self.assertFalse(
            note,
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " удаляет запись из листа")
        )


if __name__ == "__main__":
    unittest.main()
