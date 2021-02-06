from flask import (
	Flask, 
	render_template, 
	send_from_directory
)

import os

app = Flask(__name__, template_folder="website\\templates", static_folder="website\\static")

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/<path:path>')
def loadFiles(path):
	return os.listdir("files/" + path)

if __name__ == '__main__':
	app.run(debug=True)