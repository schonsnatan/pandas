# %%

import pandas as pd
import numpy as np
# %%

df = pd.read_csv('../data/customers.csv', sep=';')
df
# %%

# criando coluna com produto escalar
df['Points_double'] = df['Points'] * 2
df
# %%

df['Points_ratio'] = df['Points_double'] / df['Points']
# %%
df
# %%

df['Constante'] = 1
# %%
df
# %%
df['Points_log'] = np.log(df['Points'])

# %%
df
# %%

df['Name'].str.upper()
df
# %%

def get_first(nome:str):
    nome = nome.upper()
    return nome.split("_")[0]

# apply aplica uma função em todas as linhas da série
df["Name_first"] = df['Name'].apply(get_first)
# %%
df
# %%

get_f = lambda nome: nome.split("_")[0]
get_f("Natan_Schons")

# %%
# função quando usamos uma vez
df['Name'].apply(lambda x: x.upper().split('_')[0])
# %%

def intervalo_pontos(pontos):
    if pontos < 2500:
        return "baixo"
    elif pontos < 3500:
        return "medio"
    else:
        return "alto"
    
df['Faixa_Ponots'] = df['Points'].apply(intervalo_pontos)
df
# %%

df['UUID'].apply(lambda x: x[-3:])
# %%

# RVM Marketing
data = {
    "nome":['Teo','Nah','Maria','Lara'],
    'recencia':[1,30,10,45],
    'valor':[100,2000,15,500],
    'frequencia':[2,5,1,15]
}

df_crm = pd.DataFrame(data)
df_crm
# %%

def rfv(row):
     nota = 0

     if row['recencia'] <= 10:
        nota += 10
     elif 10 < row['recencia'] <= 30:
        nota += 5
     elif row['recencia'] > 30:
        nota += 0

     if row['valor'] > 1000:
        nota += 10
     elif 100 <= row['valor'] < 1000:
        nota += 5
     elif row['valor'] < 100:
        nota += 0

     if row['frequencia'] > 10:
        nota += 10
     elif 5 <= row['frequencia'] < 10:
        nota += 5
     elif row['frequencia'] < 5:
        nota += 0

     return nota