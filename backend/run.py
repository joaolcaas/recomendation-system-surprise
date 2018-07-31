from app import create_app

SERVER_URL = "localhost"
SERVER_PORT = 8080

if(__name__ == "__main__"):
	create_app().run(host=SERVER_URL, port=SERVER_PORT, debug=True, threaded=True)