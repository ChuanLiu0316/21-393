from flask import Flask, request
import json
from flask import send_from_directory, send_file
from server.model.solver import *

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

@app.route('/calculate', methods=['POST'])
def calculate():
    A = json.loads(request.data)

    try: 
        S = Solver(A['height'], A['weight'], A['age'], 'male', A['activity'], A['allergy'])
    except Exception as e:
        print e

    print "ok here2"
    S.run_2()
    if S.result <= -1:
        return json.dumps([])
    else:
        return json.dumps(S.need_food)
	#return None	

	#return json.dumps(place_holder_response)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)

