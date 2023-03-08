import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dict = {}
data = pd.read_csv(r"D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv")
data.CityLocation.str.lower()
cities = data.CityLocation.value_counts().index.to_list()[:10]
for city in data.CityLocation:
    if city in cities:
        if city in dict:
            dict[city] += 1
        else:
            dict[city] = 1
plt.pie(dict.values(), labels = dict.keys(), autopct = '%.2f%%')
plt.show()
x = np.array(list(dict.values()))
y = np.array(list(dict.keys()))
arg = np.argsort(x)
arg = np.flip(arg)
for rows in range(len(x)):
    print(y[arg[rows]], x[arg[rows]])