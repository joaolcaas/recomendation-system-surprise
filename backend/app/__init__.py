from flask import Flask
from app.views import main
from flask_cors import CORS

def create_app():
	app = Flask(__name__)
	app.register_blueprint(main.blueprint, url_prefix='/')
	CORS(app)
	return app