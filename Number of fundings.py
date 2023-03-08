import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dict = {}
data = pd.read_csv(r"D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv")
for dates in data.Date:
    x = int(dates[-4:])
    if x in dict:
        dict[x] += 1
    else:
        dict[x] = 1
x = np.array(list(dict.keys()))
y = np.array(list(dict.values()))
plt.plot(x,y)
plt.show()
arg = np.argsort(x)
for r in range(len(x)):
    print(x[arg[r]], y[arg[r]])