from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE'] = 'sqlite3:///database.db'

db = SQLAlchemy(app)
