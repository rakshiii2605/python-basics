import requests

API_KEY = "demo"  
BASE_URL = "https://www.alphavantage.co/query"

def get_stock_price(symbol):
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if "Global Quote" in data:
        price = data["Global Quote"]["05. price"]
        return float(price)
    else:
        return None

if __name__ == "__main__":
    symbol = input("Enter stock symbol (e.g., AAPL, TSLA, MSFT): ")
    price = get_stock_price(symbol)

    if price:
        print(f"📈 Current price of {symbol}: ${price}")
    else:
        print("⚠️ Could not fetch stock price. Check API key or symbol.")
