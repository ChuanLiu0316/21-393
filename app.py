from flask import Flask, request
import json
from flask import send_from_directory, send_file
app = Flask(__name__)

place_holder_response = {
    'Panini': 2,
    'Apple': 1,
    'Fish': 2,
    'Cheese Burger': 3,
}

@app.route('/')
def index():
	root = app.config.get('STATIC_ROOT', '')
	print root
	return send_file(root+'frontend/' + 'index.html')


@app.route('/<path:path>')
def serve_file(path):
	root = app.config.get('STATIC_ROOT', '')
	return send_file(root+'frontend/'+path)

@app.route('/js/')
def js():
	return app.send_static_file('index.js')

@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
	if request.method == 'POST':
		A = request.data 
		print A
	return json.dumps(place_holder_response)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

