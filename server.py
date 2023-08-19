from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Hello world!"

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.json
    if 'first' in data and 'second' in data:
        first = data['first']
        second = data['second']
        result = first + second
        response = {'result': result}
        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid input format'})

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.json
    if 'first' in data and 'second' in data:
        first = data['first']
        second = data['second']
        result = first - second
        response = {'result': result}
        return jsonify(response)
    else:
        return jsonify({'error': 'Invalid input format'})

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')

