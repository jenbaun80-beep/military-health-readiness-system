import pandas as pd
import sqlite3
import os

def run_etl():
    print("Starting ETL pipeline...")
    if not os.path.exists('military_health_raw.csv'):
        raise FileNotFoundError("Raw data not found. Run generate_data.py first.")
    
    # Extract
    df = pd.read_csv('military_health_raw.csv')
    
    # Transform
    df.dropna(inplace=True)
    df['service_id'] = df['service_id'].astype(str)
    
    # Load into SQLite database
    conn = sqlite3.connect('readiness.db')
    df.to_sql('health_readiness', conn, if_exists='replace', index=False)
    conn.close()
    print("ETL Pipeline complete. Data loaded into readiness.db securely.")

if __name__ == '__main__':
    run_etl()
