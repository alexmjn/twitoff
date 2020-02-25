import requests
import json
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
print(request_url)
response = requests.get(request_url)
print(type(response))
#class requests.models.Response
dir(response)
#interesting properties- status code - 200 - this will be a property of the response.
#can query this.

#response.text contains the data that we need. As a default, the response.text
# is simply a string. we need to use the json module to convert it.
data = json.loads(response.text)
# this will automatically convert into disctionary.
print(type(data))

print(data.keys)
latest_close = data["Time Series (Daily)"]["2020-02-25"]["4. close"]
print("LATEST CLOSING PRICE:", latest_close)

#note the multilayered indexing here!
