import sys
import unittest
from pathlib import Path
import os

import main
import solution

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402


class GuideTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_model_guide_columns_is_correct(self):
        student_columns = self.get_cursor_info(
            main.cursor_guide).get('columns')
        author_columns = self.get_cursor_info(
            solution.cursor_guide).get('columns')
        self.field_name_checker(student_columns, author_columns)

    def test_model_excursion_columns_is_correct(self):
        student_columns = self.get_cursor_info(
            main.cursor_excursion).get('columns')
        author_columns = self.get_cursor_info(
            solution.cursor_excursion).get('columns')
        self.field_name_checker(student_columns, author_columns)

    def test_model_guide_id_field_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Guide',
            type_name='Integer',
            fields=('id', ))

    def test_model_author_string_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Guide',
            type_name='String',
            fields=('name', 'main_speciality', 'country'))

    def test_model_excursion_int_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Excursion',
            type_name='Integer',
            fields=('id', 'guide_id', ))

    def test_model_book_string_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Excursion',
            type_name='String',
            fields=('name', ))

    def test_model_book_has_foreign_key_author_id(self):
        model = main.Excursion
        target = 'guide.id'
        self.assertFalse(
            model.guide_id.property.expression.foreign_keys == set(),
            "%@ проверьте, что добавили опцию ForeignKey к полю 'guide_id'")
        fkey_property = model.guide_id.property.expression.foreign_keys.pop()
        self.assertTrue(
            fkey_property.target_fullname == target,
            "%@ Проверьте что поле author_id имеет"
            f" опцию Foreign Key с параметром {target}")

    def test_model_book_has_relationship_to_author(self):
        model = main.Excursion
        self.assertTrue(
            hasattr(model, 'guide'),
            "%@Проверьте, что добавили в модель опцию guide,"
            "которая связывает таблицы author и book c помощью функции"
            " db.relationship")


if __name__ == "__main__":
    unittest.main()
