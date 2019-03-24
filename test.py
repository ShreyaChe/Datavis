#import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.switch_backend('agg') 
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.savefig('plt.png')
