import unittest
import main
import solution
from tools import SkyproTestCase


class CountryTestCase(SkyproTestCase):
    def setUp(self):
        self.student_query = self.get_query_info(main.sqlite_query)
        self.author_query = self.get_query_info(solution.sqlite_query)

    def test_query_columns_is_correct(self):
        student_columns = self.student_query.get('cursor_info').get('columns')
        author_columns = self.author_query.get('cursor_info').get('columns')
        self.assertEqual(student_columns, author_columns,
                         (r'%@Проверьте, что правильно выбрали'
                          ' колонку в базе данных. '
                          f'Вы выбрали {student_columns}, тогда '
                          f'как необходимо {author_columns}'))

    def test_rows_count_superfluous_condition(self):
        count = self.student_query.get('cursor_info').get('rows_count')
        author_count = self.author_query.get('cursor_info').get('rows_count')
        self.assertFalse(count > author_count,
                         (r'%@Кажется, в запросе имеется лишнее условие.'
                          f'Выводится больше строк ({count}) '
                          f'чем предполагалось {author_count}'))

    def test_rows_count_lack_condition(self):
        count = self.student_query.get('cursor_info').get('rows_count')
        author_count = self.author_query.get('cursor_info').get('rows_count')
        self.assertFalse(count < author_count,
                         (r'%@Кажется, в запросе нехватает условия.'
                          f'Выводится меньше строк ({count}) '
                          f'чем предполагалось {author_count}'))

    def test_rows_is_ascending(self):
        student_result = self.student_query.get('cursor_info').get("query_result")
        self.assertTrue(
            student_result[0][0] == "United States",
            "%@Убедитесь верно ли отсортированы строки и правильно ли выбран порядок расположения колонок таблицы"
        )


if __name__ == "__main__":
    unittest.main()
