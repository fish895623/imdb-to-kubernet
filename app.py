from flask import Flask, render_template, request

from IrisWeb import detect_iris

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/iris")
def iris():
    return render_template("iris.html")


@app.route("/iris", methods=["POST"])
def iris_post():
    a0 = request.form["a0"]
    a1 = request.form["a1"]
    a2 = request.form["a2"]
    a3 = request.form["a3"]
    result = detect_iris(float(a0), float(a1), float(a2), float(a3))
    return render_template("iris.html", a0=a0, a1=a1, a2=a2, a3=a3, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="80")
