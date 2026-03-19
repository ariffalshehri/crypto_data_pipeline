import requests
import pandas as pd
import os

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': 'bitcoin,ethereum,cardano,solana,ripple',
        'order': 'market_cap_desc'
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df = df[['id', 'symbol', 'current_price', 'market_cap', 'total_volume', 'last_updated']]
        print("Data fetched successfully!")
        return df
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    df = fetch_crypto_data()
    if df is not None:
        os.makedirs("/opt/airflow/data", exist_ok=True)
        file_path = "/opt/airflow/data/crypto_data.csv"
        
        df.to_csv(file_path, index=False)
        print(f"Data saved successfully to {file_path}")
        print(df.head())