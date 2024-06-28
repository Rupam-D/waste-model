# /3.9.12
from flask import Flask,request,jsonify

from tensorflow.keras.models import load_model 
 # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

import requests
from io import BytesIO
import urllib.request


app = Flask(__name__)

@app.route("/test")
def test():
  
  url="https://images-cdn.ubuy.co.in/633b90c0422c88091236e232-bantalan-lembar-isi-kardus-bergelombang.jpg"
  response=urllib.request.urlopen(url)

  return "testing"

if __name__ == '__main__':
    app.run(debug=True)