from flask import Flask, request, jsonify,abort
from PIL import Image
import base64
import io
import os
import numpy as np
import cv2
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from tensorflow.keras.models import load_model

UPLOAD_FOLDER = 'D:\Tensorflow-files\Projects\BreastCancerDetectoreFlask\static'

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

MODEL_PATH = 'breast-cancer-detector.h5'

model = None

def model_load():
    model = load_model(MODEL_PATH)
    if model:
        print("Model Loaded!")
        return True
    else:
        print("Model Loading Failed!")
        return False


def process_image(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE,IMG_SIZE,3)

@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        if not model_load():
            abort(500)
        image_file = request.files['image']
        if image_file:
            if not os.path.exists(UPLOAD_FOLDER): os.mkdir(UPLOAD_FOLDER)
            image_location = os.path.join(
                UPLOAD_FOLDER,
                image_file.filename
            )
            image_file.save(image_location)
            data = {
                'title': 'Upload New File!',
                'prediction': 1,
            }
            print("done")
            return jsonify(data)
    data = {
        'title': 'Upload New File!',
        'prediction': 0,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
