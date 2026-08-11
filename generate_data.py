import pandas as pd
import numpy as np

def generate_mock_readiness_data(num_records=500):
    np.random.seed(42)
    units = ['1st Marine Division', '3rd Fleet', 'SEAL Team 1', 'Camp Pendleton Base Operations', 'Naval Medical Center San Diego']
    statuses = ['Fully Mission Capable', 'Deployment Ready', 'Medical Hold', 'Requires Re-evaluation']
    
    data = {
        'service_id': [f'USN-{np.random.randint(10000, 99999)}' for _ in range(num_records)],
        'unit': np.random.choice(units, num_records),
        'readiness_status': np.random.choice(statuses, num_records, p=[0.5, 0.3, 0.15, 0.05]),
        'immunization_compliant': np.random.choice([1, 0], num_records, p=[0.92, 0.08]),
        'dental_class': np.random.choice(['Class 1', 'Class 2', 'Class 3'], num_records, p=[0.7, 0.2, 0.1]),
        'last_phra_date': pd.to_datetime('2026-01-01') - pd.to_timedelta(np.random.randint(0, 365, num_records), unit='d')
    }
    
    df = pd.DataFrame(data)
    df.to_csv('military_health_raw.csv', index=False)
    print("Synthetic military health raw data generated successfully.")

if __name__ == '__main__':
    generate_mock_readiness_data()
