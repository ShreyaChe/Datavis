import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.switch_backend('agg')
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
plt.figure(figsize=(14,14))
sns.barplot(x='Dataset',y='Age',data=df)
plt.savefig('aged.png')