import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dict = {}
dictpct = {}
data = pd.read_csv(r"D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv")
data.AmountInUSD.fillna(0, inplace = True)
for row in data.index:
    industry = data['IndustryVertical'][row]
    j = data[data.index == row].AmountInUSD.tolist()[0]
    if type(j) == str:
        J = j.replace(',','')
    else:
        J = j
    if industry in dict:
        dict[industry] += float(int(J))
    else:
        dict[industry] = float(int(J))
newdict = {}
for i in range(5):
    newdict[list(dict.keys())[i]] = list(dict.values())[i]
plt.pie(newdict.values(), labels = newdict.keys(), autopct = '%.2f%%')
plt.show()
fund = np.array(list(newdict.values()))
arg = np.argsort(fund)
Arg = np.flip(arg)
Fund = fund[Arg]
ind = np.array(list(newdict.keys()))
Ind = ind[Arg]
print(Fund, Ind)
S = sum(Fund)
for r in range(5):
    dictpct[Ind[r]] = round((Fund[r] / S)*100 , 2)
for r in range(5):
    print(list(dictpct.keys())[r], list(dictpct.values())[r],'%')