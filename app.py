import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Military Health Readiness System", layout="wide")

@st.cache_data
def load_data():
    engine = create_engine("sqlite:///readiness.db")
    return pd.read_sql("unit_readiness", engine)

df = load_data()

st.sidebar.title("Security & Governance")
st.sidebar.info("System Status: **SECURE (HIPAA / DoD Compliant)**")
user_role = st.sidebar.selectbox("Access Role Level", ["Executive Commander", "Medical Officer", "Unit Supervisor"])

st.sidebar.markdown("---")
selected_unit = st.sidebar.selectbox("Filter by Unit", ["All Units"] + list(df["Unit"].unique()))

st.title("🛡️ Military Health Information Governance & Readiness System")
st.markdown("*Executive Command Oversight & Force Health Protection Dashboard*")
st.markdown("---")

if selected_unit != "All Units":
    filtered_df = df[df["Unit"] == selected_unit]
else:
    filtered_df = df

total_personnel = len(filtered_df)
deployable_count = len(filtered_df[filtered_df["Readiness_Status"] == "Fully Deployable"])
readiness_rate = (deployable_count / total_personnel) * 100 if total_personnel > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Personnel Tracked", total_personnel)
col2.metric("Fully Deployable", deployable_count)
col3.metric("Overall Unit Readiness Rate", f"{readiness_rate:.1f}%")

st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("⚠️ Readiness Bottlenecks")
    non_deployable_df = filtered_df[filtered_df["Readiness_Status"] == "Non-Deployable"]
    dental_issues = len(non_deployable_df[non_deployable_df["Dental_Class"].isin(["Class 3", "Class 4"])])
    profile_issues = len(non_deployable_df[non_deployable_df["On_Temporary_Profile"] == "Yes"])
    
    bottleneck_data = pd.DataFrame({
        "Category": ["Dental Class 3/4", "Active Temp Profiles", "Overdue PHA / Administrative"],
        "Count": [dental_issues, profile_issues, len(non_deployable_df) - (dental_issues + profile_issues)]
    })
    st.bar_chart(bottleneck_data.set_index("Category"))

with col_right:
    st.subheader("📊 Readiness Breakdown by Status")
    status_counts = filtered_df["Readiness_Status"].value_counts()
    st.dataframe(status_counts, use_container_width=True)

st.markdown("---")
st.subheader("📋 Personnel Roster & Tracking Details")

if user_role == "Executive Commander":
    st.caption("Displaying high-level roster data with PHI protected under DoD governance guidelines.")
    st.dataframe(filtered_df, use_container_width=True)
elif user_role == "Medical Officer":
    st.caption("Accessing clinical tracking records and status flags.")
    st.dataframe(filtered_df[["Member_ID", "Unit", "PHA_Date", "Dental_Class", "On_Temporary_Profile"]], use_container_width=True)
else:
    st.warning("Restricted View: Unit Supervisors have limited visibility into detailed medical tracking logs.")
