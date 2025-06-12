import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from pathlib import Path

# Cargar variables de entorno
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / "config" / "settings.env")

# Construir conexión a la base de datos
def get_engine():
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    return create_engine(db_url)

# Cargar los datos desde la base
def load_data():
    engine = get_engine()
    query = "SELECT crypto, price_usd, timestamp_utc FROM crypto_prices ORDER BY timestamp_utc DESC"
    return pd.read_sql(query, engine)

# Construir la interfaz
st.set_page_config(page_title="CryptoStream", layout="wide")

st.title("📈 Monitoreo de precios de criptomonedas")
st.markdown("Visualización en tiempo real de los últimos precios obtenidos.")

df = load_data()

# Mostrar tabla
st.dataframe(df, use_container_width=True)

# Mostrar gráfico
st.line_chart(df.pivot(index='timestamp_utc', columns='crypto', values='price_usd'))
