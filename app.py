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


@app.route("/test")
def imdb():
    value = ""
    return render_template("imdb.html", value=value)


@app.route("/test", methods=["POST"])
def imdb_post():
    a0 = request.form["a0"]
    a1 = request.form["a1"]
    result = int(a0) + int(a1)
    return render_template("imdb.html", result=result, a0=a0, a1=a1)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
