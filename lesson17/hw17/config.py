import os


class Config:

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.getcwd(), 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
