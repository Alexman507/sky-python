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
from ttools.skyprotests.tests_mixins import SchemaTestsMixin  # noqa: E402


class SerializationTestCase(SkyproTestCase, SchemaTestsMixin):

    def test_role_schema_is_valid(self):
        self.schema_is_valid(
            main=main,
            schema_name='RoleSchema')

    def test_role_schema_names_and_types_is_valid(self):
        self.compare_schema_with_author_solution(
            student_schema=main.RoleSchema,
            author_schema=solution.RoleSchema)

    def test_serialize_returns_json_format(self):
        self.assertTrue(
            isinstance(main.serialize(), list),
            "%@Проверьте что функция serialize возвращает список")


if __name__ == "__main__":
    unittest.main()
