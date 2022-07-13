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


class SerializationTestCase(SkyproTestCase,
                            SchemaTestsMixin,
                            ResponseTestsMixin):

    def setUp(self):
        self.student_app = main.app.test_client()
        self.author_app = solution.app.test_client()

    def test_view_notes_is_available_and_works_correct(self):
        url = "/notes/"
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

    def test_view_notes_id_is_available_and_works_correct(self):
        url = "/notes/1"
        test_options = {
            "url": url,
            "method": "GET",
            "code": [200],
            "student_response": self.student_app.get(url),
            "author_response": self.author_app.get(url),
            "expected": dict,
        }
        self.check_status_code_jsonify_and_expected(**test_options)
        self.compare_result_fields_with_author_solution(**test_options)


if __name__ == "__main__":
    unittest.main()
