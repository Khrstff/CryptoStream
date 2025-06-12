import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / "config" / "settings.env")

def store_data(df: pd.DataFrame):
    """
    Inserta un DataFrame en la tabla crypto_prices de PostgreSQL.
    """
    # Construye la URL de conexión
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    db_url = f"postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

    # Crea la conexión con SQLAlchemy
    engine = create_engine(db_url)

    # Inserta los datos
    df.to_sql("crypto_prices", con=engine, if_exists="append", index=False)
    print("Datos insertados correctamente.")

# Uso local de prueba
if __name__ == "__main__":
    from ingest import fetch_crypto_prices
    from transform import transform_crypto_data

    raw = fetch_crypto_prices()
    df = transform_crypto_data(raw)
    store_data(df)
