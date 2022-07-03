import unittest
import main
import solution
from tools import SkyproTestCase


class WherePlays2TestCase(SkyproTestCase):
    def setUp(self):
        self.student_query = self.get_query_info(main.sqlite_query)
        self.author_query = self.get_query_info(solution.sqlite_query)

    def test_query_structure_has_like_operator(self):
        self.assertRegex(main.sqlite_query, r".[Ll][Ii][Kk][Ee]",
                         (r'%@Проверьте, что воспользовались оператором like'
                          ' при составлении запроса'))

    def test_is_artist_in_query(self):
        self.assertRegex(main.sqlite_query, ".%Joaquin Phoenix%",
                         (r'%@Проверьте, что правильно указали артиста'
                          ' в условиях запроса'))

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


if __name__ == "__main__":
    unittest.main()
