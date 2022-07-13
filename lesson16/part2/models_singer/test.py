import sys
import unittest
from pathlib import Path
import os

import main
import solution
import sqlalchemy

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402


class SingerTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_model_singer_columns_is_correct(self):
        student_columns = self.get_cursor_info(
            main.cursor).get('columns')
        author_columns = self.get_cursor_info(
            solution.cursor).get('columns')
        self.field_name_checker(student_columns, author_columns)

    def test_model_singer_id_field_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Singer',
            type_name='Integer',
            fields=('id', 'age', ))

    def test_model_singer_string_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Singer',
            type_name='String',
            fields=('name', 'group', ))

    def test_models_singer_has_correct_age_constraint(self):
        with self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            msg=("%@Проверьте, что полю 'age' нельзя присвоить"
                 " значение больше 34")):
            model = main.Singer(name='Виктор', age=35, group='qwe')
            main.db.session.add(model)
            main.db.session.commit()

    def test_models_singer_has_correct_group_constraint(self):
        with self.assertRaises(
            sqlalchemy.exc.IntegrityError,
            msg=("%@Проверьте, что полю 'group' нельзя присвоить"
                 " Null значение (None)")):
            model = main.Singer(name='Виктор', age=34, group=None)
            main.db.session.add(model)
            main.db.session.commit()

    def test_models_singer_has_correct_name_constraint(self):
        with self.assertRaises(
                sqlalchemy.exc.IntegrityError,
                msg=("%@Проверьте, что поле 'name' является уникальным")):
            model = main.Singer(name='Виктор', age=34, group='qwe')
            model2 = main.Singer(name='Виктор', age=33, group='qwe1')
            models = (model, model2)
            main.db.session.add_all(models)
            main.db.session.commit()

    def tearDown(self):
        main.db.session.close()


if __name__ == "__main__":
    unittest.main()
