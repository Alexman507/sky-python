import sys
import unittest
import os
from pathlib import Path

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

MODEL_NAME = 'City'


class CityTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_model_columns_is_correct(self):
        student_columns = self.get_cursor_info(main.cursor).get('columns')
        author_columns = self.get_cursor_info(solution.cursor).get('columns')
        self.assertEqual(student_columns, author_columns,
                         (r'%@Проверьте, что правильно определили '
                          'поля модели. '
                          f'Вы выбрали {student_columns}, тогда '
                          f'как необходимо {author_columns}'))

    def test_model_city_integer_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='City',
            type_name='Integer',
            fields=('id', 'population'))

    def test_model_city_string_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='City',
            type_name='String',
            fields=('name', 'country_ru'))


if __name__ == "__main__":
    unittest.main()
