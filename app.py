from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return "<h1>login page!!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
