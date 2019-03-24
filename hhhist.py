import matplotlib.pyplot as plt
import pandas as pd
plt.switch_backend('agg')
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
fig = plt.figure(figsize = (18,18))
ax = fig.gca()
df.hist(ax=ax,bins=30)
plt.savefig('histsum.png')