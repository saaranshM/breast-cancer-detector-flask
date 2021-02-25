from flask import Flask, request, jsonify,abort,Response
import os
import numpy as np
import cv2
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.models import load_model

UPLOAD_FOLDER = 'D:\Tensorflow-files\Projects\BreastCancerDetectoreFlask\static'

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

MODEL_PATH = 'breast-cancer-detector.h5'


def model_load():
    print("Model Loaded!")
    return load_model(MODEL_PATH)


def process_image(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE,IMG_SIZE,3)

@app.route('/', methods=['POST', 'GET'])
def predict():
    if request.method == "POST":
        model = model_load()
        if not model:
            abort(500)
        image_file = request.files['image']
        if image_file:
            if not os.path.exists(UPLOAD_FOLDER): os.mkdir(UPLOAD_FOLDER)
            image_location = os.path.join(
                UPLOAD_FOLDER,
                image_file.filename
            )
            image_file.save(image_location)
            image_to_predict = process_image(image_location)
            predcition = model.predict([image_to_predict]).tolist()
            data = {
                'title': 'Upload New File!',
                'prediction': predcition[0],
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
