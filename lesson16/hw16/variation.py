# Роут, если логику хотим разгрузить с базы

# @app.route("/users/<int:user_id>", methods=["GET"])
# def get_user_by_id(user_id):
#     data = get_all_users()
#     for row in data:
#         if user_id == row.get("id"):
#             return app.response_class(
#                 response=json.dumps(data, indent=4),
#                 status=200,
#                 mimetype="application/json"
#             )
#     return app.response_class(
#         response=json.dumps({}, indent=4),
#         status=200,
#         mimetype="application/json"
