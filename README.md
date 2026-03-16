# Cloud Infrastructure Anomaly Detection (PySpark & Isolation Forest)

## 📌 Project Overview
Operating sovereign cloud infrastructure (such as STACKIT) requires monitoring thousands of virtual machines and bare-metal servers. Hardware degradation, memory leaks, and cybersecurity threats (like DDoS attacks) manifest as anomalies in server telemetry.

This project implements an **Unsupervised Machine Learning Pipeline** to automatically detect abnormal server behavior. It utilizes **PySpark** to ingest and standardize high-volume server telemetry (CPU, RAM, Network I/O) and trains a **scikit-learn Isolation Forest** to isolate and flag critical infrastructural anomalies without requiring labeled training data.

**Business Value:** Enhances Site Reliability Engineering (SRE) and cybersecurity threat hunting by shifting from manual, rule-based alerts to automated, AI-driven anomaly detection, ensuring high availability for enterprise cloud operations.

## 🛠️ Tech Stack
* **Big Data Engineering:** Apache Spark (PySpark SQL, MLlib Feature Scaling)
* **Machine Learning:** scikit-learn (Isolation Forest - Unsupervised Learning)
* **Data Manipulation:** Pandas, NumPy
* **Language:** Python 3.x

## 🏗️ Architecture & Workflow
1. **Telemetry Simulation:** Generates synthetic, high-resolution server logs simulating baseline operations and injecting complex, multi-variate anomalies (e.g., simultaneous CPU and Network spikes).
2. **Distributed Processing:** Employs PySpark's `VectorAssembler` and `StandardScaler` to ingest, scale, and prepare the multidimensional telemetry data for mathematical modeling.
3. **Unsupervised Detection:** Trains an Isolation Forest algorithm to detect outliers. Unlike simple threshold alerts (e.g., "Alert if CPU > 90%"), this model detects complex anomalies across multiple dimensions simultaneously.
4. **Threat Flagging:** Outputs a structured report isolating compromised or failing servers for immediate SRE or SOC (Security Operations Center) review.

## 📂 Project Structure
```text
├── data/                   # Data directory (Simulated telemetry excluded via .gitignore)
├── src/                    
│   ├── telemetry_simulator.py # Generates synthetic STACKIT server logs
│   ├── data_prep.py        # PySpark ingestion and standard scaling
│   ├── anomaly_detector.py # scikit-learn Isolation Forest training
│   └── main.py             # Pipeline orchestrator
├── requirements.txt        # Python dependencies
├── .gitignore              # Ignored files and directories
└── README.md               # Project documentation
