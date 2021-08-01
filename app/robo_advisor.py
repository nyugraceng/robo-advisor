import requests
import json

from pprint import pprint

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

symbol = "XYZ"
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

response = requests.get(request_url)
# print(type(response))
# print(response.status_code)
# print(response.text)

parsed_response = json.loads(response.text)

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

tsd = parsed_response["Time Series (Daily)"]

dates = list(tsd.keys()) #sort to ensure latest day is first 

latest_day = dates[0] # "2021-07-30"

latest_close = tsd[latest_day]["4. close"] #> $100.00

#from getpass import getpass # secret version of the import function
# locally we'll wan t to use env vars
# but on colab we can use getpass / input them
#api_key = getpass("Please input your api key:")

# this is the "app/robo_advisor.py" file


print("-------------------------")
print("SELECTED SYMBOL: IBM")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm") #use day time module
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

