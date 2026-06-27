FedBlock -> Federated Learning with Blockchain Auditability

A privacy preserving system for collaborative medical AI, built across three hospital nodes using Federated Averaging and a custom blockchain for audit logging.


What this project does

Hospitals sit on some of the most valuable data in the world for training diagnostic AI — and almost none of it can be shared. Privacy laws, patient ethics, institutional liability: the barriers are real and legitimate. The result is that most healthcare AI is trained on whatever one institution happens to have, which is rarely enough.

FedBlock takes a different approach. Instead of pooling data, it pools learning. Each hospital trains a local model on its own private patient records. Only the model weights not the underlying data are sent to a central server, which aggregates them using Federated Averaging and records every round immutably on a blockchain. The raw data never moves. The model improves as if it had seen everything.

This was built and tested on the Wisconsin Breast Cancer Dataset across three simulated hospital nodes, and the accuracy came out competitive with a centrally trained baseline which is the whole point.


Architecture

+------------------+    +------------------+    +------------------+
|   Hospital 1     |    |   Hospital 2     |    |   Hospital 3     |
| (hospital_1.py)  |    | (hospital_2.py)  |    | (hospital_3.py)  |
|                  |    |                  |    |                  |
|  Trains locally  |    |  Trains locally  |    |  Trains locally  |
|  on private data |    |  on private data |    |  on private data |
+--------+---------+    +--------+---------+    +--------+---------+
         |                       |                        |
         |     model weights only — no raw data           |
         +-----------------------+------------------------+
                                 |
                                 v
                   +---------------------------+
                   |     Blockchain Server     |
                   |   (blockchain_update.py)  |
                   |                           |
                   |  1. Collect weight        |
                   |     updates from nodes    |
                   |  2. Run FedAvg            |
                   |  3. Record round on       |
                   |     the blockchain        |
                   |  4. Send global model     |
                   |     back to all nodes     |
                   +---------------------------+

Each round works the same way: local training happens in parallel across nodes, weights are sent to the server, FedAvg produces a new global model, and that round is permanently logged on-chain before the updated model is broadcast back.

Project structure

fedBlock/
| 
+-- juypter notebook           # doesnt play any role in blockchain was used while building the blockchain used for rapid testing and validation
+-- data_preprocessing.py      # dividing the dataset into three distinct dataset so different hospital can train on it
+-- operations.py              # has all the necessary classes required for the functioning of the blockchain
+-- hospital_1.py              # Node 1 — local training and weight transmission
+-- hospital_2.py              # Node 2 — local training and weight transmission
+-- hospital_3.py              # Node 3 — local sraining and weight transmission
|
+-- blockchain_update.py       # Central server — FedAvg aggregation and blockchain logging
|

How it works
Local training

Each hospital script loads its partition of the dataset, trains a classifier independently, and sends only the resulting model weights to the server. The data itself goes nowhere.

Federated Averaging
The server receives weights from all three nodes and computes a weighted average proportional to each node's dataset size:
This produces a global model that reflects the collective learning of all three hospitals without any of them seeing each other's data.

Blockchain logging
After each aggregation round, a new block is appended to the chain. It contains the round number, timestamp, a hash of the aggregated weights, the IDs of all contributing nodes, and the hash of the previous block. This makes the contribution history tamper-evident — you can verify exactly who contributed what and when, and any retroactive modification breaks the chain.
The federated model performs on par with a centrally trained model, demonstrating that the privacy-preserving setup does not require sacrificing much in the way of predictive quality.

Privacy and compliance
The system was designed with HIPAA, GDPR, and India's DPDP Act in mind. The short version: no patient data ever leaves a hospital node. Only model weights travel over the network, and every interaction between nodes is logged permanently on the blockchain. There is no point in the pipeline where a single entity has access to all the raw data.


Tech stack
Python
scikit-learn / NumPy
Custom blockchain (built from scratch)

dataset used for simulation
Wisconsin Breast Cancer Dataset (UCI)
