from flask import Flask, request, jsonify,abort,Response
import os
import numpy as np
import cv2
from flask_cors import CORS
from tensorflow.keras.models import load_model

UPLOAD_FOLDER = os.getcwd()
UPLOAD_FOLDER = os.path.join(UPLOAD_FOLDER,'static')

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

MODEL_PATH = 'breast-cancer-detector.h5'


def model_load():
    print("Model Loaded!")
    return load_model(MODEL_PATH)

model_load()


def process_image(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE,IMG_SIZE,3)

@app.route('/', methods=['POST', 'GET'])
def predict():
    predcitions = []
    data = {
             'model_predictions': []
        }

    if request.method == "POST":
        model = model_load()
        if not model:
            abort(500)

        if not os.path.exists(UPLOAD_FOLDER): os.mkdir(UPLOAD_FOLDER)
        res = request.files.to_dict(flat=False)
        for image_file in res['images']:
            if image_file:
                image_location = os.path.join(
                    UPLOAD_FOLDER,
                    image_file.name
                )
                image_file.save(image_location)
                image_to_predict = process_image(image_location)
                predcition = int(np.argmax(model.predict([image_to_predict])))
                img_obj = {
                    'name': image_file.filename,
                    'prediction': predcition
                }
                data['model_predictions'].append(img_obj)
                os.remove(image_location)
        print("done")
        return jsonify(data)

if __name__ == '__main__':
    app.run()