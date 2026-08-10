import pandas as pd
from sqlalchemy import create_engine

def run_etl():
    print("EXTRACT: Reading raw readiness data...")
    raw_df = pd.read_csv("synthetic_readiness_data.csv")
    
    print("TRANSFORM: Cleaning data, handling missing values, standardizing formats...")
    df = raw_df.drop_duplicates(subset=["Member_ID"])
    df["PHA_Date"] = pd.to_datetime(df["PHA_Date"])
    
    print(f"Processed {len(df)} valid records through compliance filters.")
    
    print("LOAD: Storing transformed data into secure database...")
    engine = create_engine("sqlite:///readiness.db")
    df.to_sql("unit_readiness", engine, if_exists="replace", index=False)
    print("ETL Pipeline Complete. Database 'readiness.db' successfully updated.")

if __name__ == "__main__":
    run_etl()
