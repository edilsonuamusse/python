import sys
import requests

import sys
import requests # It does import the libary called requests. Basically allows us to download any file from any link, for eg: a csv file

# Check whether a quantity was provided.
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

try:
    quantity = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

url = "https://rest.coincap.io/v3/assets/bitcoin?apiKey=988f70ec56e13ed8f566bd057177304b48e59e8fd8c12f9460e7c0c246944538"

try:
    # Query the API and check for HTTP errors.
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    # Extract the price and convert it to a number.
    data = response.json()
    price = float(data["data"]["priceUsd"])

except requests.RequestException:
    sys.exit("Could not retrieve Bitcoin price")
except (KeyError, TypeError, ValueError):
    sys.exit("Invalid API response")

total = quantity * price
print(f"${total:,.4f}")
