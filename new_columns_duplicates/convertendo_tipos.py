# %%
import pandas as pd

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df.dtypes
# %%

#posso passar lista de valores
df['Points'].astype(str)