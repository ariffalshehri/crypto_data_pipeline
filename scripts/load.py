import pandas as pd
from sqlalchemy import create_engine
import os

def load_data_to_postgres():
    file_path = "/opt/airflow/data/crypto_data.csv"
    
    if not os.path.exists(file_path):
        print("Error: Data file not found.")
        return

    
    df = pd.read_csv(file_path)
    
    
    db_url = 'postgresql://admin:admin_password@postgres:5432/crypto_db'
    engine = create_engine(db_url)
    
    try:
       
        df.to_sql('crypto_prices', engine, if_exists='replace', index=False)
        print("Data loaded successfully to PostgreSQL!")
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    load_data_to_postgres()