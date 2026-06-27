import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from operations import Blockchain, hospital_data, FederatedModelData
model = LogisticRegression()
df = pd.read_csv("hospital_1.csv")
df = df.drop(columns=['Unnamed: 32'])
X = df.drop(columns=['diagnosis'])
Y = df['diagnosis']
x_train,x_test,y_train,y_test = train_test_split(X,Y,train_size=0.8,random_state=42)
model.fit(x_train,y_train)
m_coeff_1 = model.coef_
m_inter_1 = model.intercept_

if __name__ == "__main__":
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.2f}\n")

    print("--- Classification Report ---")
    print(classification_report(y_test, y_pred))

    print("--- Confusion Matrix ---")
    print(confusion_matrix(y_test, y_pred))

    print(m_coeff_1,m_inter_1)
    hospital1 = hospital_data("Apollo", 101, {'m_coeff': m_coeff_1, 'm_inter': m_inter_1})
    blockchain = Blockchain(difficulty=2)

    hospital_list = [hospital1.get_hospital_weight()]
    fed_avg = FederatedModelData(hospital_list)

    data = f"Hospital: {hospital1.hospital_name}, Weights: {hospital_list}, Fed Avg: {fed_avg.get_avg()}"
    blockchain.add_block(data=data)

    print("Node 1 Block:")
    print(blockchain.get_last_block())