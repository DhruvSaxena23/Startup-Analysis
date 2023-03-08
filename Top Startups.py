import numpy as np
import pandas as pd
dict = {}
data = pd.read_csv(r'D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv')
data.AmountInUSD.fillna(0, inplace = True)
data["StartupName"].replace("Flipkart.com","Flipkart",inplace = True)
data["StartupName"].replace("Ola Cabs","Ola",inplace = True)
data["StartupName"].replace("Olacabs","Ola",inplace = True)
data["StartupName"].replace("Oyorooms","Oyo",inplace = True)
data["StartupName"].replace("OyoRooms","Oyo",inplace = True)
data["StartupName"].replace("OYO Rooms","Oyo",inplace = True)
data["StartupName"].replace("Oyo Rooms","Oyo",inplace = True)
data["StartupName"].replace("Paytm Marketplace","Paytm",inplace = True)
for n in data.index:
    x = data.StartupName[n]
    j = data.AmountInUSD[n]
    if type(j) == str:
        J = j.replace(',', '')
    else:
        J = j
    if x in dict:
        dict[x] += float(int(J))
    else:
        dict[x] = float(int(J))
l = np.array(list(dict.values()))
arg = np.argsort(l)
Arg = np.flip(arg)
s = np.array(list(dict.keys()))
for a in range(5):
    print(s[Arg[a]])