from flask import Flask, jsonify
from waitress import serve


app = Flask(__name__)

tasks = [
    {'id': 1, 'task': 'Faire les courses'},
    {'id': 2, 'task': 'Repondre aux e-mails'},
    {'id': 3, 'task': 'Preparer la presentation'},
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    serve(app, host='0.0.0.0' , port=8080)
