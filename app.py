#!/bin/python
# coding: utf-8

from flask import Flask, render_template
from watchdog.observers import Observer
from modules.watch import ChangeHandler
from modules.config import Config


app = Flask(__name__)

image_path = "./image_test"
config_path = "./config/config.ini"
config = Config.read_config(config_path)

@app.route("/")
def top():
    return render_template("index.html")

@app.route("/config")
def config():
    return render_template("config.html")

@app.route("/save_config", methods=["POST"])
def save_config():
    return render_template("index.html")


if __name__ == "__main__":
    print("on app")
    change_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(change_handler, image_path, recursive=True)
    observer.start()
    app.run(host="127.0.0.1", port=5000)
