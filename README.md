# Cryptocurrency ETL Pipeline

An automated, end-to-end data pipeline designed to extract, process, and visualize live cryptocurrency market data. This project demonstrates a complete data engineering workflow using a containerized modern data stack.

## 🛠 Tech Stack
* **Orchestration:** Apache Airflow
* **Database:** PostgreSQL
* **Data Processing:** Python (Pandas, SQLAlchemy)
* **Visualization:** Metabase
* **Infrastructure:** Docker & Docker Compose

## ⚙️ Pipeline Architecture
The ETL pipeline is orchestrated by an Airflow DAG and consists of three main stages:
1. **Extract:** Fetches real-time market data for top cryptocurrencies (Bitcoin, Ethereum, Ripple, Solana, Cardano) from a public API.
2. **Load:** Inserts the raw data directly into the `crypto_prices` table in PostgreSQL.
3. **Transform:** Cleans and enriches the data using Pandas. It calculates prices in Saudi Riyals (SAR), converts the market cap to billions for readability, and categorizes price levels. The final dataset is loaded into the `crypto_analytics` table for visualization.

## 🚀 How to Run the Project
The entire infrastructure runs locally in isolated Docker containers.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ariffalshehri/crypto_data_pipeline.git](https://github.com/ariffalshehri/crypto_data_pipeline.git)
   cd crypto_data_pipeline

2. **Start the services**
    docker-compose up -d


3.  **Access the Web Interfaces**

--Apache Airflow UI--

URL: http://localhost:8080

Username: admin

Password: admin

--Metabase UI--

URL: http://localhost:3000

(Setup: Connect to the PostgreSQL database using your database credentials to view the dashboards).
