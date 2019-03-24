import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
plt.switch_backend('agg')
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
plt.figure(figsize=(18,18))
sns.distplot(df.Age)
plt.savefig('hage.png')