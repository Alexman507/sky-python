import sys
import unittest
import os
from pathlib import Path

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
        self.app = main.app.test_client()
        self.guides = self.app.get('/guides')
        self.guide_id = self.app.get('/guides/3')
        self.author_app = solution.app.test_client()
        self.author_guides = self.author_app.get('/guides')
        self.author_guide_id = self.author_app.get('/guides/3')

    def test_guides_page_is_available(self):
        self.assertEqual(
            self.guides.status_code, 200,
            "%@Проверьте, что адрес '/guides' доступен")

    def test_guide_id_page_is_available(self):
        self.assertEqual(
            self.guide_id.status_code, 200,
            "%@Проверьте, что адрес '/guides/<int:id>' доступен")

    def test_guides_page_returns_json(self):
        self.assertTrue(
            self.guides.is_json,
            ("%@Проверьте что при запросе на страницу '/guides'"
             " данные возвращаются в формате json, попробуйте "
             " использовать функцию jsonify"))

    def test_guide_id_page_returns_json(self):
        self.assertTrue(
            self.guides.is_json,
            ("%@Проверьте что при запросе на страницу '/guides/<int:id>'"
             " данные возвращаются в формате json, попробуйте "
             "использовать функцию jsonify"))

    def test_guides_page_result_is_dict(self):

        self.assertTrue(
            isinstance(self.guides.json, list),
            ('%@Проверьте что при запросе на страницу "/guides" '
             'возвращаемые данные являются словарем'))

    def test_guide_id_page_result_is_dict(self):
        self.assertTrue(
            isinstance(self.guide_id.json, dict),
            ('%@Проверьте что при запросе на страницу "/guides/<int:id>" '
             'возвращаемые данные являются словарём'))

    def test_guides_returns_correct_keys(self):
        author_keys = self.author_guides.json[0].keys()
        student_keys = self.guides.json[0].keys()
        missing_keys = []
        for key in author_keys:
            if key not in student_keys:
                missing_keys.append(key)
        if len(missing_keys) > 0:
            msg = ("%@Проверьте, присутствуют ли в возвращаемых объектах "
                   f" следующие поля: {missing_keys} при обращении по "
                   "адресу '/guides'")
            raise self.failureException(msg)

    def test_guide_id_returns_correct_keys(self):
        author_keys = self.author_guide_id.json.keys()
        student_keys = self.guide_id.json.keys()
        missing_keys = []
        for key in author_keys:
            if key not in student_keys:
                missing_keys.append(key)
        if len(missing_keys) > 0:
            msg = ("%@Проверьте, присутствуют ли в возвращаемом объекте "
                   f" следующие поля: {missing_keys} при обращении по "
                   "адресу '/guides/<int:id>'")
            raise self.failureException(msg)

    def test_guides_returns_correct_values(self):
        student_dict = self.guides.json[0]
        author_items = self.author_guides.json[0].items()
        missing_values = []
        for key, value in author_items:
            if value != student_dict[key]:
                missing_values.append(key)
        if len(missing_values) > 0:
            msg = ("%@Проверьте, правильные ли значения содержатся в "
                   f" следующих полях: {missing_values} при обращении "
                   " по адресу  '/guides'")
            raise self.failureException(msg)

    def test_guide_id_returns_correct_values(self):
        student_dict = self.guide_id.json
        author_items = self.author_guide_id.json.items()
        missing_values = []
        for key, value in author_items:
            if value != student_dict[key]:
                missing_values.append(key)
        if len(missing_values) > 0:
            msg = ("%@Проверьте, правильные ли значения содержатся в "
                   f" следующих полях: {missing_values} при обращении "
                   "по адресу '/guides/<int:id>'")
            raise self.failureException(msg)


if __name__ == "__main__":
    unittest.main()
