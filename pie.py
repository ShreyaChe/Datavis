import matplotlib.pyplot as plt
import pandas as pd
plt.switch_backend('agg')
df=pd.read_csv("/home/ubuntu/pucho/indian_liver_patient.csv")
var=df.groupby(['Gender']).sum().stack()
temp=var.unstack()
type(temp)
x_list = temp['Total_Protiens']
label_list = temp.index
plt.axis("equal") #The pie chart is oval by default. To make it a circle use pyplot.axis("equal")
#To show the percentage of each pie slice, pass an output format to the autopctparameter 
plt.pie(x_list,labels=label_list,autopct="%1.1f%%") 
plt.title("Pastafarianism expenses") 
plt.savefig('piech.png')