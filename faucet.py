import requests
import time
import os
import subprocess
import sys

REPO_URL = "https://github.com/Pro-Tik/sui-faucet-claimer.git"
LOCAL_REPO_PATH = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory

def check_for_updates():
    """Checks if the script is running from the specified Git repository and pulls updates if it is."""
    try:
        # Check if the current directory is a git repository
        if not os.path.exists(os.path.join(LOCAL_REPO_PATH, '.git')):
            print("Error: This script must be run from the Git repository.")
            sys.exit(1)  # Exit if not in a git repository
        
        # Pull the latest updates from the repository
        subprocess.run(["git", "pull"], cwd=LOCAL_REPO_PATH, check=True)
        print("Updated to the latest version from the repository.")
    except Exception as e:
        print(f"Failed to check for updates: {e}")
        sys.exit(1)  # Exit on failure

def load_proxies():
    """Loads proxies from proxies.txt file."""
    try:
        with open('proxies.txt', 'r') as file:
            proxies = [line.strip() for line in file if line.strip()]
        return proxies
    except FileNotFoundError:
        print("Error: 'proxies.txt' file not found.")
        return []

def load_wallets():
    """Loads wallet addresses from wallet.txt file."""
    try:
        with open('wallet.txt', 'r') as file:
            wallets = [line.strip() for line in file if line.strip()]
        return wallets
    except FileNotFoundError:
        print("Error: 'wallet.txt' file not found.")
        return []

def request_faucet_tokens(wallet_address, proxy=None):
    url = "https://faucet.testnet.sui.io/v1/gas"  # SUI faucet endpoint
    
    # Payload for requesting tokens
    payload = {
        "FixedAmountRequest": {  
            "recipient": wallet_address  # Your wallet address
        }
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    proxies_dict = {
        "http": proxy,
        "https": proxy
    } if proxy else None
    
    try:
        response = requests.post(url, json=payload, headers=headers, proxies=proxies_dict)
        response.raise_for_status()  # Raise error for bad responses (4xx or 5xx)
        return response.json()  # Assuming the response is in JSON format
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if response.content:
            print("Response content:", response.content)
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    check_for_updates()  # Check for updates when the script starts

    wallets = load_wallets()
    proxies = load_proxies()

    if not wallets:
        print("No wallets found. Please ensure 'wallet.txt' contains wallet addresses.")
    elif not proxies:
        print("No proxies found. Please ensure 'proxies.txt' contains proxy addresses.")
    else:
        proxy_index = 0  # Start at the first proxy
        proxy_count = len(proxies)

        while True:  # Infinite loop to run the script every 10 minutes
            for wallet_address in wallets:
                # Use proxies in round-robin fashion
                proxy = proxies[proxy_index] if proxies else None
                print(f"Using proxy: {proxy} for wallet: {wallet_address}")
                
                result = request_faucet_tokens(wallet_address, proxy)
                
                if result:
                    print(f"Tokens requested successfully for {wallet_address}: {result}")
                else:
                    print(f"Failed to request tokens for {wallet_address}.")
                
                # Move to the next proxy for the next request
                proxy_index = (proxy_index + 1) % proxy_count

            print("Waiting for 10 minutes before the next run...")
            time.sleep(600)  # Wait for 10 minutes (600 seconds)
