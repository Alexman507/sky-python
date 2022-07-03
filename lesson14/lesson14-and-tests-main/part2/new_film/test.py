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

    def test_film_name_is_correct(self):
        value = re.findall(r"[\w+]*", main.result)[0]
        author_value = re.findall(r"[\w+]*", solution.result)[0]
        self.assertEqual(
            value, author_value,
            (r'%@Проверьте, на самом ли деле название '
             'фильма верное.'))


if __name__ == "__main__":
    unittest.main()
