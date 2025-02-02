# %%

import pandas as pd

# %%

df_customer = pd.read_csv("../data/customers.csv", sep=';')
df_customer
# %%

df_customer.shape
# %%

#info da memoria usada
df_customer.info(memory_usage='deep')
# %%

df_customer['Points'].describe()
# %%

df_customer['Points'].astype(int)
# %%

# operação vetorial (aplicação de filtros no pandas)
condicao = df_customer['Points'] > 1000
df_customer[condicao]

# %%

# pegamos o valor maximo (4304)
maximo = df_customer['Points'].max()

# vou agora pegar uma condicao de booleanos e achar quem tem esse valor
condicao_max = df_customer['Points'] == maximo

# aplicar o filtro e achar a posição
df_customer[condicao_max]

# %%

# mais comum a condição lógica estar na posição
df_customer[df_customer['Points'] == df_customer['Points'].max()]['Name'].iloc[0]

 # %%

condicao_max = df_customer['Points'] == df_customer['Points'].max()
df_maior = df_customer[condicao_max]
df_maior['Name'].iloc[0]

# %%

condicao_intervalo = (df_customer['Points'] >= 1000) & (df_customer['Points'] <= 2000)

df_1000_2000 = df_customer[condicao_intervalo].copy()

# tenho que fazer uma copia do filtro pois vou alterar o dataframe
# original se não fizer a copia
df_1000_2000['Points'] = df_1000_2000['Points'] + 1000

df_1000_2000.shape
 
# %%

df_customer
# %%

df_customer[['Name','Points']]
# %%

#ordenar em ordem alfabética
colunas = df_customer.columns.tolist()
colunas.sort()
colunas

# aqui só estamos papssando a lista de colunas de maneira ordenada
# sem alterar o df original
df_customer[colunas]

df_customer = df_customer[colunas]
df_customer

# %%

# o rename gera um dataframe novo
df_customer = df_customer.rename(columns={"Name": "Nome", "Points":"Pontos"})
df_customer
# %%

# já muda direto no dataframe 
df_customer.rename(columns={"UUID":'Id'}, inplace=True)
df_customer
# %%


