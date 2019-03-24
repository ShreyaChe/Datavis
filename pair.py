import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
plt.switch_backend('agg')
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
plt.figure(figsize=(14,14))
print(df.info())
sns.pairplot(df[['Age','Total_Bilirubin','Direct_Bilirubin','Alkaline_Phosphotase','Alamine_Aminotransferase','Total_Protiens','Albumin','Dataset']])
plt.savefig('pair.png')