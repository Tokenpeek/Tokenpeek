import requests
import logging

# Set up logging to a file and console
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", handlers=[
    logging.FileHandler("token_collector.log"),
    logging.StreamHandler()
])

# Exchange API URLs (mocked for demonstration, to be replaced with real endpoints)
BINANCE_API_URL = 'https://api.binance.com/api/v3/exchangeInfo'
COINBASE_API_URL = 'https://api.coinbase.com/v2/currencies'
KRAKEN_API_URL = 'https://api.kraken.com/0/public/AssetPairs'

# Function to get token list from Binance
def get_binance_tokens():
    try:
        response = requests.get(BINANCE_API_URL)
        response.raise_for_status()
        data = response.json()
        tokens = [symbol['baseAsset'] for symbol in data['symbols'] if symbol['status'] == 'TRADING']
        logging.info(f"Binance Tokens: {tokens}")
        return tokens
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Binance tokens: {e}")
        return []

# Function to get token list from Coinbase
def get_coinbase_tokens():
    try:
        response = requests.get(COINBASE_API_URL)
        response.raise_for_status()
        data = response.json()
        tokens = [currency['id'] for currency in data['data']]
        logging.info(f"Coinbase Tokens: {tokens}")
        return tokens
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Coinbase tokens: {e}")
        return []

# Function to get token list from Kraken
def get_kraken_tokens():
    try:
        response = requests.get(KRAKEN_API_URL)
        response.raise_for_status()
        data = response.json()
        tokens = [pair.split('/')[0] for pair in data['result'].keys()]  # Extract base tokens from pairs
        logging.info(f"Kraken Tokens: {tokens}")
        return tokens
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching Kraken tokens: {e}")
        return []

# Main function to collect tokens from all exchanges
def collect_tokens():
    logging.info("Collecting tokens from exchanges...")

    binance_tokens = get_binance_tokens()
    coinbase_tokens = get_coinbase_tokens()
    kraken_tokens = get_kraken_tokens()

    # Combine all tokens and remove duplicates
    all_tokens = set(binance_tokens + coinbase_tokens + kraken_tokens)
    logging.info(f"All Collected Tokens: {all_tokens}")

    # You can save this data to a file or database for future use
    with open("collected_tokens.txt", "w") as f:
        for token in all_tokens:
            f.write(f"{token}\n")

    logging.info("Token collection completed and saved to 'collected_tokens.txt'.")

# Run the token collection
if __name__ == "__main__":
    collect_tokens()
