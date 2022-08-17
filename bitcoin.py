import requests
import sys

def main():
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command line argument is not a number")
        sys.exit()
    result = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = result.json()
    rate = result["bpi"]["USD"]["rate_float"]
    cost = n * rate
    print(f"${cost:,.4f}")


if __name__ == "__main__":
    main()