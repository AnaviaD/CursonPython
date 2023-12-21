from flask import Flask, request, Response, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Home"


if __name__ == '__main__':
    app.run(debug=True)