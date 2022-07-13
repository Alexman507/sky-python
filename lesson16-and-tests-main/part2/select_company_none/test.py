import sys
import unittest
import os
from pathlib import Path

import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import DataBaseTestsMixin  # noqa: E402

MODEL_NAME = 'City'


class ToursCompanyNoneTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_function_returns_list(self):
        self.assertTrue(isinstance(main.do_request(), list),
                        "%@Проверьте что функция do_request"
                        " возвращает список значений")

        self.assertTrue(len(main.do_request()) != 0,
                        "%@Проверьте что список значений возвращаемых "
                        " функцией do_request не пустой")

        self.assertTrue(
            isinstance(main.do_request()[0], main.Guide),
            "%@Проверьте что список значений возвращаемых "
            " функцией do_request содержит экземпляры модели Guide")

    def test_function_retuns_correct_value(self):
        value_list = main.do_request()
        for instance in value_list:
            self.assertEqual(
                instance.company, None,
                "%@Проверьте, что в результате запроса содержатся"
                " только те записи, в которых значение поля company=None")


if __name__ == "__main__":
    unittest.main()
