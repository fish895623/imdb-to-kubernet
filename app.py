#!/usr/bin/env python3
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


@app.route("/")
def aaaa():
    return render_template("index.html")


@app.route("/api", methods=["POST", "GET"])
def my_form_post():
    json_data = request.json
    print(json_data["a_key"])
    return jsonify(json_data)


@app.route("/ff", methods=["GET"])
def starting_url():
    json_data = request.json
    a_value = json_data["a_key"]
    return "JSON value sent: " + a_value


@app.route("/test")
def imdb():
    value = ""
    return render_template("imdb.html", value=value)


@app.route("/test", methods=["POST"])
def ffffaa():
    imdb_input = request.form["imdb_input"]
    return render_template("imdb.html", result=imdb_input, imdb_input=imdb_input)


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
