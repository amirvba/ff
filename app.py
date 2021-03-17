from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Steffen aus GitHub! um 18:16, from public repository. second try: 18:21"


if __name__ == '__main__':
    app.run(debug=True)
