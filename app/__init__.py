"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa8pe7avj5o48e33n0-a.oregon-postgres.render.com",
        database="todo_rfbs",
        user="todo_rfbs_user",
        password="SUaUlRjohBaKoJRjWkBloliwv3mhZlOs")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
