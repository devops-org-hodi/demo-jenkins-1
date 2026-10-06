from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify(ping="pong")

if __name__ == "__main__":
    app.run(debug=True, port=5000)