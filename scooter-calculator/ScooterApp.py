from flask import Flask, render_template, request
import ScooterCost as sc

ScooterApp = Flask(__name__)


@ScooterApp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        minutes = int(request.form["minutes"])
        cost = sc.ScooterMinute(minutes)
        return render_template("result.html", minutes=minutes, cost=cost)
    return render_template("index.html")

@ScooterApp.route("/kilometer", methods=["GET", "POST"])
def kilometerRoute():
    if request.method == "POST":
        kilometer = int(request.form["kilometer"])
        cost = sc.ScooterKilometer(kilometer)
        return render_template("result2.html", kilometer=kilometer, cost=cost)
    return render_template("index.html")
