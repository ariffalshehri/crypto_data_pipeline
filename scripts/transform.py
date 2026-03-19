import pandas as pd
from sqlalchemy import create_engine

def transform_data():
    db_url = 'postgresql://admin:admin_password@postgres:5432/crypto_db'
    engine = create_engine(db_url)
    
    try:
        df = pd.read_sql('SELECT * FROM crypto_prices', engine)
        
        
        df['price_category'] = df['current_price'].apply(lambda x: 'High' if x > 1000 else 'Low')
        
        
        df['market_cap_billions'] = df['market_cap'] / 1e9
        
        
        exchange_rate = 3.75
        df['price_sar'] = df['current_price'] * exchange_rate
        
        df.to_sql('crypto_analytics', engine, if_exists='replace', index=False)
        print("Data transformed successfully with SAR prices.")
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    transform_data()