import requests
import time

# API endpoints for exchanges (mocked here)
BINANCE_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
COINBASE_API_URL = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

# Function to get the current price of BTC from Binance
def get_binance_price():
    response = requests.get(BINANCE_API_URL)
    data = response.json()
    return float(data['price'])

# Function to get the current price of BTC from Coinbase
def get_coinbase_price():
    response = requests.get(COINBASE_API_URL)
    data = response.json()
    return float(data['data']['amount'])

# Function to check for arbitrage opportunity
def check_arbitrage():
    binance_price = get_binance_price()
    coinbase_price = get_coinbase_price()

    print(f"Binance BTC Price: ${binance_price}")
    print(f"Coinbase BTC Price: ${coinbase_price}")

    # Check if an arbitrage opportunity exists (10% price difference)
    if binance_price < coinbase_price * 0.9:
        print(f"Arbitrage Opportunity Found! Buy on Binance and sell on Coinbase.")
        profit = coinbase_price - binance_price
        print(f"Profit per BTC: ${profit:.2f}")
    elif coinbase_price < binance_price * 0.9:
        print(f"Arbitrage Opportunity Found! Buy on Coinbase and sell on Binance.")
        profit = binance_price - coinbase_price
        print(f"Profit per BTC: ${profit:.2f}")
    else:
        print("No arbitrage opportunity found.")

# Main loop to keep checking prices
if __name__ == "__main__":
    while True:
        print("\nChecking for arbitrage opportunities...")
        check_arbitrage()
        time.sleep(10)  # Sleep for 10 seconds before checking again
