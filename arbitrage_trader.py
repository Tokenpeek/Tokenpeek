import requests
import time
import logging

# Set up logging to a file and console
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", handlers=[
    logging.FileHandler("arbitrage_bot.log"),
    logging.StreamHandler()
])

# API endpoints for exchanges (mocked here)
BINANCE_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
COINBASE_API_URL = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

# Function to get the current price of BTC from Binance
def get_binance_price():
    try:
        response = requests.get(BINANCE_API_URL)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()
        return float(data['price'])
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Binance price: {e}")
        return None

# Function to get the current price of BTC from Coinbase
def get_coinbase_price():
    try:
        response = requests.get(COINBASE_API_URL)
        response.raise_for_status()
        data = response.json()
        return float(data['data']['amount'])
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Coinbase price: {e}")
        return None

# Function to simulate trading action
def execute_trade(action, amount, price):
    logging.info(f"Executing {action} trade for {amount} BTC at ${price}")
    # In a real bot, this would interact with the exchange API to place an order
    # Here we simulate a successful trade by just logging the action
    logging.info(f"Trade successful: {action} {amount} BTC at ${price}")

# Function to check for arbitrage opportunity
def check_arbitrage():
    binance_price = get_binance_price()
    coinbase_price = get_coinbase_price()

    if binance_price is None or coinbase_price is None:
        return  # If prices could not be fetched, exit the function

    logging.info(f"Binance BTC Price: ${binance_price}")
    logging.info(f"Coinbase BTC Price: ${coinbase_price}")

    # Check if an arbitrage opportunity exists (10% price difference)
    if binance_price < coinbase_price * 0.9:
        logging.info(f"Arbitrage Opportunity Found! Buy on Binance and sell on Coinbase.")
        profit = coinbase_price - binance_price
        logging.info(f"Profit per BTC: ${profit:.2f}")
        # Simulate trade execution
        execute_trade("buy", 1, binance_price)
        execute_trade("sell", 1, coinbase_price)
    elif coinbase_price < binance_price * 0.9:
        logging.info(f"Arbitrage Opportunity Found! Buy on Coinbase and sell on Binance.")
        profit = binance_price - coinbase_price
        logging.info(f"Profit per BTC: ${profit:.2f}")
        # Simulate trade execution
        execute_trade("buy", 1, coinbase_price)
        execute_trade("sell", 1, binance_price)
    else:
        logging.info("No arbitrage opportunity found.")

# Main loop to keep checking prices
if __name__ == "__main__":
    while True:
        logging.info("\nChecking for arbitrage opportunities...")
        check_arbitrage()
        time.sleep(10)  # Sleep for 10 seconds before checking again
