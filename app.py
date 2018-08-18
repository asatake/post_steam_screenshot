#!/bin/python
# coding: utf-8

from flask import Flask

app = Flask(__name__)

@app.route("/")
def top():
    return "Tweet Steam screenshot tool"

if __name__ == "__main__":
    print("on app")
    app.run(host="127.0.0.1", port=5000)
