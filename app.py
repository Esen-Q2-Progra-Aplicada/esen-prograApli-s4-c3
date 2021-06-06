from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if request.form["username"] != "admin" or request.form["password"] != "secret":
            flash("invalid credentials", "error")
            return redirect(url_for("login"))
        else:
            flash("you were successfully logged in", "login")
            flash("what another message !?!?", "login")
            return redirect(url_for("index"))
    elif request.method == "GET":
        flash("you are at login sherlock", "render")
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
