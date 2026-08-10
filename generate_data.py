import pandas as pd
import random
from datetime import datetime, timedelta

def generate_mock_records(num_records=150):
    units = ["NAVWAR-DET-1", "NSWC-CORONA", "NIWC-PAC-HQ", "COMNAAVWARSYSCOM", "NECC-LOG-SUP"]
    ranks = ["E-4", "E-5", "E-6", "E-7", "O-1", "O-2", "O-3", "O-4"]
    
    data = []
    base_date = datetime.now()

    for i in range(1, num_records + 1):
        pha_days_ago = random.randint(30, 500)
        dental_class = random.choice([1, 1, 1, 2, 2, 3, 4])
        pha_date = base_date - timedelta(days=pha_days_ago)
        
        is_pha_current = pha_days_ago <= 365
        is_dental_deployable = dental_class in [1, 2]
        temp_profile = random.choices([True, False], weights=[10, 90])[0]
        
        if is_pha_current and is_dental_deployable and not temp_profile:
            readiness_status = "Fully Deployable"
        else:
            readiness_status = "Non-Deployable"
            
        record = {
            "Member_ID": f"ID-{1000 + i}",
            "Unit": random.choice(units),
            "Rank": random.choice(ranks),
            "PHA_Date": pha_date.strftime("%Y-%m-%d"),
            "Dental_Class": f"Class {dental_class}",
            "On_Temporary_Profile": "Yes" if temp_profile else "No",
            "Readiness_Status": readiness_status
        }
        data.append(record)
        
    df = pd.DataFrame(data)
    df.to_csv("synthetic_readiness_data.csv", index=False)
    print("Mock data generated and saved to synthetic_readiness_data.csv")

if __name__ == "__main__":
    generate_mock_records()
