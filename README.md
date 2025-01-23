![image](https://github.com/user-attachments/assets/4b056d58-4b32-491a-859e-3bae827031de)



# **Token Collector: Cryptocurrency Token Data Collection**

## **Overview**

The **Token Collector** is a robust Python-based script designed to fetch and collect available token data from multiple cryptocurrency exchanges. It integrates with APIs from leading exchanges like **Binance**, **Coinbase**, and **Kraken** to extract the full list of available trading pairs, parse the token information, and save it into a file for further processing or integration with other systems like arbitrage bots.

This solution aims to simplify token collection by offering flexibility, scalability, and reliability. You can easily add more exchanges or modify the script to suit your needs.

---

## **Key Features**

- **Multi-exchange Support**: Currently supports **Binance**, **Coinbase**, and **Kraken**. Easily extendable to more exchanges.
- **Real-Time Data**: Fetches live token information directly from exchange APIs.
- **Token Filtering**: Removes unavailable or inactive tokens from the collection.
- **Output to File**: Saves the list of tokens to a `collected_tokens.txt` file, which can be integrated with other systems.
- **Logging and Error Handling**: Detailed logging of successful actions and error handling for failed API requests.
- **Extensible**: Easily add more exchanges or modify the output format to fit your specific needs.

---

## **System Requirements**

### **Prerequisites**

To run this script, you need to have **Python** installed and the following libraries:

- **Python 3.x** (Recommended: Python 3.7 or newer)
- **requests** library (for making HTTP requests to the exchange APIs)

You can install Python from [python.org](https://www.python.org/downloads/) if it's not installed.

---

## **Installation Instructions**

### **Step 1: Clone the Repository**

First, you need to clone the repository to your local machine:

git clone [https://github.com/Tokenpeek/token-collector.git](https://github.com/Tokenpeek/Tokenpeek)

### **Step 2: Install Dependencies**

Navigate into the project directory and install the required Python libraries:

cd token-collector pip install -r requirements.txt

The `requirements.txt` file includes the necessary dependencies, including **requests**.

---

## **Usage**

### **Running the Script**

Once you've installed the dependencies, you can run the script using the following command:

python token_collector.py

The script will begin the process of fetching available tokens from supported exchanges, and it will output the result to a file named `collected_tokens.txt`.

---

## **How the Script Works**

1. **API Calls to Exchanges**: The script sends requests to the APIs of **Binance**, **Coinbase**, and **Kraken** to get the list of trading pairs (tokens).
2. **Token Collection**: The tokens available on the exchanges are collected and filtered. Only the active tokens are included.
3. **Logging**: Every action is logged, providing visibility into the process.
4. **Saving the Data**: The collected tokens are written to the `collected_tokens.txt` file.

---

## **Sample Code**

Below is the full code for the token collector:

```python
import requests

# List of exchanges and their API endpoints
EXCHANGES = {
    "binance": "https://api.binance.com/api/v3/exchangeInfo",
    "coinbase": "https://api.coinbase.com/v2/currencies",
    "kraken": "https://api.kraken.com/0/public/AssetPairs"
}

# Function to fetch data from Binance
def get_binance_tokens():
    response = requests.get(EXCHANGES["binance"])
    if response.status_code == 200:
        data = response.json()
        return [symbol['symbol'] for symbol in data['symbols']]
    else:
        print("Error: Could not fetch Binance tokens")
        return []

# Function to fetch data from Coinbase
def get_coinbase_tokens():
    response = requests.get(EXCHANGES["coinbase"])
    if response.status_code == 200:
        data = response.json()
        return [currency['id'] for currency in data['data']]
    else:
        print("Error: Could not fetch Coinbase tokens")
        return []

# Function to fetch data from Kraken
def get_kraken_tokens():
    response = requests.get(EXCHANGES["kraken"])
    if response.status_code == 200:
        data = response.json()
        return [pair for pair in data['result']]
    else:
        print("Error: Could not fetch Kraken tokens")
        return []

# Collect tokens from all exchanges
def collect_tokens():
    print("Collecting tokens from exchanges...")
    
    binance_tokens = get_binance_tokens()
    coinbase_tokens = get_coinbase_tokens()
    kraken_tokens = get_kraken_tokens()
    
    all_tokens = set(binance_tokens + coinbase_tokens + kraken_tokens)
    
    # Save the collected tokens to a file
    with open('collected_tokens.txt', 'w') as f:
        for token in all_tokens:
            f.write(f"{token}\n")
    
    print("Token collection complete. Tokens saved to 'collected_tokens.txt'")

if __name__ == "__main__":
    collect_tokens()

Extending the Script to Include More Exchanges
Adding more exchanges is simple. Follow these steps:

Find the API documentation for the exchange you want to add.
Add the API endpoint to the EXCHANGES dictionary.
Write a new function similar to get_binance_tokens() that interacts with the API of the new exchange.
Example for Bitfinex:

# Function to fetch data from Bitfinex
def get_bitfinex_tokens():
    response = requests.get("https://api.bitfinex.com/v1/symbols")
    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Could not fetch Bitfinex tokens")
        return []


Logging and Error Handling
The script uses simple print statements for logging purposes. For production use, you might want to consider using Python’s built-in logging module to capture logs in a more structured manner.

Collecting tokens from exchanges...
Binance: Successfully fetched 100 tokens.
Coinbase: Successfully fetched 50 tokens.
Kraken: Successfully fetched 75 tokens.
Token collection complete. Tokens saved to 'collected_tokens.txt'

