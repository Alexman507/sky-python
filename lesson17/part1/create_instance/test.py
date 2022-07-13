import main
import sys
import solution
import unittest
from flask_sqlalchemy import SQLAlchemy
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
from ttools.skyprotests.tests_mixins import SchemaTestsMixin  # noqa: E402

SQL_QUERY = ("CREATE TABLE role ("
             "id integer PRIMARY KEY, "
             "name varchar(200))")


class SerializationTestCase(SkyproTestCase, SchemaTestsMixin):

    @classmethod
    def setUpClass(self):
        self.app = main.app
        self.db = SQLAlchemy(self.app)
        self.db.drop_all()
        with self.db.session.begin():
            self.db.session.execute(text(SQL_QUERY))

    def test_role_schema_is_valid(self):
        self.schema_is_valid(
            main=main,
            schema_name='RoleSchema')

    def test_role_schema_names_and_types_is_valid(self):
        self.compare_schema_with_author_solution(
            student_schema=main.RoleSchema,
            author_schema=solution.RoleSchema)

    def test_create_add_row_to_db(self):
        js = {"id": 1, "name": "Student"}
        main.create(js)
        result = self.db.session.execute("SELECT * from role").fetchall()
        self.assertTrue(
            result == [(js['id'], js['name'])],
            "%@Проверьте что функция create создает объект в базе данных"
        )


if __name__ == "__main__":
    unittest.main()
