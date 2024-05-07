from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:Khalil100100@localhost/cloudy_members"
)
db = SQLAlchemy(app)


class Team(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    CGPA = db.Column(db.DECIMAL, nullable=False)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/team")
def team():
    return render_template("team.html", team=Team.query.all())


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
