import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
fig=plt.figure()
ax=fig.add_subplot(1,1,1)# add 1*1 grid first subplot
ax.hist(df['Age'],bins=10)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Patients')
plt.savefig('age.png')

