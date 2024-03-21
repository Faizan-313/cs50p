import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        value = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

try:
    l = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = l.json()
    rate = r["bpi"]["USD"]["rate_float"]
    amount = rate*value
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit("page not available currently")


