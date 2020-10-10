from flask import Flask
import requests

app = Flask(__name__)

#API_URL = f'https://financialmodelingprep.com/api/v3/quote-short/{ticket}'  # ?apikey=5f05375cf0a7a36dda57008663befa65'


def fetch_price(ticker):
    data = requests.get(f'https://financialmodelingprep.com/api/v3/quote-short/{ticker.upper()}',
                        params={"apikey": "5f05375cf0a7a36dda57008663befa65"})
    return data.json()[0]['price']


@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return f"The price of {ticker} is {price}"


@app.route("/")
def home_page():
    return "Try /stock/AAPL"


if __name__ == '__main__':
    fetch_price("AAPL")
