import matplotlib
matplotlib.use('Agg')
import seaborn as sns;sns.set()
import pandas as pd
import matplotlib.pyplot as plt
dataset=pd.read_csv('/home/ubuntu/pucho/customer.csv')
plot_income= sns.distplot(dataset["Annual Income (k$)"])
plot_spend=sns.distplot(dataset["Spending Score (1-100)"])
plt.xlabel('Income/spend')
f,axes = plt.subplots(1,2,figsize=(12,6),sharex=True,sharey=True)
v1=sns.violinplot(data=dataset,x='Annual Income (k$)',color="skyblue",ax=axes[0])
v2=sns.violinplot(data=dataset,x='Spending Score (1-100)',color="lightgreen",ax=axes[1])
v1.set(xlim=(0,420))
plt.show()

