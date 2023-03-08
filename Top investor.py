import numpy as np
import pandas as pd
dict = {}
data = pd.read_csv(r"D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv")
data.InvestorsName.fillna("nill", inplace = True)
data["InvestorsName"] = data["InvestorsName"].str.replace(", ","^")
data["InvestorsName"] = data["InvestorsName"].str.replace(",","^")
for inv in data.InvestorsName:
    lis = inv.split("^")
    for ele in lis:
        if ele in dict:
            dict[ele] += 1
        else:
            dict[ele] = 1
keys = np.array(list(dict.keys()))
value = np.array(list(dict.values()))
x = np.argmax(value)
print(keys[x], value[x])