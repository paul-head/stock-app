from flask import Blueprint, render_template, redirect, url_for, request


home = Blueprint("home", __name__)


@home.route("/")
def home_page():
    return render_template("home/index.html")


@home.route("/lookup", methods=["POST"])
def lookup():
    print(request.form)
    return redirect(url_for("stock.quote", ticker=request.form["ticker"]))
