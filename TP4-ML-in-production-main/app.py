from flask import Flask, render_template, request
from flask.json import jsonify
from keras.models import load_model
import ast
import numpy as np

app = Flask(__name__)

# Model ML

loaded_model = load_model('./model/fashion_mnist_model.h5')

class_labels = {0: 'T-shirt/top',
                1: 'Trouser',
                2: 'Pullover',
                3: 'Dress',
                4: 'Coat',
                5: 'Sandal',
                6: 'Shirt',
                7: 'Sneaker',
                8: 'Bag',
                9: 'Ankle boot'}

# Routes

@app.route('/')
def index():
    return render_template('home.html')

@app.route("/api/hello/<name>")
def hello_name(name):
    """
    Return a hello message with name
    """
    return jsonify({"hello": name})


@app.route('/classify/<path:array>', methods=['GET', 'POST'])
def classify(array):
    image = ast.literal_eval(array)


    image = np.array(image, dtype=np.float32)
    image = image.reshape(1, 28, 28, 1)
    image = image.astype("float32")
    image = image / 255

    prediction = loaded_model.predict(image)
    label = int(np.argmax(prediction))
    return jsonify({"prediction": label, 'label': class_labels[label]})

if __name__ == "__main__":
    app.run(debug=True)