# Military Health Information Governance & Readiness System

An end-to-end data pipeline and application engineered for executive command oversight, featuring automated ETL pipelines and HIPAA/DoD-compliant PHI security layers.

## 🚀 Key Architectural Features

* **Automated ETL Pipeline (`etl_pipeline.py`)**: Extracts, transforms, and loads synthetic health records, ensuring data cleanliness, schema validation, and normalization.
* **Synthetic Data Generation (`generate_data.py`)**: Programmatically generates realistic, compliant mock military readiness and medical status records for testing and analysis.
* **Interactive Command Dashboard (`app.py`)**: Built with Streamlit to provide real-time visualization of medical readiness metrics, deployment statuses, and unit availability.
* **Secure Data Storage (`readiness.db`)**: Uses a structured SQLite relational backend designed to maintain data integrity and support analytical queries.

## 🔄 End-to-End Workflow Architecture

```mermaid
graph TD
    A[generate_data.py] -->|Outputs Raw Data| B(military_health_raw.csv)
    B -->|Ingests & Cleans| C[etl_pipeline.py]
    C -->|Normalizes & Validates| D[(readiness.db)]
    C -->|Exports Processed Data| E(synthetic_readiness_data.csv)
    D -->|Queries Metrics| F[app.py - Streamlit Dashboard]
    E -->|Visualizes Trends| F

## 🖥️ Command Dashboard Interface (`app.py`)

Below is the complete implementation code for the **Streamlit** command dashboard, which reads from your SQLite backend (`readiness.db`) or processed data file to visualize medical readiness metrics and deployment statuses in real time.

```python
import sqlite3
import pandas as pd
import plotly.express as px
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Military Health & Readiness Command Dashboard",
    page_icon="🛡️",
    layout="wide",
)

# Title and Header
st.title("🛡️ Military Health Information Governance & Readiness System")
st.markdown(
    "Executive command oversight dashboard for tracking unit readiness, deployment eligibility, and medical status pipelines."
)
st.markdown("---")


# Database Connection & Data Loading
@st.cache_data
def load_data():
    try:
        conn = sqlite3.connect("readiness.db")
        df = pd.read_sql("SELECT * FROM unit_readiness", conn)
        conn.close()
    except Exception:
        df = pd.read_csv("synthetic_readiness_data.csv")
    return df


df = load_data()

# Sidebar Filters for Command Oversight
st.sidebar.header("Command Filters")
selected_unit = st.sidebar.selectbox(
    "Select Unit Code", options=["All Units"] + list(df["unit_code"].unique())
)
deployment_filter = st.sidebar.selectbox(
    "Deployment Eligibility", options=["All", "Deployable", "Non-Deployable"]
)

# Apply Filters
filtered_df = df.copy()
if selected_unit != "All Units":
    filtered_df = filtered_df[filtered_df["unit_code"] == selected_unit]
if deployment_filter == "Deployable":
    filtered_df = filtered_df[filtered_df["deployable_status"] == "Yes"]
elif deployment_filter == "Non-Deployable":
    filtered_df = filtered_df[filtered_df["deployable_status"] == "No"]

# Top Metrics Row (KPI Cards)
total_personnel = len(filtered_df)
deployable_count = len(
    filtered_df[filtered_df["deployable_status"] == "Yes"]
)
readiness_pct = (
    (deployable_count / total_personnel * 100) if total_personnel > 0 else 0
)
overdue_pha = len(filtered_df[filtered_df["pha_status"] == "Overdue"])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Personnel Tracked", f"{total_personnel:,}")
col2.metric("Fully Deployable", f"{deployable_count:,}")
col3.metric("Readiness Rate", f"{readiness_pct:.1f}%")
col4.metric("PHA Overdue / Action Req.", f"{overdue_pha:,}")

st.markdown("---")

# Visualizations Row
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Deployment Status Breakdown")
    if not filtered_df.empty:
        status_counts = (
            filtered_df["deployable_status"].value_counts().reset_index()
        )
        status_counts.columns = ["Status", "Count"]
        fig_pie = px.pie(
            status_counts,
            names="Status",
            values="Count",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Prism,
        )
        st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("No data available for selected filters.")

with col_right:
    st.subheader("🦷 Dental Classification Impact")
    if not filtered_df.empty:
        dental_counts = (
            filtered_df["dental_class"].value_counts().reset_index()
        )
        dental_counts.columns = ["Dental Class", "Count"]
        fig_bar = px.bar(
            dental_counts,
            x="Dental Class",
            y="Count",
            color="Dental Class",
            color_discrete_sequence=px.colors.qualitative.Bold,
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
        st.info("No data available for selected filters.")

# Detailed Personnel Table View
st.markdown("---")
st.subheader("📋 Unit Member Readiness Records")
st.dataframe(filtered_df, use_container_width=True)
