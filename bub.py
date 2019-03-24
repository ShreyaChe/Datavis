import matplotlib.pyplot as plt
import pandas as pd
plt.switch_backend('agg')
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(df['Age'],df['Total_Bilirubin'], s=df['Dataset']) # Added third variable income as size of the bubble
plt.savefig('bub.png')