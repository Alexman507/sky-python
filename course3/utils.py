import json

from config import DATA_PATH, COMMENTS_PATH


def get_posts_all(path=DATA_PATH):
    """возвращает посты"""
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_posts_by_user(user_name):
    """
    возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError`
    если такого пользователя нет и пустой список, если у пользователя нет постов.
    """
    count_of_posts = []
    posts = get_posts_all()
    for post in posts:
        if user_name in post["name"].lower():
            count_of_posts.append(post)
    if count_of_posts:
        return count_of_posts
    raise ValueError("Такого пользователя нет в списке")


def get_comments_by_post_id(post_id):
    """
    возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError`,
     если такого поста нет и пустой список, если у поста нет комментов.
     """
    posts = get_posts_all(COMMENTS_PATH)
    count_of_posts = []
    for post in posts:
        if post["post_id"] == post_id:
            count_of_posts.append(post)
    if count_of_posts:
        return count_of_posts
    raise ValueError("Такого поста нет в списке")


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    count_of_posts = []
    posts = get_posts_all()
    for post in posts:
        if query.lower() in post["content"].lower():
            count_of_posts.append(post)
    if count_of_posts:
        return count_of_posts
    raise ValueError(f'По вашему запросу "{query}" ничего не нашлось. Попробуйте поискать пост вручную')


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору."""
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == pk:
            return post
