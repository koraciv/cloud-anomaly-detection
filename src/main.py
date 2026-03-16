import os
from pyspark.sql import SparkSession
from telemetry_simulator import generate_telemetry_data
from data_prep import process_telemetry_pyspark
from anomaly_detector import detect_anomalies

def run_infrastructure_pipeline():
    data_path = "../data/server_telemetry.csv"
    
    # 1. Simulate Cloud Telemetry
    generate_telemetry_data(data_path, num_records=10000, anomaly_rate=0.02)
    
    spark = SparkSession.builder \
        .appName("STACKIT_Anomaly_Detection") \
        .config("spark.driver.memory", "4g") \
        .getOrCreate()

    try:
        # 2. Distributed Feature Engineering
        processed_df = process_telemetry_pyspark(spark, data_path)
        
        # 3. Unsupervised Machine Learning
        analyzed_df, model = detect_anomalies(processed_df)
        
        # 4. Reporting
        print("\n================ THREAT & HARDWARE MONITORING REPORT ================")
        anomalies = analyzed_df[analyzed_df['status'] == 'Anomaly']
        print("Sample of Detected Anomalies (Potential DDoS or Hardware Failure):")
        # Print the first 5 anomalies to show what the model caught
        print(anomalies[['timestamp', 'server_id', 'cpu_usage_pct', 'network_in_mbps']].head(5))
        print("=====================================================================")

    except Exception as e:
        print(f"\nPipeline failed: {e}")
    finally:
        spark.stop()

if __name__ == "__main__":
    run_infrastructure_pipeline()
