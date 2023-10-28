import os
from flask import Flask, render_template, request, send_file
from dotenv import load_dotenv
from enums import MAX_SCORE, NAME, student

load_dotenv()

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/base")
def base():
    return render_template("base.html", title="Python course for Goiteens")


@app.route("/birthday")
def birthday():
    return render_template("birthday.html", title="2010")



@app.route("/login", methods=["GET", "POST"])
def login_user():
    if request.method == "POST":
        user = request.form.get("name")
        return "Method POST"
    else:
        user = request.args.get("name")
        return f"Method GET, user is {user}"



@app.route("/context")
def context():
    context_dict = {
        "title": "Python_course",
        "name": NAME,
        "max_score": MAX_SCORE,
        "student": student
    }
    return render_template("context.html", **context_dict)


if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))

