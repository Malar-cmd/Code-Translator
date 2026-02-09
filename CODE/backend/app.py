from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from translator import translate_python_to_java
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/style.css")
def style():
    return send_from_directory(FRONTEND_DIR, "style.css")

@app.route("/editor.js")
def editor():
    return send_from_directory(FRONTEND_DIR, "editor.js")

@app.route("/translate", methods=["POST"])
def translate():
    code = request.json["code"]
    return jsonify({
        "java_code": translate_python_to_java(code)
    })

if __name__ == "__main__":
    print("Frontend directory:", FRONTEND_DIR)
    app.run(debug=True)
