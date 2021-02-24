from flask import Flask, request, jsonify
from PIL import Image
import base64
import io
import numpy as np
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from tensorflow.keras.models import load_model

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    data = {
        'title': 'Upload New File!',
        'prediction': 0,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
