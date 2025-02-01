# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%

df = pd.read_csv("../data/customers.csv", sep=';')

# %%

# posso passar uma lista para ordenar os valores, tanto na coluna quanto no asc
df.sort_values(by=['Points','Name'], 
               ascending=[False,True])


# %%
# ordenação (não altera o df) - cria um df novo ordenado
df.sort_values(by='Points', ascending=False, inplace=True)
df.rename(columns={'Name':'Nome','Points':'Pontos'},inplace=True)
df

# %%

# o sort retorna un nov df por isso empilhamos o rename (sem o inplace)
df = (df.sort_values(by='Pontos', ascending=False)
      .rename(columns={'Nome':'Name','Pontos':'Points'}))

# %%

df = (df.sort_values(by=['Points','Name'], 
               ascending=[False,True])
        .rename(columns={'Nome':'Name','Pontos':'Points'}))

df
# %%
