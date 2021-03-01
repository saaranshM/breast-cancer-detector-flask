from tensorflow.keras.models import load_model
import tensorflow as tf
import cv2
import numpy as np
import os

test_dir_path_0 = '8863/0'
test_dir_path_1 = '8863/1'

print(tf.__version__)

model_path = 'breast-cancer-detector.h5'

model = load_model(model_path)
print("Model Loaded!")



# for filename in os.listdir(test_dir_path_1):
#     path = os.path.join(test_dir_path_1,filename)
#     img_to_predict = process_image(path)
#     prediction = model.predict(img_to_predict)
#     print(prediction)




# categories = ["NO_IDC", "IDC"]



# # process_image('cancer.png')
# predict = model.predict([process_image('cancer1.png')])

# print(np.argmax(predict))