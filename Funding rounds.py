import numpy as np
import pandas as pd
dict = {}
data = pd.read_csv(r'D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv')
data["StartupName"].replace("Flipkart.com","Flipkart",inplace = True)
data["StartupName"].replace("Ola Cabs","Ola",inplace = True)
data["StartupName"].replace("Olacabs","Ola",inplace = True)
data["StartupName"].replace("Oyorooms","Oyo",inplace = True)
data["StartupName"].replace("OyoRooms","Oyo",inplace = True)
data["StartupName"].replace("OYO Rooms","Oyo",inplace = True)
data["StartupName"].replace("Oyo Rooms","Oyo",inplace = True)
data["StartupName"].replace("Paytm Marketplace","Paytm",inplace = True)
for n in data.StartupName:
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
l = np.array(list(dict.values()))
arg = np.argsort(l)
Arg = np.flip(arg)
s = np.array(list(dict.keys()))
for a in range(5):
    print(s[Arg[a]], l[Arg[a]])