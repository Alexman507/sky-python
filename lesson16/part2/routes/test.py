import sys
import unittest
import os
from pathlib import Path
from guides_sql import CREATE_TABLE, INSERT_VALUES
from sqlalchemy import text
import main
import solution

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))

from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import ResponseTestsMixin  # noqa: E402


class RoutesTestCase(SkyproTestCase, ResponseTestsMixin):

    @classmethod
    def setUpClass(cls):
        cls.instance_to_create = {
            "surname": "Иванов",
            "full_name": "Иван Иванов",
            "tours_count": 7,
            "bio": "Провожу экскурсии по крышам СПб",
            "is_pro": True,
            "company": "Удивительные экскурсии"
        }

    def setUp(self):
        self.app = main.app.test_client()
        self.db = main.db
        self.db.drop_all()
        with self.db.session.begin():
            self.db.session.execute(text(CREATE_TABLE))
            self.db.session.execute(text(INSERT_VALUES))
        self.author_app = solution.app.test_client()
        self.author_db = solution.db
        self.author_db.drop_all()
        with self.db.session.begin():
            self.author_db.session.execute(text(CREATE_TABLE))
            self.author_db.session.execute(text(INSERT_VALUES))

    def test_get_method_is_available_and_works_correct(self):
        url = '/guides'
        response = self.app.get(url)
        method = 'GET'
        author_response = self.author_app.get(url)

        self.check_status_code_jsonify_and_expected(
            url=url,
            response=response,
            method=method,
            expected=list)

        data = response.json
        self.assertEqual(
            len(data), 10,
            f"%@Проверьте, что в ответ на {method}-запрос по адресу {url} "
            "возвращаются все объекты")

        self.compare_result_fields_with_author_solution(
            many=True,
            method=method,
            url=url,
            author_response=author_response,
            student_response=response)

    def test_get_filter_method_is_available_and_works_correct(self):
        tours_count = 1
        filter_value = 'tours_count'
        url = f'/guides?{filter_value}={tours_count}'
        response = self.app.get(url)
        author_response = self.author_app.get(url)
        method = 'GET'

        self.check_status_code_jsonify_and_expected(
            url=url,
            response=response,
            method=method,
            expected=list)

        data = response.json
        for instance in data:
            self.assertEqual(
                instance[filter_value], tours_count,
                f"%@Проверьте что ответ на {method}-запрос по адресу {url} "
                "отфильтрован верно")

        self.compare_result_fields_with_author_solution(
            method=method,
            url=url,
            author_response=author_response,
            student_response=response,
            many=True)

    def test_get_id_method_is_available_and_works_correct(self):
        url = '/guides/1'
        response = self.app.get(url)
        author_response = self.author_app.get(url)
        method = 'GET'

        self.check_status_code_jsonify_and_expected(
            url=url,
            response=response,
            method=method,
            expected=dict)

        self.compare_result_fields_with_author_solution(
            method=method,
            url=url,
            author_response=author_response,
            student_response=response)

    def test_delete_method_is_available_and_works_correct(self):
        url = '/guides/1/delete'
        response = self.app.get(url)
        method = 'GET'

        self.check_status_code_jsonify_and_expected(
            url=url,
            response=response,
            method=method,
            expected=None)

        result = self.db.session.execute(
            text('select * from guide where id=1')).fetchall()
        self.assertTrue(
            result == [],
            f"%@Проверьте что {method}-запрос на адрес {url} "
            " удаляет запись из базы данных"
        )

    def test_create_method_is_available_and_works_correct(self):
        url = '/guides'
        instance_data = self.instance_to_create
        response = self.app.post(url, json=instance_data)
        author_response = self.author_app.post(url, json=instance_data)
        method = 'POST'

        self.check_status_code_jsonify_and_expected(
            url=url,
            response=response,
            method=method,
            expected=dict)

        self.compare_result_fields_with_author_solution(
            method=method,
            url=url,
            author_response=author_response,
            student_response=response)

        result = self.db.session.execute(
            text('select * from guide where id=11')).fetchall()
        self.assertTrue(
            result != [],
            f"%@Проверьте что {method}-запрос на адрес {url} "
            " создаёт запись из базы данных"
        )

    def tearDown(self):
        self.db.session.close()
        self.author_db.session.close()


if __name__ == "__main__":
    unittest.main()
