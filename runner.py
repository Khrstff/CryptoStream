import time
from scripts.ingest import fetch_crypto_prices
from scripts.transform import transform_crypto_data
from scripts.store import store_data

def run_pipeline():
    while True:
        try:
            print("🔄 Ejecutando pipeline de datos...")
            raw = fetch_crypto_prices()
            df = transform_crypto_data(raw)
            store_data(df)
            print("✅ Datos procesados e insertados correctamente.")
        except Exception as e:
            print(f"❌ Error durante ejecución del pipeline: {e}")
        
        time.sleep(5)  # Espera de 5 segundos

if __name__ == "__main__":
    run_pipeline()
