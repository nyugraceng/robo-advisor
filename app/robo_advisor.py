import csv
import requests
from datetime import datetime
import json
import os

from dotenv import load_dotenv
load_dotenv()

from pprint import pprint

def run_automated_stock_rec(symbol):
    api_key = os.environ.get("ALPHAVANTAGE_API_KEY")

    def to_usd(my_price):
        return "${0:,.2f}".format(my_price)

    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"

    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    # pprint(parsed_response)
    try:
        last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
    except KeyError:
        print("Uh oh, this seems to be an invalid symbol - maybe try again?")
        return

    tsd = parsed_response["Time Series (Daily)"]

    # sort to ensure latest day is first 
    dates = list(tsd.keys()) 

    latest_day = dates[0] 
    latest_close = float(tsd[latest_day]["4. close"])

    high_prices = []
    low_prices = []

    for date in dates:
        high_price = tsd[date]["2. high"]
        high_prices.append(float(high_price))
        low_price = tsd[date]["3. low"]
        low_prices.append(float(low_price))


    recent_high = float(max(high_prices))
    recent_low = float(min(low_prices))

    # csv_file_path = "data/prices.csv" change to be OS friendly
    csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

    csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

    with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader() # uses fieldnames set above
        for date in dates:
            daily_prices = tsd[date]
            writer.writerow({
                "timestamp": date,
                "open": daily_prices["1. open"],
                "high": daily_prices["2. high"],
                "low": daily_prices["3. low"],
                "close": daily_prices["4. close"],
                "volume": daily_prices["6. volume"]
            })

    now = datetime.now()
    current_time = now.strftime("%I:%M:%S")
    currentSecond= datetime.now().second
    currentMinute = datetime.now().minute
    currentHour = datetime.now().hour

    current_date = now.strftime("%d %B,%Y")
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    # recommendation
    is_buy = "BUY" if latest_close < recent_low * 1.2 else "DON'T BUY"
    rec_condition = "less than" if is_buy == "BUY" else "greater than"

    print("-------------------------")
    print(f"SELECTED SYMBOL: {symbol}")
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")
    # Run at: 11:52pm on June 5th, 2018
    print(f"YOUR REQUEST RUN AT: {current_time} on {current_date}") 
    print("-------------------------")
    print(f"LATEST DAY: {last_refreshed}")
    print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
    print(f"RECENT HIGH: {to_usd(float(recent_high))}")
    print(f"RECENT LOW: {to_usd(float(recent_low))}")
    print("-------------------------")
    print(f"RECOMMENDATION: {is_buy}")
    print(f"RECOMMENDATION REASON: We are recommending {is_buy.lower()} {symbol} because it's latest closing price {to_usd(latest_close)} is {rec_condition} 20% above its recent low {to_usd(recent_low)}")
    print("-------------------------")
    print(f"WRITING DATA TO CSV: {csv_file_path }...")
    print("-------------------------")
    print("HAPPY INVESTING!")
    print("-------------------------")

symbol = "TSLA"
run_automated_stock_rec(symbol) 