import sys
import unittest
import os
from pathlib import Path

import flask_sqlalchemy

import main
import solution
import sqlalchemy
import inspect

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402

MODEL_NAME = 'Course'


class CourseTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_module_bookschema_exists(self):
        self.assertTrue(
            hasattr(main, MODEL_NAME),
            f"%@Проверьте есть ли класс {MODEL_NAME} в модуле")

    def test_bookschema_is_class(self):
        self.assertTrue(
            inspect.isclass(main.Course),
            f"%@Проверьте, что {MODEL_NAME} это класс"
        )

    def test_bookschema_inheritance_is_correct(self):
        self.assertTrue(
            issubclass(main.Course, flask_sqlalchemy.Model),
            ("%@Проверьте, правильно ли указан родительский класс у "
             f"класса {MODEL_NAME}. Попробуйте использовать экземпляр "
             "класса SQLAlchemy")
        )

    def test_model_columns_is_correct(self):
        student_columns = self.get_cursor_info(main.cursor).get('columns')
        author_columns = self.get_cursor_info(solution.cursor).get('columns')
        self.assertEqual(student_columns, author_columns,
                         (r'%@Проверьте, что правильно определили '
                          'поля модели. '
                          f'Вы выбрали {student_columns}, тогда '
                          f'как необходимо {author_columns}'))

    def test_model_course_text_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name=MODEL_NAME,
            type_name='Text',
            fields=('title', 'subject'))

    def test_model_course_integer_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name=MODEL_NAME,
            type_name='Integer',
            fields=('id', 'price'))

    def test_model_course_text_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name=MODEL_NAME,
            type_name='Float',
            fields=('weeks', ))


if __name__ == "__main__":
    unittest.main()
