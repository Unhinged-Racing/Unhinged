from flask import Flask, request, send_from_directory
import os

app = Flask(__name__, static_url_path='/static')
UPLOAD_FOLDER = 'static'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('static', 'viewer.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No image part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    file.save(os.path.join(UPLOAD_FOLDER, 'latest.jpg'))
    return 'OK'

@app.route('/latest.jpg')
def latest_image():
    return send_from_directory(UPLOAD_FOLDER, 'latest.jpg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
