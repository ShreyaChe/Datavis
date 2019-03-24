import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.switch_backend('agg')
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
plt.figure(figsize=(14,14))
df.Albumin_and_Globulin_Ratio = pd.to_numeric(df.Albumin_and_Globulin_Ratio,errors='coerce').fillna(0)
sns.distplot(df.Total_Protiens[df.Dataset==2],label='No Disease',color='blue')
sns.distplot(df.Total_Protiens[df.Dataset==1],label='Disease',color='Red')
sns.distplot(df.Albumin[df.Dataset==2],label='No Disease',color='Green')
sns.distplot(df.Albumin[df.Dataset==1],label='Disease',color='violet')
plt.legend()
plt.savefig('disnodis.png')