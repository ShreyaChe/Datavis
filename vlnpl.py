import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd
import seaborn as sns
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
ax=sns.violinplot(df['Age'],df['Gender'])
#sns.despine()
fig = ax.get_figure()
fig.savefig('vlnpng.png')