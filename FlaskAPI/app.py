import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np
from dummy import data_in

app = Flask(__name__)


def load_models():
    with open("models/model.pickle", "rb") as f:
        clf = pickle.load(f)

    return clf


@app.route("/predict", methods=["GET"])
def predict():
    request_json = request.get_json()
    x = request_json["input"]
    x_in = np.array(x).reshape(1, -1)
    # x = np.array(data_in).reshape(1, -1)

    clf = load_models()
    result = clf.predict(x_in)[0]
    response = json.dumps({"response": result})

    return response, 200


if __name__ == "__main__":
    application.run(debug=True)
