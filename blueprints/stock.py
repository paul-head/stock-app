from flask import Blueprint, render_template
from pprint import pprint
import requests

stock = Blueprint('stock', __name__)


def fetch_price(ticker):
    data = requests.get(f'https://financialmodelingprep.com/api/v3/quote-short/{ticker.upper()}',
                        params={"apikey": "5f05375cf0a7a36dda57008663befa65"})
    return data.json()[0]['price']


def fetch_income(ticker):
    financials = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{ticker}",
                              params={'period': 'quarter',
                                      'apikey': '5f05375cf0a7a36dda57008663befa65'}).json()  # ["financials"]
    financials.sort(key=lambda quarter: quarter['date'])
    return financials


@stock.route('/<string:ticker>')
def quote(ticker):
    price = fetch_price(ticker)
    return render_template("stock/quote.html", ticker=ticker, stock_price=price)


@stock.route('/<string:ticker>/financials')
def financials(ticker):
    data = fetch_income(ticker)

    chart_data = [float(q["eps"]) for q in data if q["eps"]]
    chart_params = {
        "type": "line",
        "data": {
            "labels": [q["date"] for q in data if q["eps"]],
            "datasets": [{"label": 'EPS', "data": chart_data}]
        }
    }
    return render_template('stock/financials.html', ticker=ticker, financials=data, chart_params=chart_params)
