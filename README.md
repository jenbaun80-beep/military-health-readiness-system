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
