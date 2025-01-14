from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "欢迎来到我的Flask应用程序！"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return jsonify(message=f"你好, {name}!")

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify(received_data=data), 200

if __name__ == '__main__':
    app.run(debug=True)
