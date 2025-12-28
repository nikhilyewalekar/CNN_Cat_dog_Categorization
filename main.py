from flask import Flask, request, render_template
import os
from src.utils import CNNCatDogClassification

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/uploadImage", methods=["POST"])
def uploadImage():
    file = request.files['image_file']
    file_name = os.path.join('upload', file.filename)
    file.save(file_name)
    obj = CNNCatDogClassification()
    result = obj.predict_cateory(file_name)
    print(result)
    if os.path.exists(file_name):
        os.remove(file_name)
    return f"{result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
