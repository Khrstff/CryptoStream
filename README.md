# 📊 CryptoStream – Real-Time Cryptocurrency Data Pipeline

CryptoStream is a real-time data pipeline that collects, transforms, stores, and visualizes cryptocurrency prices using Python, PostgreSQL, Streamlit, and Docker.

---

## 🚀 Features

- 🔄 Automatic price ingestion from the CoinGecko API every 5 seconds  
- 🧼 Clean, structured transformation of data  
- 🗃 Persistent storage in PostgreSQL with decimal precision  
- 📈 Live dashboard built with Streamlit  
- 🐳 Fully containerized using Docker and Docker Compose  

---

## 🧱 Project Structure

```plaintext
crypto-stream/
├── config/
│   └── settings.env           # Environment variables (DB and API config)
├── dashboard/
│   └── app.py                 # Real-time dashboard built with Streamlit
├── scripts/
│   ├── ingest.py              # Fetches data from CoinGecko API
│   ├── transform.py           # Cleans and structures the raw data
│   └── store.py               # Inserts data into PostgreSQL
├── start_runner.sh            # Shell script that runs the pipeline every 5 seconds
├── runner.py                  # Orchestrates the full pipeline (ingest → transform → store)
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker image configuration
├── docker-compose.yml         # Docker Compose setup for DB, pipeline, and dashboard
└── README.md                  # Project overview and instructions
```

---

## ⚙️ Technologies Used

- **Python 3.11**
- **PostgreSQL 15**
- **Pandas, SQLAlchemy, psycopg2**
- **Streamlit**
- **Docker + Docker Compose**
- **CoinGecko API**

---

## 📦 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/crypto-stream.git
cd crypto-stream
```

### 2. Set up environment variables

Create a file at `config/settings.env`:

```env
DB_HOST=postgres
DB_PORT=5432
DB_USER=postgres
DB_PASS=postgres
DB_NAME=cryptodb
COINGECKO_URL=https://api.coingecko.com/api/v3/simple/price
```

### 3. Run the project with Docker Compose

```bash
docker compose up --build
```

- 📊 Dashboard: http://localhost:8501  
- 🐘 PostgreSQL available on host port: `5433` (if remapped)

---

## 🗃 Database: Table Schema

Ensure the following table exists in your PostgreSQL database:

```sql
CREATE TABLE crypto_prices (
    id SERIAL PRIMARY KEY,
    crypto VARCHAR(50),
    price_usd NUMERIC(12, 6),
    timestamp_utc TIMESTAMP
);
```

---

## 👤 Author

**Daniel Khristoff Aguilar Jiménez**  
_Data Engineer & Python Developer_  
📧 danielaj1909@gmail.com

---

## 🏷 Suggested GitHub Topics

`data-engineering` · `cryptocurrency` · `real-time` · `streamlit` · `postgresql` · `docker` · `python`

