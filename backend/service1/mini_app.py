from flask import Flask, jsonify
import random
from waitress import serve

app = Flask(__name__)

@app.route('/random_number', methods=['GET'])
def generate_random_number():
    random_number = random.randint(1, 100)
    return jsonify({'random_number': random_number})

if __name__ == '__main__':
    serve(app, host='0.0.0.0' , port=8080)
