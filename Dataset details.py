import pandas as pd
import numpy as np
data = pd.read_csv(r"D:\Data Science\[CN] Data Science\14. Project - Case Study (Part - I)\startup_funding.csv")
print(data.IndustryVertical.mode())
print(data['InvestorsName'].value_counts().index.tolist()[2])
print(data.SubVertical.mode())