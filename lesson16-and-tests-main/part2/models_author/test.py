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


class AuthorTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_model_author_columns_is_correct(self):
        student_columns = self.get_cursor_info(
            main.cursor_author).get('columns')
        author_columns = self.get_cursor_info(
            solution.cursor_author).get('columns')
        self.field_name_checker(student_columns, author_columns)

    def test_model_book_columns_is_correct(self):
        student_columns = self.get_cursor_info(
            main.cursor_book).get('columns')
        author_columns = self.get_cursor_info(
            solution.cursor_book).get('columns')
        self.field_name_checker(student_columns, author_columns)

    def test_model_author_id_field_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Author',
            type_name='Integer',
            fields=('id', ))

    def test_model_author_string_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Author',
            type_name='String',
            fields=('first_name', 'last_name'))

    def test_model_book_int_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Book',
            type_name='Integer',
            fields=('id', 'copyright', 'author_id'))

    def test_model_book_string_fields_has_correct_types(self):
        self.field_type_checker(
            module=main,
            model_name='Book',
            type_name='String',
            fields=('title', ))

    def test_model_book_has_foreign_key_author_id(self):
        model = main.Book
        self.assertFalse(
            model.author_id.property.expression.foreign_keys == set(),
            "%@ проверьте, что добавили опцию ForeignKey к полю 'author_id'")
        fkey_property = model.author_id.property.expression.foreign_keys.pop()
        self.assertTrue(
            fkey_property.target_fullname == 'author.id',
            "%@ Проверьте что поле author_id имеет"
            " опцию Foreign Key с параметром 'author.id'")

    def test_model_book_has_relationship_to_author(self):
        model = main.Book
        self.assertTrue(
            hasattr(model, 'author'),
            "%@Проверьте, что добавили в модель опцию author,"
            "которая связывает таблицы author и book c помощью функции"
            " db.relationship")


if __name__ == "__main__":
    unittest.main()
