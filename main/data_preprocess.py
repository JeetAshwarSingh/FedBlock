import pandas as pd 
from sklearn.preprocessing import StandardScaler
import random
scaler = StandardScaler()

df = pd.read_csv("data.csv")


def converter (element) -> int :
    if element =="M":
        return 1
    else:
        return 0 


df['diagnosis'] = df['diagnosis'].map(converter)

random_state = random.randint(35,55)
df = df.sample(frac=1, random_state=random_state).reset_index(drop=True)

for element in df.columns.to_list():
    if element != 'diagnosis':
        df[element] = scaler.fit_transform(df[element].values.reshape(-1,1))




df_1 = df[0:189]
df_2 = df[189:378]
df_3 = df[378:567]

df_1.to_csv("hospital_1.csv", index=False)
df_2.to_csv("hospital_2.csv", index=False)
df_3.to_csv("hospital_3.csv", index=False)