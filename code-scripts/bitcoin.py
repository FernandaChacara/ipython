import sys
import requests

# 1) Check if the user provided a command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

# 2) Convert the argument to a float
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# 3) Make a request to the CoinCap API
try:
    r = requests.get(
        "https://rest.coincap.io/v3/assets/bitcoin?apiKey=749825ee0396dcd6503ef10aa08419b15f48f4003ec96613fc685369cc6a3148"
    )
except requests.RequestException:
    sys.exit("Network error")

# 4) Extract the price from the JSON response
try:
    data = r.json()
    price = float(data["data"]["priceUsd"])
except (KeyError, TypeError, ValueError):
    sys.exit("Unexpected response")

# 5) Calculate and print the USD value with 4 decimal places and thousand separators
amount = bitcoins * price
print(f"${amount:,.4f}")
