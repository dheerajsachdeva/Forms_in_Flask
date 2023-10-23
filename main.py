from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods= ["POST"])
def login():
    name = request.form["username"]
    password = request.form["password"]
    return f"Name: {name}, Password: {password}"

if __name__ == "__main__":
    app.run(debug=True)
