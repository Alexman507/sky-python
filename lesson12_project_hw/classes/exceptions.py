import logging


class DataSourceBrokenException(Exception):
    """
    Класс для повреждённых файлов
    """
    logger = logging.getLogger("basic")
    logger.error("Файл с данными повреждён")
