# Military Health Information Governance & Readiness System

An end-to-end data pipeline and application engineered for executive command oversight, featuring automated ETL pipelines and HIPAA/DoD-compliant PHI security layers.

## 🚀 Key Architectural Features
- **Automated ETL Pipeline (`etl_pipeline.py`):** Extracts, transforms, and loads synthetic health records, ensuring data cleanliness, schema validation, and normalization.
- **Synthetic Data Generation (`generate_data.py`):** Programmatically generates realistic, compliant mock military readiness and medical status records for testing and analysis.
- **Interactive Command Dashboard (`app.py`):** Built with Streamlit to provide real-time visualization of medical readiness metrics, deployment statuses, and unit availability.
- **Secure Data Storage (`readiness.db`):** Uses a structured SQLite relational backend designed to maintain data integrity and support analytical queries.

---

## 🛠️ Project Structure
- **`app.py`**: The Streamlit user interface application for leadership dashboards.
- **`etl_pipeline.py`**: The core data processing script handling transformations and database loading.
- **`generate_data.py`**: Script responsible for generating synthetic dataset distributions.
- **`synthetic_readiness_data.csv`**: The raw export source file for pipeline processing.
- **`readiness.db`**: The local relational database storing processed operational metrics.

---

## 💻 How to Run Locally

1. Clone the repository and navigate into it using your terminal.

2. Install dependencies:
   ```bash
   pip install streamlit pandas
   python generate_data.py
   python etl_pipeline.py
   streamlit run app.py
