# %%
import pandas as pd
import os

def import_etl(path:str):
    name = path.split('/')[-1].split('.')[0]
    df = (pd.read_csv(path, sep=';')
          .rename(columns={'valor':name})
          .set_index(['cod','nome','período'])
          )
    return df

path = "../data/ipea/"
files = os.listdir(path)

dfs = []
for i in files:
    dfs.append(import_etl(path+i))

df_consolidado = pd.concat(dfs,axis=1).reset_index()
df_consolidado.to_csv('../data/consolidado.csv', 
                      sep=';',
                      index=False)
