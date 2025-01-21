import pandas as pd
import numpy as np


#consider this code for generating synthetic datasets
#1.Run this code manually and then dataset file (csv) will be added to project directory
#2.use it in postman for sample dataset for training model purposes



def generate_synthetic_data(num_rows=1000):
    np.random.seed(42)
    data = {
        'product_id': np.random.randint(1, 101, num_rows),
        'defect_type': np.random.choice(["Minor", "Major"], size=num_rows),
        'severity': np.random.normal(loc=75, scale=10, size=num_rows),
        'inspection_method': np.random.uniform(low=100, high=500, size=num_rows),
        'repair_cost': np.random.uniform(low=50, high=200, size=num_rows),
        'defect_id': np.random.randint(0, 2, num_rows)
    }
    return pd.DataFrame(data)

# Generate 1000 rows of synthetic data
synthetic_df = generate_synthetic_data(1000)

# Save as CSV file
synthetic_df.to_csv('dynamic_synthetic_data.csv', index=False)
