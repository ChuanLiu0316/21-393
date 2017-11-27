from flask import Flask
app = Flask(__name__)

place_holder_response = {
    'Panini': 2,
    'Apple': 1,
    'Fish': 2,
    'Cheese Burger': 3,
}

@app.route('/')
def index():
	return place_holder_response
