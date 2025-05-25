from flask import request, json, redirect, render_template, Flask

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def home():
    return "welcome to my flask app"

if __name__ == "__main__":
    app.run()