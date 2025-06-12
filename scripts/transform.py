import pandas as pd
from datetime import datetime

def transform_crypto_data(raw_data):

    # Verifica estructura esperada
    if not raw_data:
        raise ValueError("No se recibieron datos para transformar.")

    # Convierte a lista de registros
    records = []
    timestamp = datetime.utcnow()

    for coin, info in raw_data.items():
        records.append({
            "crypto": coin,
            "price_usd": info["usd"],
            "timestamp_utc": timestamp
        })

    # DataFrame ordenado
    df = pd.DataFrame(records)
    pd.set_option('display.float_format', lambda x: f'{x:.6f}')

    return df

# Uso local de prueba
if __name__ == "__main__":
    from ingest import fetch_crypto_prices
    raw = fetch_crypto_prices()
    df = transform_crypto_data(raw)
    print(df)
