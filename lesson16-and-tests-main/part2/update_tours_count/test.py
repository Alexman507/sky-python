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


class ToursCompanyNoneTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_function_retuns_correct_value(self):
        result = main.cursor.execute(
            "SELECT tours_count FROM guide where `id`=1")
        result = result.fetchall()
        self.assertEqual(
            result[0][0], 6,
            "%@Проверьте, что у гида с id=1,"
            " значение поля tours_count обновлено до 6 и "
            "изменения зафиксированы с помощью функции commit")


if __name__ == "__main__":
    unittest.main()
