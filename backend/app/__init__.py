from flask import Flask
from flask_cors import CORS

app = Flask(__name__,
            template_folder="../../frontend/dist",
            static_folder="../../frontend/dist/static")
CORS(app, resources=r'/*')

from app import routes
