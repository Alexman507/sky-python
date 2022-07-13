import main
import sys
import solution
import unittest
import os
from pathlib import Path

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

    def setUp(self):
        self.student_app = main.app.test_client()
        self.author_app = solution.app.test_client()
        self.instance = {
            "id": 3,
            "text": "Текст заметки идет здесь",
            "author": "Кто ты?"
        }
        self.url = '/notes/'
        self.method = 'POST'

    def test_view_notes_is_available_and_works_correct(self):
        test_options = {
            "url": self.url,
            "method": self.method,
            "code": [201],
            "student_response": self.student_app.post(
                self.url, json=self.instance),
            "author_response":
            self.author_app.post(self.url, json=self.instance),
        }
        self.check_status_code_jsonify_and_expected(**test_options)

    def test_instance_is_added_to_list(self):
        self.student_app.post(self.url, json=self.instance)
        self.assertIn(
            self.instance, main.notes,
            (f"%@Проверьте, что {self.method}-запрос по адресу {self.url}"
             " добавляет сущность в список")
        )


if __name__ == "__main__":
    unittest.main()
