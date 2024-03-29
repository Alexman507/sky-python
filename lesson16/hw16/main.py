import json
# timecode 1:35:26
from flask import request

from config import app
from lesson16.hw16.models import Order, User, Offer
from lesson16.hw16.service import init_db, get_all, get_by_id, insert_data_user


@app.route("/users", methods=["GET", "POST"])
def get_users_app():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps(get_all(User), indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    elif request.method == 'POST':
        if isinstance(request.json, list):
            insert_data_user(request.json)
        elif isinstance(request.json, dict):
            insert_data_user(request.json)
        else:
            print('Непонятный тип данных')

        return app.response_class(
            response=json.dumps(request.json, indent=4, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )



@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id_app(user_id):
    data = get_by_id(User, user_id)

    return app.response_class(
        response=json.dumps(data, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.route("/orders", methods=["GET"])
def get_orders_app():
    return app.response_class(
        response=json.dumps(get_all(Order), indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.route("/orders/<int:order_id>", methods=["GET"])
def get_order_by_id_app(order_id):
    data = get_by_id(Order, order_id)

    return app.response_class(
        response=json.dumps(data, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.route("/offers", methods=["GET"])
def get_offers_app():
    return app.response_class(
        response=json.dumps(get_all(Offer), indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


@app.route("/offers/<int:user_id>", methods=["GET"])
def get_order_by_id_app(user_id):
    data = get_by_id(Offer, user_id)

    return app.response_class(
        response=json.dumps(data, indent=4, ensure_ascii=False),
        status=200,
        mimetype="application/json"
    )


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=8080, debug=True)
