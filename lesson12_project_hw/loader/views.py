import logging

from flask import Blueprint, render_template, request, current_app

from classes.data_manager import DataManager
from .exceptions import OutOfFreeNamesError, PictureFormatNotSupportedError, PictureNotUploadedError
from .upload_manager import UploadManager

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')
logger = logging.getLogger("basic")


@loader_blueprint.route('/post', methods=['GET'])
def page_form():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])
def page_create_posts():

    path = current_app.config.get('POST_PATH')
    data_manager = DataManager(path)
    upload_manager = UploadManager()

    # Получаем данные
    picture = request.files.get('picture', None)
    content = request.values.get('content', '')

    # Сохранение картинки с помощью менеджера загрузок
    filename_saved = upload_manager.save_with_random_name(picture)

    # Путь для браузера клиента
    web_path = f"/uploads/images/{filename_saved}"

    # Данные для записи в файл
    post = {"pic": web_path, "content": content}

    # Добавляет данные в файл
    data_manager.add(post)

    return render_template('post_uploaded.html', pic=web_path, content=content)


@loader_blueprint.errorhandler(OutOfFreeNamesError)
def error_out_of_free_names(e):
    logger.error("Закончились свободные имена для картинок")
    return "Закончились свободные имена для загрузки картинок, обратитесь к администратору сайта"


@loader_blueprint.errorhandler(PictureFormatNotSupportedError)
def error_format_not_supported(e):
    logger.error("Некорректный формат картинки")
    return "Данный формат картинки не поддерживается, выберите другой"


@loader_blueprint.errorhandler(PictureNotUploadedError)
def error_not_uploaded(e):
    logger.error("Ошибка загрузки картинки")
    return "Не удалось загрузить картинку"
