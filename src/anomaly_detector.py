from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    print("Initializing Isolation Forest Anomaly Detector...")
    
    # We use CPU, RAM, and Network as our training features
    features = df[['cpu_usage_pct', 'ram_usage_pct', 'network_in_mbps']]
    
    # contamination=0.02 tells the model we expect roughly 2% of the data to be anomalous
    model = IsolationForest(n_estimators=100, contamination=0.02, random_state=42)
    
    print("Training model and predicting outliers...")
    # The model returns 1 for normal data, and -1 for anomalies
    df['anomaly_score'] = model.fit_predict(features)
    
    # Map -1 to "Anomaly" and 1 to "Normal" for readability
    df['status'] = df['anomaly_score'].apply(lambda x: 'Anomaly' if x == -1 else 'Normal')
    
    anomalies_found = len(df[df['status'] == 'Anomaly'])
    print(f"Detection complete. Flagged {anomalies_found} abnormal server events.")
    
    return df, model
