from flask import Flask,render_template, request , url_for

app = Flask(__name__)

@app.route("/login")
def login():
    pass

@app.route("/home")
def home():
    pass

@app.route("/appointment")
def appointment():
    pass

if __name__ == "__main__":
    app.run(debug=True)
