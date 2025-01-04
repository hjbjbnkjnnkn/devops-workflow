from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/status/verify', methods=['GET'])
def status_verify():
    return jsonify({"status": "Running smoothly"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
