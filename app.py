from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def get_numbers():
    data = request.get_json()
    a = float(data['a'])
    b = float(data['b'])
    return a, b


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['POST'])
def add():
    try:
        a, b = get_numbers()
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'некорректные числа'}), 400
    return jsonify({'result': a + b})


@app.route('/subtract', methods=['POST'])
def subtract():
    try:
        a, b = get_numbers()
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'некорректные числа'}), 400
    return jsonify({'result': a - b})


@app.route('/multiply', methods=['POST'])
def multiply():
    try:
        a, b = get_numbers()
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'некорректные числа'}), 400
    return jsonify({'result': a * b})


@app.route('/divide', methods=['POST'])
def divide():
    try:
        a, b = get_numbers()
    except (KeyError, ValueError, TypeError):
        return jsonify({'error': 'некорректные числа'}), 400
    if b == 0:
        return jsonify({'error': 'на ноль делить нельзя'}), 400
    return jsonify({'result': a / b})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
