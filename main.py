
from flask import Flask, request, redirect, render_template, url_for, session
import random

app = Flask(__name__)
app.secret_key = "super secret key"

cricketers = [
    "Sachin Tendulkar",
    "Virat Kohli",
    "Brian Lara",
    "Ricky Ponting",
    "Jacques Kallis",
    "AB de Villiers",
    "MS Dhoni",
    "Kane Williamson",
    "Steve Smith",
    "David Warner",
]

@app.route("/")
def index():
    if "word" not in session:
        session["word"] = random.choice(cricketers)
        session["guesses"] = []
    return render_template("index.html")

@app.route("/guess", methods=["POST"])
def guess():
    guess = request.form["guess"].title()
    session["guesses"].append(guess)

    if guess == session["word"]:
        return redirect(url_for("win"))
    elif guess not in cricketers:
        return redirect(url_for("invalid"))
    else:
        return redirect(url_for("index"))

@app.route("/hint")
def hint():
    hint = session["word"].split(" ")[0][:3]
    return render_template("hint.html", hint=hint)

@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/win")
def win():
    return render_template("win.html", word=session["word"])

@app.route("/invalid")
def invalid():
    return render_template("invalid.html")

if __name__ == "__main__":
    app.run(debug=True)
