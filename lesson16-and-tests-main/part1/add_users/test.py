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

TABLE_NAME = 'user'


class CourseTestCase(SkyproTestCase, DataBaseTestsMixin):

    def setUp(self):
        student_db = main.db
        author_db = solution.db
        self.student_session = student_db.session()
        self.author_session = author_db.session()

    def test_all_rows_added(self):
        query = f"SELECT * FROM {TABLE_NAME}"
        student_rows_count = len(self.student_session.execute(
            query).fetchall())
        author_rows_count = len(self.author_session.execute(
            query).fetchall())
        self.assertLessEqual(
            student_rows_count,
            author_rows_count,
            ("%@Проверьте, что не включили в таблицу ничего лишнего. "
             f"В вашей таблице {student_rows_count} строк, "
             f"тогда как должно быть {author_rows_count} строк"))
        self.assertGreaterEqual(
            student_rows_count,
            author_rows_count,
            ("%@Проверьте, что включили все записи. "
             f"В вашей таблице {student_rows_count} строк, "
             f"тогда как должно быть {author_rows_count} строк"))

    def test_records_is_correct(self):
        users = [
            'Людмила Новикова',
            'Андрей Васечкин',
            'Георги Беридзе',
            'Оксана Ласкина',
            'Иван Горячий'
        ]
        for user in users:
            query = f"SELECT * FROM {TABLE_NAME} WHERE full_name='{user}'"
            self.assertEqual(
                self.student_session.execute(query).fetchall(),
                self.author_session.execute(query).fetchall(),
                f"%@Проверьте, что правильно внесли сведения про {user}")


if __name__ == "__main__":
    unittest.main()
