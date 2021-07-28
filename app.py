from flask import Flask, render_template, request

from transformer import predict, transformer, model


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


@app.route("/transformer")
def transformer():
    return render_template("transformer.html")


@app.route("/transformer", methods=["POST"])
def transformer_post():
    a0 = request.form["a0"]
    result = predict(a0)
    return render_template("transformer.html", a0=a0, result=result)


@app.route("/transformer/post", methods=["POST"])
def transformer_POST_form():
    sentence = str(request.form["sentence"])
    run = predict(sentence)
    return run


if __name__ == "__main__":
    model.load_weights("best_model.h5")
    app.run(host="0.0.0.0", port="5000")
