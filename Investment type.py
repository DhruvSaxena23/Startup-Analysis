import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
pctdict = {}
dict = {}
data = pd.read_csv(r"D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv")
data.replace("Crowd funding","Crowd Funding", inplace = True)
data.replace("PrivateEquity","Private Equity", inplace = True)
data.replace("SeedFunding","Seed Funding", inplace = True)
for row in data.InvestmentType:
    if row in dict:
        dict[row] += 1
    else:
        dict[row] = 1
plt.pie(dict.values(), labels = dict.keys(), autopct = "%.2f%%")
plt.show()
sum = sum(dict.values())
for a in dict.keys():
    pctdict[a] = round((dict[a]/sum)*100 ,2)
keys = np.array(list(pctdict.keys()))
values = np.array(list(pctdict.values()))
arg = np.argsort(values)
narg = np.flip(arg)
for r in range(len(pctdict.keys())):
    print(keys[narg[r]], values[narg[r]],"%")