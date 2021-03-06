# Flask API
# Back-end code

import os
import cv2
from flask import Flask, request, jsonify, redirect
from Predict_From_Trained_Model import *
from flask_cors import CORS, cross_origin # Allows Cross Origin Resource Sharing
from PIL import Image
import base64

# Initialize a flask object
app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'

# Translate page route:
@app.route('/translate', methods=['POST'])
# ADD ORIGIN OF THE FRONT END
# For deployment origin: http://signtext.ue.r.appspot.com/translate
@cross_origin(origin = 'http://localhost:3000/translate')
def recieve_image():

    data_string = request.form['image']
    # data_string form: <str>: 'data:image/png;base64,base64 encoding itself'
    # Get substring, disregarding the first 21 positions
    img_string = data_string[22:]
    img = base64.b64decode(img_string)

    # Save the image & its path name
    img_file_name = "image.png"
    with open(img_file_name, 'wb') as f:
        f.write(img)
    cur_path = os.getcwd()
    img_path = cur_path + "/image.png"

    # Pass the path to the predictor function & return a prediction
    prediction = get_prediction(img_path)
    return jsonify(prediction)

# app.run()
if __name__ == '__main__':
    app.run()
