import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;sns.set()
#matplotlib inline
plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')
dataset=pd.read_csv('customer.csv')
dataset.head()
