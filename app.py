from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/about")
def about():
    return "Sobre"

if __name__ == "__main__":
    app.run()