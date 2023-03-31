from flask import Flask, send_from_directory
from main.main import main
from loader.loader import loader

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main)

app.register_blueprint(loader)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
