from flask import Flask, request, jsonify
import time
app = Flask(__name__)
start_time = time.time()
logs = []

@app.route('/add', methods=['GET'])
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a + b
        logs.append(f"Addition of {a} and {b} is {result}")
        return jsonify(result=result)
    except ValueError:
        return jsonify(error="invalid input"), 400

@app.route('/subtract', methods=['GET'])
def subtract():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a - b
        logs.append(f"Subtraction of {a} and {b} is {result}")
        return jsonify(result=result)
    except ValueError:
        return jsonify(error="invalid input"), 400

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        result = a * b
        logs.append(f"Multiplication of {a} and {b} is {result}")
        return jsonify(result=result)
    except ValueError:
        return jsonify(error="invalid input"), 400

@app.route('/divide', methods=['GET'])
def divide():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
        if b == 0:
            return jsonify(error="Division by zero is not allowed"), 400
        result = a / b
        logs.append(f"Division of {a} and {b} is {result}")
        return jsonify(result=result)
    except ValueError: 
        return jsonify(error="invalid input"), 400

@app.route('/logs', methods=['GET'])
def history_function():
    return jsonify(logs)

@app.route('/healthz', methods=['GET'])
def health():
    try:
        return jsonify(uptime=time.time() - start_time)
    except ValueError:
        return jsonify(error=str("Error")), 400
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)