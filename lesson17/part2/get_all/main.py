# У вас имеется настроенный фласк и словарь с данными.
#
# Вам необходимо:
#
# 1. Создать переменную app c экземпляром
#    класса App из библиотеки flask_restx
#
# 2. Создать неймспейc book_ns с адресом `/books`
#
# 3. Создать Сlass based view который позволяет
#    с помощью GET-запроса по адресу `/books` получить
#    список всех сущностей, определенных в cписке


from flask import Flask

app = Flask(__name__)
app. config['RESTX_JSON'] = {'ensure_ascii': False, 'indent': 2}

api = # TODO допишите код
book_ns = # TODO допишите код

books = [
    {
        "id": 1,
        "name": "Harry Potter",
        "year": 2000,
        "author": "Joan Routing"
    },
    {
        "id": 2,
        "name": "Le Comte de Monte-Cristo",
        "year": 1844,
        "author": "Alexandre Dumas"
    }
]


# TODO напишите Class Based View здесь


# для проверки работоспособности запустите фаил
# и зайдите в браузере на адрес http://127.0.0.1/books

if __name__ == '__main__':
    app.run(debug=False)
