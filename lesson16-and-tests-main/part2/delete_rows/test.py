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


class DeleteRowsTestCase(SkyproTestCase, DataBaseTestsMixin):

    def test_function_retuns_correct_value(self):
        result = main.Guide.query.filter(main.Guide.id.in_([1, 4, 7])).all()
        self.assertTrue(
            len(result) == 0,
            "%@Проверьте, что удалили из базы гидов с id=1,4,7,")


if __name__ == "__main__":
    unittest.main()
