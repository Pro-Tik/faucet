import requests
import json
import time
import random

def load_wallets(filename):
    """Load wallet addresses from a file."""
    with open(filename, 'r') as file:
        wallets = [line.strip() for line in file if line.strip()]
    return wallets

def load_proxies(filename):
    """Load proxy addresses from a file."""
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

def get_random_proxy(proxies):
    """Select a random proxy from the list."""
    if proxies:
        return random.choice(proxies)
    return None

def request_tokens(wallet, proxies, max_retries=3):
    """Request tokens from the faucet for a specific wallet address."""
    url = "https://faucet.blockbolt.io/api/faucet"  # Adjust API endpoint if necessary
    headers = {'Content-Type': 'application/json'}
    data = {"address": wallet}  # Adjust based on actual API requirements

    retries = 0

    while retries < max_retries:
        proxy = get_random_proxy(proxies)
        if proxy:
            print(f"Trying proxy: {proxy} for wallet: {wallet}")
            try:
                response = requests.post(url, headers=headers, data=json.dumps(data), proxies={"http": proxy, "https": proxy}, timeout=10)
            except requests.exceptions.RequestException as e:
                print(f"Proxy {proxy} failed. Error: {e}")
                retries += 1
                continue  # Try another proxy

            if response.status_code == 200:
                print(f"Successfully requested tokens for wallet: {wallet} - {response.json()}")
                return True
            else:
                print(f"Failed with proxy {proxy} for wallet: {wallet} - Status code: {response.status_code} - {response.text}")
                retries += 1
        else:
            print("No proxies available.")
            break

    print(f"Failed to request tokens for wallet: {wallet} after {max_retries} attempts.")
    return False

def main():
    wallets = load_wallets('wallet.txt')
    proxies = load_proxies('proxy.txt')

    for wallet in wallets:
        success = request_tokens(wallet, proxies)
        if not success:
            print(f"Giving up on wallet: {wallet} after multiple failed attempts.")
        time.sleep(5)  # Wait 5 seconds between requests to avoid rate limits

if __name__ == "__main__":
    main()
