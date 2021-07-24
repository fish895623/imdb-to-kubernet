from flask import Flask, render_template, request

from Transformer import predict, transformer, model
from Transformer import VOCAB_SIZE, NUM_LAYERS, DFF, D_MODEL, NUM_HEADS, DROPOUT

model = transformer(
    vocab_size=VOCAB_SIZE,
    num_layers=NUM_LAYERS,
    dff=DFF,
    d_model=D_MODEL,
    num_heads=NUM_HEADS,
    dropout=DROPOUT,
)
model.load_weights("best_model.h5")

app = Flask(__name__)

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
    app.run(host="0.0.0.0", port="5000")
