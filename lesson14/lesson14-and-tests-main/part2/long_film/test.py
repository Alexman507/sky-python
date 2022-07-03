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
            r'(\w+)*\s[-—]\s[0-9]*\sминут',
            r'%@Проверьте, что используете правильный формат выдачи')

    def test_query_exists_year_condition(self):
        value = re.findall(r"\d+", main.result)
        author_value = re.findall(r"\d+", solution.result)
        self.assertEqual(
            value, author_value,
            (r'%@Проверьте, на самом ли деле это '
             'самый длинный фильм 2019 года.'))

    def test_film_name_is_correct(self):
        value = re.findall(r"[\w+\s]*", main.result)[0]
        author_value = re.findall(r"[\w+\s]*", solution.result)[0]
        self.assertEqual(
            value, author_value,
            (r'%@Проверьте, на самом ли деле название '
             'фильма верное.'))


if __name__ == "__main__":
    unittest.main()
