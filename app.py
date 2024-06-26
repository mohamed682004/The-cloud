from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from time import sleep

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI")
db = SQLAlchemy(app)


class Member(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.FLOAT, nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/team")
def team():
    try:
        return render_template("team.html", team=Member.query.all())
    except:
        sleep(2)
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
