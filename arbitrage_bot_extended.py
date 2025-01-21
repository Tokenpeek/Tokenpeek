import requests
import time
import logging
import random

# Set up logging to a file and console
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", handlers=[
    logging.FileHandler("arbitrage_bot_extended.log"),
    logging.StreamHandler()
])

# API endpoints for exchanges (mocked here)
BINANCE_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
COINBASE_API_URL = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'

# Mock trading fees (e.g., 0.1% trading fee)
TRADING_FEE = 0.001

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

# Function to simulate trading action with fee consideration
def execute_trade(action, amount, price):
    # Calculate trade value after fees
    fee = amount * price * TRADING_FEE
    net_amount = amount * price - fee
    logging.info(f"Executing {action} trade for {amount} BTC at ${price} each. Trade fee: ${fee:.2f}")
    logging.info(f"Net amount after fees: ${net_amount:.2f}")
    # In a real bot, this would interact with the exchange API to place an order
    logging.info(f"{action.capitalize()} trade successful: {amount} BTC at ${price} each")

# Function to simulate random delay between operations
def random_delay():
    delay = random.uniform(1, 5)  # Random delay between 1 to 5 seconds
    time.sleep(delay)

# Function to check for arbitrage opportunity with price difference
def check_arbitrage():
    binance_price = get_binance_price()
    coinbase_price = get_coinbase_price()

    if binance_price is None or coinbase_price is None:
        return  # If prices could not be fetched, exit the function

    logging.info(f"Binance BTC Price: ${binance_price}")
    logging.info(f"Coinbase BTC Price: ${coinbase_price}")

    # Check for arbitrage opportunities (10% price difference)
    if binance_price < coinbase_price * 0.9:
        logging.info(f"Arbitrage Opportunity Found! Buy on Binance and sell on Coinbase.")
        profit = (coinbase_price - binance_price) * (1 - TRADING_FEE * 2)
        logging.info(f"Profit per BTC: ${profit:.2f} (after fees)")
        # Simulate trade execution with fees
        amount = random.uniform(0.5, 2)  # Random trade amount between 0.5 to 2 BTC
        execute_trade("buy", amount, binance_price)
        execute_trade("sell", amount, coinbase_price)
    elif coinbase_price < binance_price * 0.9:
        logging.info(f"Arbitrage Opportunity Found! Buy on Coinbase and sell on Binance.")
        profit = (binance_price - coinbase_price) * (1 - TRADING_FEE * 2)
        logging.info(f"Profit per BTC: ${profit:.2f} (after fees)")
        # Simulate trade execution with fees
        amount = random.uniform(0.5, 2)  # Random trade amount between 0.5 to 2 BTC
        execute_trade("buy", amount, coinbase_price)
        execute_trade("sell", amount, binance_price)
    else:
        logging.info("No arbitrage opportunity found.")

# Function to simulate a "smart" trade opportunity
def simulate_smart_trade():
    logging.info("Simulating smart arbitrage trade...")

    # Generate random scenario
    scenario = random.choice(["no_opportunity", "binance_to_coinbase", "coinbase_to_binance"])
    
    if scenario == "no_opportunity":
        logging.info("No arbitrage opportunities at the moment.")
    elif scenario == "binance_to_coinbase":
        logging.info("Found an opportunity: Buy BTC on Binance, Sell BTC on Coinbase.")
        profit = random.uniform(100, 500)  # Random profit value
        logging.info(f"Estimated profit: ${profit:.2f}")
    elif scenario == "coinbase_to_binance":
        logging.info("Found an opportunity: Buy BTC on Coinbase, Sell BTC on Binance.")
        profit = random.uniform(100, 500)  # Random profit value
        logging.info(f"Estimated profit: ${profit:.2f}")

# Main loop to keep checking prices
if __name__ == "__main__":
    while True:
        logging.info("\nChecking for arbitrage opportunities...")
        check_arbitrage()
        simulate_smart_trade()  # Simulating a smart trade scenario
        random_delay()  # Random delay between checks to simulate real-time
        logging.info("Waiting for the next opportunity...\n")
