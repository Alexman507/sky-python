import json

from flask import Flask

from lesson14.hw14.utils import search_by_title

app = Flask(__name__)


@app.get("/movie/<title>")
def page_index(title):
    result = search_by_title(title)

    return app.response_class(
        response=json.dumps(result, ensure_ascii=False, indent=4),
        status=200,
        mimetype="application/json"

    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
