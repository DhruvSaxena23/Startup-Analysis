import pandas as pd
import matplotlib.pyplot as plt
dict = {}
pctdict = {}
data = pd.read_csv(r"D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv")
data.CityLocation.str.lower()
data.AmountInUSD.fillna(0, inplace = True)
for n in data.index:
    x = data[data.index == n]["CityLocation"].tolist()[0]
    j = data[data.index == n].AmountInUSD.tolist()[0]
    if type(j) == str:
        J = j.replace(',','')
    else:
        J = j
    if x in dict:
        dict[x] += int(float(J))
    else:
        dict[x] = int(float(J))
plt.pie(dict.values(), labels=dict.keys(), autopct = '%.2f%%')
plt.show()
sum = sum(dict.values())
for a in dict.keys():
    pctdict[a] = (dict[a]/sum)*100
keys = list(pctdict.keys())
values = list(pctdict.values())
for r in range(len(pctdict.keys())):
    print(keys[r], values[r],"%")