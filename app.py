#!/bin/python
# coding: utf-8

from flask import Flask, render_template
import configparser
import os
import sys


def read_config(config_path):
    confp = configparser.ConfigParser()
    if os.path.exists(config_path):
        confp.read(config_path)
    else:
        confp["PATH"] = {"path": image_path}
        confp["Twitter"] = {
            "key": "",
            "key_secret": "",
            "token": "",
            "token_secret": ""
        }
        confp["Mastodon"] = {
            "client": "",
            "client_secret": "",
            "token": ""
        }
        with open(config_path, "w") as cf:
            confp.write(cf)

    return confp


def parse_config():
    return


def write_config(path):
    return


app = Flask(__name__)

image_path = ""
config_path = "./config/config.ini"
config = read_config(config_path)

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
    app.run(host="127.0.0.1", port=5000)
