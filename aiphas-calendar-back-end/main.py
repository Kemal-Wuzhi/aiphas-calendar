import uuid
import eventlet
import time
import os
import socket
import json
import threading
from flask_cors import CORS
from flask import (
    Flask,
    current_app,
    config,
    render_template,
    send_from_directory,
    Blueprint,
    jsonify,
    request,
    make_response,
    redirect,
    flash,
    url_for,
    session,
)
import paho.mqtt.client as mqtt
from flask_socketio import SocketIO

eventlet.monkey_patch()
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app)

CORS(app, resources={r"/*": {"origins": "*"}})

# route & feature


@socketio.on("/main", methods=["GET"])
def get_task():
    for task in Tasks:
        if task["id"] == task_id:
            return task
    return null


# @app.route("/ping", methods=["GET"])
# def ping_pong():
#     return jsonify("pong!")


# def remove_book(book_id):
#     for book in BOOKS:
#         if book["id"] == book_id:
#             BOOKS.remove(book)
#             return True
#     return False


# @app.route("/books", methods=["GET", "POST"])
# def all_books():
#     response_object = {"status": "success"}
#     if request.method == "POST":
#         post_data = request.get_json()
#         BOOKS.append(
#             {
#                 "id": uuid.uuid4().hex,
#                 "title": post_data.get("title"),
#                 "author": post_data.get("author"),
#                 "read": post_data.get("read"),
#             }
#         )
#         response_object["message"] = "Book added!"
#     else:
#         response_object["books"] = BOOKS
#     return jsonify(response_object)


# @app.route("/books/<book_id>", methods=["PUT", "DELETE"])
# def single_book(book_id):
#     response_object = {"status": "success"}
#     if request.method == "PUT":
#         post_data = request.get_json()
#         remove_book(book_id)
#         BOOKS.append(
#             {
#                 "id": uuid.uuid4().hex,
#                 "title": post_data.get("title"),
#                 "author": post_data.get("author"),
#                 "read": post_data.get("read"),
#             }
#         )
#         response_object["message"] = "Book updated!"
#     if request.method == "DELETE":
#         remove_book(book_id)
#         response_object["message"] = "Book removed!"
#     return jsonify(response_object)


# if __name__ == "__main__":
    app.run()
