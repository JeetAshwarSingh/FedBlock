# FedBlock – Federated Learning with Blockchain Auditability

A privacy-preserving system for collaborative medical AI built across three hospital nodes using **Federated Averaging (FedAvg)** and a **custom blockchain** for immutable audit logging.

---

## What This Project Does

Hospitals possess some of the world's most valuable data for training diagnostic AI models, yet privacy regulations, ethical concerns, and institutional policies prevent them from sharing patient records. As a result, many healthcare AI models are trained on data from a single institution, limiting their generalizability.

**FedBlock** addresses this challenge through **Federated Learning**.

Instead of sharing patient data, each hospital trains a model locally on its own private dataset. Only the trained model weights—not the underlying patient records—are transmitted to a central server. The server aggregates these weights using the **Federated Averaging (FedAvg)** algorithm and records every aggregation round on a blockchain, creating a tamper-evident audit trail.

Throughout the entire process:

* Patient data never leaves the hospital.
* Only model parameters are exchanged.
* Every federated learning round is permanently recorded on-chain.

This project was evaluated using the **Wisconsin Breast Cancer Dataset**, partitioned across three simulated hospital nodes. The federated model achieved performance comparable to a centrally trained model while preserving data privacy.

---

## System Architecture

```text
+------------------+    +------------------+    +------------------+
|   Hospital 1     |    |   Hospital 2     |    |   Hospital 3     |
| (hospital_1.py)  |    | (hospital_2.py)  |    | (hospital_3.py)  |
|                  |    |                  |    |                  |
|  Trains locally  |    |  Trains locally  |    |  Trains locally  |
|  on private data |    |  on private data |    |  on private data |
+--------+---------+    +--------+---------+    +--------+---------+
         |                       |                        |
         |     Model weights only (no raw patient data)  |
         +-----------------------+------------------------+
                                 |
                                 v
                  +-----------------------------+
                  |     Blockchain Server       |
                  | (blockchain_update.py)      |
                  |                             |
                  | • Collect local weights     |
                  | • Run FedAvg aggregation    |
                  | • Log round on blockchain   |
                  | • Broadcast global model    |
                  +-----------------------------+
```

Each training round follows the same workflow:

1. Every hospital trains its model locally.
2. Model weights are sent to the central server.
3. The server performs **Federated Averaging**.
4. The aggregation round is recorded on the blockchain.
5. The updated global model is distributed back to all participating hospitals.

---

## Project Structure

```text
FedBlock/
│
├── jupyter_notebook.ipynb       # Used during blockchain development for testing and validation
├── data_preprocessing.py        # Splits the dataset into three hospital partitions
├── operations.py                # Blockchain classes and utility functions
├── hospital_1.py                # Hospital Node 1
├── hospital_2.py                # Hospital Node 2
├── hospital_3.py                # Hospital Node 3
│
└── blockchain_update.py         # Central server: FedAvg aggregation + blockchain logging
```

---

## How It Works

### 1. Local Training

Each hospital loads its assigned dataset partition, trains a local machine learning model independently, and transmits **only the learned model weights** to the central server.

No patient data is shared.

---

### 2. Federated Averaging (FedAvg)

The server receives model weights from all participating hospitals and computes a weighted average based on the size of each local dataset.

The resulting global model benefits from knowledge learned across all hospitals while ensuring that no institution ever accesses another's private data.

---

### 3. Blockchain Logging

After every aggregation round, a new block is appended to the blockchain containing:

* Round number
* Timestamp
* Hash of the aggregated model weights
* IDs of participating hospital nodes
* Previous block hash

This creates a tamper-evident audit trail. Any attempt to modify historical records invalidates the blockchain, making every contribution verifiable.

---

## Privacy and Compliance

The system is designed around privacy-by-design principles and aligns with the goals of regulations such as:

* HIPAA
* GDPR
* India's DPDP Act

Key privacy guarantees include:

* Patient data never leaves a hospital.
* Only model parameters are transmitted.
* Every communication between participants is immutably logged.
* No central authority ever has access to all raw patient data.

---

## Results

The federated model achieved performance comparable to a centrally trained model, demonstrating that strong privacy guarantees can be maintained without significantly compromising predictive accuracy.

---

## Tech Stack

* Python
* scikit-learn
* NumPy
* Custom blockchain implementation

---

## Dataset

**Wisconsin Breast Cancer Dataset (UCI Repository)**

Used to simulate three independent hospitals participating in federated learning.

## Contributing

Pull requests are welcome. If you are planning something substantial, open an issue first so we can discuss the direction before you write the code.

---

**Hospitals should not have to choose between protecting their patients and improving their diagnostic tools. This is one attempt at making both possible simultaneously.**
