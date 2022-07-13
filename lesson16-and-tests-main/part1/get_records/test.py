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


class CourseTestCase(SkyproTestCase, DataBaseTestsMixin):

    def setUp(self):
        self.student_get_one = main.get_one
        self.student_get_all = main.get_all
        self.author_get_one = solution.get_one
        self.author_get_all = solution.get_all

    def test_get_all_returns_list(self):
        self.assertTrue(
            isinstance(self.student_get_all(), list),
            "%@Проверьте, что при вызове функции get_all возвращается лист"
        )

    def test_get_all_is_not_empty(self):
        self.assertFalse(
            self.student_get_all == [],
            "%@Проверьте, что при вызове функции get_all"
            " возвращается не пустой лист"
        )

    def test_get_all_items_is_user_instance(self):
        self.assertTrue(
            isinstance(self.student_get_all()[0], main.User),
            ("%@Проверьте что при вызове функции get_all "
             "в возвращаемом массиве содержатся экземпляры модели User")
        )

    def test_get_all_returns_all_items(self):
        self.assertEqual(
            len(self.student_get_all()),
            len(self.author_get_all()),
            "%@Проверьте что при вызове функции get_all возвращаются все "
            "объекты из таблицы"
        )

    def test_get_one_returns_user_instance(self):
        index = 4
        self.assertTrue(
            isinstance(self.student_get_one(index), main.User),
            "%@Проверьте, что функция get_one "
            " возвращает экземпляр класса User")

    def test_get_one_returns_сorrect_value(self):
        index = 4
        instance_student = self.student_get_one(
            index).__dict__
        instance_author = self.author_get_one(
            index).__dict__
        del instance_student['_sa_instance_state']
        del instance_author['_sa_instance_state']
        self.assertEqual(
            instance_student,
            instance_author,
            "%@Проверьте, что get_one возвращает объект в соответствии с "
            "принятым аргументом ")


if __name__ == "__main__":
    unittest.main()
