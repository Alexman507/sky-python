import sqlite3
import sqlalchemy
import unittest

class DataBaseTestsMixin:
    """
    Includes methods for Tests with DB Models and Queries
    """
    STRING = 'String'
    INTEGER = 'Integer'
    DATE = 'Date'

    def get_query_info(self, query):
        from_sql_checker = self._sql_checker(query)
        from_cursor = self._get_cursor_info(query)
        return {"query_info": from_sql_checker,
                "cursor_info": from_cursor}

    def _get_db_cursor(self, query):
        con = sqlite3.connect("../netflix.db")
        cur = con.cursor()
        cur.execute(query)
        return cur

    def _get_cursor_info(self, query):
        """
        Creates dict with info from SQL query string
        """
        cur = self._get_db_cursor(query)
        return self.get_cursor_info(cur)

    def get_cursor_info(self, cursor):
        """
        Returns dict with info about current cursor with query
        """
        columns = cursor.description
        columns_len = len(columns)
        names_of_columns = []
        query_result = cursor.fetchall()
        rows_count = len(query_result)
        for name in columns:
            names_of_columns.append(name[0])
        return {"columns": names_of_columns,
                "columns_count": columns_len,
                "query_result": query_result,
                "rows_count": rows_count}

    def _sql_checker(self, query: str):
        query = query.lower()
        keywords = self._get_key_words(query)
        select_ind = query.find('select ')
        from_ind = query.find('from ')
        where_ind = query.find('where ')
        and_ind = query.find(' and ')
        select_block = query[select_ind:from_ind]
        from_block = query[from_ind:where_ind]
        where_block = query[where_ind:]
        and_block = None
        if and_ind:
            where_block = query[where_ind:and_ind]
            and_block = query[and_ind:]
        blocks = {'колонка': select_block,
                  'таблица': from_block,
                  'условие': where_block,
                  'доп условие': and_block}
        for key, value in blocks.items():
            blocks[key] = self._cleaner(blocks[key])
        blocks['keywords'] = keywords
        return blocks

    def _cleaner(self, lst):
        lst = lst.split(' ')
        key_words = ['select', 'from', 'where', 'like', 'distinct', 'and', '']
        for value in key_words:
            if value in lst:
                lst.remove(value)
        for value in lst:
            if ',' in value:
                devided_value = value.split(',')
                try:
                    devided_value.remove('')
                except:  # noqa: E722
                    pass
                lst.remove(value)
                lst += devided_value
        return lst

    def _get_key_words(self, query):
        keywords = ['select', 'from', 'where', 'like',
                    'group by', 'distinct', 'limit', 'order by']
        lst = []
        for keyword in keywords:
            if keyword in query:
                lst.append(keyword)
        return lst

    def field_name_checker(self, student_columns, author_columns):
        self.assertEqual(student_columns, author_columns,
                 (r'%@Проверьте, что правильно определили '
                  'поля модели Author. '
                  f'Вы выбрали {student_columns}, тогда '
                  f'как необходимо {author_columns}'))

    def field_type_checker(
            self,
            module = None,
            model_name: str =None, 
            type_name: str = None,
            fields = None):  # field.name (field.name, field.name)
            correct_field_type = getattr(sqlalchemy, type_name)
            model = getattr(module, model_name)
            fields = (getattr(model, field_name) for field_name in fields)
            for field in fields:
                name = field.property.key
                self.assertTrue(
                    isinstance(field.type, correct_field_type),
                    f"%@Проверьте имеет ли поле {name} модели {model_name} "
                    f"тип {type_name}")

class ResponseTestsMixin:
    
    def _required_args_checker(self, *args, **kwargs):
        for test_arg in args:  # required args
            if not kwargs.get(test_arg):
                raise ValueError(
                    f"key argument '{test_arg}' in TestCase"
                     "function <check status code> must be defined")

    def check_status_code_jsonify_and_expected(self: unittest.TestCase, **kwargs):
        """
        compex check that testing:
        - response status code
        - is_json type
        - expected_obj (if arg expected is not None)
        """
        code: list = kwargs.get('code')
        url: str = kwargs.get('url')
        response = kwargs.get('response')
        expected: object = kwargs.get('expected')
        method: str = kwargs.get('method')
        self._required_args_checker('url', 'response', **kwargs)
        code = kwargs.get('code')
        url = kwargs.get('url')
        response = kwargs.get('response')
        if code:
            self.assertIn(
                response.status_code, code,
                (f"%@Проверьте, что адрес {url} доступен, а {method}-запрос "
                f"возвращает код {code}"))
        else:
            self.assertNotIn(
                response.status_code, [404, 500],
                (f"%@Кажется, на сервере произошла ошибка."
                 f"Проверьте, что адрес {url} доступен."))
            self.assertNotIn(
                response.status_code, [405],
                (f"%@Проверьте, что при {method}-запросе на адрес "
                f"{url} используется правильный http-метод"))
        self.assertTrue(
            response.is_json,
            (f"%@Проверьте, что в ответ на {method}-запрос "
             f"по адресу {url} возращает данные в формате json."
             " Попробуйте использовать функцию jsonify из библиотеки flask."))
        if expected:
            data = response.json
            self.assertTrue(
                isinstance(data, expected),
                f"%@Проверьте что в ответ на {method}-запрос по адресу {url}"
                f"возвращается {expected}"
            )
        else:
            self.assertEqual(
                response.json, '',
                f"%@Проверьте что в ответ на {method}-запрос по адресу {url}"
                f" возвращается пустое значение."
            )
    
    def compare_result_fields_with_author_solution(
        self,
        many=False,
        **kwargs):
        """
        Compare student response.data with author sulution.
        Note:* (response.data must be not None)
        use `many=true` for inspecting response.data which contains list
        """
        self._required_args_checker(
            'method', 
            'url', 
            'student_response',
            'author_response',
            **kwargs)
        method = kwargs.get('method')
        url = kwargs.get('url')
        student_response = kwargs.get('student_response').json
        author_response = kwargs.get('author_response').json
        if not many and isinstance(author_response, list):
            raise ValueError('check `response.data` maybe many arg must have True value')
        if many:
            author_data = author_response[0]
            data = student_response[0]
        else:
            author_data = author_response
            data = student_response
        student_keys = data.keys()
        for key, value in author_data.items():
            self.assertIn(
                key,
                student_keys,
                f"%@ Проверьте, что ответ на {method}-запрос по адресу {url} "
                f"содержит поле {key}")
            self.assertEqual(
                value,
                data[key],
                f"%@ Проверьте, что ответ на {method}-запрос по адресу {url} "
                f"в поле {key} содержится правильное значение")
