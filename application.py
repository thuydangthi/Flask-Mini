import datetime
import wikipedia
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")

@app.route("/search", methods=["GET"])
def search():
    return render_template("search.html")

@app.route("/result", methods=["POST"])
def result():
    search = request.form.get("search", None)
    try:
        page = wikipedia.page(search)
    except:
        page = None
    return render_template("results.html", page=page)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/countdown", methods=["GET"])
def countdown():
    """
    Calculate and return the number of days until Christmas.
    """
    dt = datetime.datetime
    now = dt.now()
    christmas_day = 25
    christmas_month = 12
    christmas_year = now.year

    if now.month == christmas_month and now.day >= christmas_day:
        christmas_year = now.year + 1
    timeLeft = dt(year=christmas_year, month=christmas_month, day=christmas_day)\
        - dt(year=now.year, month=now.month, day=now.day)

    return render_template("countdown.html", day_left=timeLeft.days, year = christmas_year)
