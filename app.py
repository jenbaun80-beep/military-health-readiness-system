import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Military Health Readiness Command Dashboard", layout="wide")

st.title("🛡️ Military Health Information Governance & Readiness System")
st.markdown("Executive command oversight dashboard for real-time medical readiness tracking and unit availability.")

@st.cache_data
def load_data():
    conn = sqlite3.connect('readiness.db')
    query = "SELECT * FROM health_readiness"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

try:
    df = load_data()
    
    unit_filter = st.sidebar.selectbox("Select Command Unit", options=["All Units"] + list(df['unit'].unique()))
    if unit_filter != "All Units":
        df = df[df['unit'] == unit_filter]
    
    st.metric(label="Total Personnel Monitored", value=len(df))
    
    st.subheader("Readiness Status Breakdown")
    status_counts = df['readiness_status'].value_counts()
    st.bar_chart(status_counts)
    
    st.subheader("Personnel Records Overview")
    st.dataframe(df.head(100))

except Exception as e:
    st.warning("Database not found or empty. Please run generate_data.py and etl_pipeline.py first.")
