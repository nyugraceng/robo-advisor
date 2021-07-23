import requests
import json

from pprint import pprint

from getpass import getpass # secret version of the import function
# locally we'll wan t to use env vars
# but on colab we can use getpass / input them
api_key = getpass("Please input your api key:")
symbol = "MSFT"
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}"
response = requests.get(stock_url)
parsed_response = json.loads(response.text)
print(type(parsed_response))
pprint(parsed_response)

# this is the "app/robo_advisor.py" file

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
