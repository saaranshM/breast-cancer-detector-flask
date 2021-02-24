from flask import Flask, request, jsonify
from PIL import Image
import base64
import io
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array
from tensorflow.keras.models import load_model

app = Flask(__name__)

def get_model():
    global model
    model = load_model('breast-cancer-detector.h5')
    print('Model Loaded!')

def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)

    return image

print("Loading Model!")
get_model()

@app.route("/predict", methods=["POST"])
def predict():
    print('predict')
    message = request.get_json(force=True)
    print(message)
    encoded = message['image']
    print(encoded)
    decoded = base64.b64encode(encoded)
    image = Image.open(io.BytesIO(decoded))
    processed_image = preprocess_image(image, target_size=(50,50))

    prediction = model.preict(processed_image).toList()

    response = {
        'prediction': {
            "Yes": prediction[0][0],
            "No": prediction[0][1]
        }
    }

    return jsonify(response)
