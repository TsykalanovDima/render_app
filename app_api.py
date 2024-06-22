from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    if 'name' in data:
        name = data['name']
        return jsonify(message=f'Привет, {name}!')
    else:
        return jsonify(error='Имя не указано'), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
