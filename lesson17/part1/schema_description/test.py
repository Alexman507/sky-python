import main
import unittest
import solution
from pathlib import Path
import sys
import os

BASENAME = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(BASENAME)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import SchemaTestsMixin  # noqa: E402


class SchemaTestCase(SkyproTestCase, SchemaTestsMixin):

    def test_bookschema_is_valid(self):
        self.schema_is_valid(
            main=main,
            schema_name='BookSchema')

    def test_bookschema_field_names_and_types_is_valid(self):
        self.compare_schema_with_author_solution(
            student_schema=main.BookSchema,
            author_schema=solution.BookSchema)


if __name__ == "__main__":
    unittest.main()
