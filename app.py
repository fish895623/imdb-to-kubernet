# -*- coding: utf-8 -*-
"""
flask app
"""
from flask import Flask, render_template, request

from Transformer import predict, model

app = Flask(__name__)


@app.route("/transformer")
def transformer():
    """
    초기 html 로드
    """
    return render_template("transformer.html")


@app.route("/transformer", methods=["POST"])
def transformer_post():
    """
    POST data from `/transformer`

    param
        sentence    (str)   : html에서 수신받은 입력값
        result      (str)   : `predict(str(sentence))` transformer를 이용한 예측값
    """
    sentence = request.form["sentence"]
    result = predict(sentence)
    return render_template("transformer.html", sentence=sentence, result=result)


@app.route("/transformer/post", methods=["POST"])
def transformer_post_form():
    """
    POST data from requested `/transformer/post`

    param
        sentence (str) : `sentence` 의 value값
        run (str)      : `predict(str(sentence))` transformer를 이용한 예측값
    """
    sentence = str(request.form["sentence"])
    run = predict(sentence)
    return run


if __name__ == "__main__":
    model.load_weights("best_model.h5")
    app.run(host="0.0.0.0", port="5000")
