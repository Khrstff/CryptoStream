# scripts/ingest.py
import requests
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="config/settings.env")

def fetch_crypto_prices():
    url = os.getenv("COINGECKO_URL")
    params = {
        "ids": "ethereum,dogecoin,solana,pepe",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    data = fetch_crypto_prices()
    print(data)
