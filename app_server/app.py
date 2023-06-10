from flask import Flask, render_template

app = Flask(__name__)


@app.route("/login")
def login():
    return render_template("regal/pages/samples/login.html")


@app.route("/logout")
def logout():
    return render_template("regal/pages/samples/login.html")


@app.route("/")
def index():
    return render_template("regal/index.html")


if __name__ == "__main__":
    app.run(debug=True)
