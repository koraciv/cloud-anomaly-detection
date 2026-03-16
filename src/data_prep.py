from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StandardScaler

def process_telemetry_pyspark(spark, file_path):
    print("Ingesting telemetry logs via PySpark...")
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    
    print("Assembling metric features into vectors...")
    feature_cols = ['cpu_usage_pct', 'ram_usage_pct', 'network_in_mbps']
    assembler = VectorAssembler(inputCols=feature_cols, outputCol="raw_features")
    df_assembled = assembler.transform(df)
    
    print("Standardizing features for Unsupervised Learning...")
    scaler = StandardScaler(inputCol="raw_features", outputCol="scaled_features", withStd=True, withMean=True)
    scaler_model = scaler.fit(df_assembled)
    df_scaled = scaler_model.transform(df_assembled)
    
    print("Converting processed features to local Pandas DataFrame for scikit-learn...")
    # Extract the scaled arrays back into a Pandas DataFrame
    pandas_df = df_scaled.select("timestamp", "server_id", "cpu_usage_pct", "ram_usage_pct", "network_in_mbps").toPandas()
    
    return pandas_df
