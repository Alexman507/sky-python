import main
import sys
import solution
import unittest
from pathlib import Path
from flask_restx import Api, Namespace
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

    def setUp(self):
        self.student_app = main.app.test_client()
        self.author_app = solution.app.test_client()

    def test_module_have_api_instance(self):
        self.assertTrue(
            hasattr(main, 'api'),
            '%@Проверьте, что переменная api существует в модуле'
        )
        self.assertTrue(
            isinstance(main.api, Api),
            f"%@Проверьте, что переменная api является "
            f"экземпляром класса {Api}"
        )

    def test_module_have_books_ns_variable(self):
        self.assertTrue(
            hasattr(main, 'book_ns'),
            '%@Проверьте что переменная book_ns существует'
        )
        self.assertTrue(
            isinstance(main.book_ns, Namespace),
            "%@Проверьте что переменная book_ns создана с помощью"
            "функции namespace"
        )

    def test_view_books_is_available_and_works_correct(self):
        url = "/books/"
        test_options = {
            "url": url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.get(url),
            "author_response": self.author_app.get(url),
            "expected": list,
            "many": True
        }
        self.check_status_code_jsonify_and_expected(**test_options)
        self.compare_result_fields_with_author_solution(**test_options)


if __name__ == "__main__":
    unittest.main()
