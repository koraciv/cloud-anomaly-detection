import pandas as pd
import numpy as np
import os

def generate_telemetry_data(file_path, num_records=10000, anomaly_rate=0.02):
    print("Simulating cloud infrastructure telemetry (STACKIT environment)...")
    np.random.seed(42)
    
    # 1. Generate Normal Server Behavior
    cpu_usage = np.random.normal(loc=30.0, scale=10.0, size=num_records)  # 30% average CPU
    ram_usage = np.random.normal(loc=50.0, scale=15.0, size=num_records)  # 50% average RAM
    network_in = np.random.normal(loc=100.0, scale=20.0, size=num_records) # MB/s
    
    # Constrain to realistic boundaries
    cpu_usage = np.clip(cpu_usage, 0, 100)
    ram_usage = np.clip(ram_usage, 0, 100)
    network_in = np.clip(network_in, 0, 1000)
    
    df = pd.DataFrame({
        'timestamp': pd.date_range(start='2024-01-01', periods=num_records, freq='T'),
        'server_id': np.random.choice(['server_A', 'server_B', 'server_C', 'server_D'], num_records),
        'cpu_usage_pct': cpu_usage,
        'ram_usage_pct': ram_usage,
        'network_in_mbps': network_in
    })
    
    # 2. Inject Anomalies (e.g., DDoS attacks or memory leaks)
    num_anomalies = int(num_records * anomaly_rate)
    anomaly_indices = np.random.choice(df.index, num_anomalies, replace=False)
    
    print(f"Injecting {num_anomalies} anomalies (CPU/RAM/Network spikes)...")
    df.loc[anomaly_indices, 'cpu_usage_pct'] = np.random.uniform(90, 100, num_anomalies)
    df.loc[anomaly_indices, 'ram_usage_pct'] = np.random.uniform(90, 100, num_anomalies)
    df.loc[anomaly_indices, 'network_in_mbps'] = np.random.uniform(800, 1000, num_anomalies)
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    print(f"Telemetry log saved to {file_path}")
    return df
