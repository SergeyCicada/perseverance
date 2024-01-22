from flask import Flask, render_template, request
import logging

from functions.function_send_mail import send_email
from functions.function_for_api import *
from config import API_KEY

logging.basicConfig(filename="logs.log")

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/rover/")
def photos_rover():
    try:
        photos_rover = get_photos_rover(API_KEY)
        return render_template("rover.html", photos_rover=photos_rover)
    except Exception:
        return render_template("error.html")


@app.route("/space/")
def photos_space():
    try:
        photos_space = get_photos_space(API_KEY)
        return render_template("space.html", photos_space=photos_space)
    except Exception:
        return render_template("error.html")


@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")


@app.route("/message/")
def send_message():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    message = request.args.get('text')

    string_send = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    send_email(string_send)
    return render_template("thank_message.html")


if __name__ == "__main__":
    app.run(debug=True)
