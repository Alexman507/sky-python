import logging
from flask import Flask, send_from_directory

from main.views import main_blueprint
from loader.views import loader_blueprint
import loggers


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config["POST_PATH"] = "data/posts.json"
app.config["UPLOAD_FOLDER"] = "uploads/images"

loggers.create_logger()

logger = logging.getLogger("basic")

# @app.route("/")
# def page_index():
#     pass
#
#
# @app.route("/list")
# def page_tag():
#     pass
#
#
# @app.route("/post", methods=["GET", "POST"])
# def page_post_form():
#     pass
#
#
# @app.route("/post", methods=["POST"])
# def page_post_upload():
#     pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


logger.info("Приложение запускается")

app.run(debug=True)

