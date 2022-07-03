import unittest
import main
import solution
from tools import SkyproTestCase
import re


class YearsTestCase(SkyproTestCase):

    def test_main_has_result(self):
        self.assertTrue(
            hasattr(main, 'result'),
            r'%@Проверьте, что переменная result существует')

    def test_result_format_is_correct(self):
        self.assertRegex(
            main.result,
            r'фильмы:\s[0-9]*\sшт\nсериалы:\s[0-9]*\sшт',
            r'%@Проверьте, что используете правильный формат выдачи')

    def test_hours_value_is_correct(self):
        value = re.findall(r"\d+", main.result)[0]
        author_value = re.findall(r"\d+", solution.result)[0]
        self.assertEqual(
            value, author_value,
            (r'%@Проверьте, что количество фильмов '
             'посчитано верно.'))

    def test_hours_value_is_correct(self):
        value = re.findall(r"\d+", main.result)[1]
        author_value = re.findall(r"\d+", solution.result)[1]
        self.assertEqual(
            value, author_value,
            (r'%@Проверьте, что количество сериалов '
             'посчитано верно.'))


if __name__ == "__main__":
    unittest.main()
