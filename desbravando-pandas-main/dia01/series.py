# %%
import pandas as pd


# %%

idades = [30, 42, 90, 34]
idades
# %%

media = sum(idades) / len(idades)

#Desvio padrão (Variancia)

total = 0
for i in idades:
    total += (media - i)**2
variancia = total / len(idades) - 1

desvio_padrao = variancia**(1/2)
desvio_padrao

# %%

#Series
series_idades = pd.Series(idades)
series_idades
# %%

#Variância
series_idades.var()

# %% 

#Desvio padrão
desvio = series_idades.std()
# %%

#1o quartil
series_idades.quantile(0.25)

#3o quartil
series_idades.quantile(0.75)

# %%

#Sumarização
series_idades.describe() #diversas infos
# %%

#Mediana - 2o quartil
series_idades.median()
# %%

#Dimensão da série
series_idades.shape
# %%

#Navegação da lista
idades[0]
# %%

#posso alterar os índices
series_idades.index = [40, 10, 30, 20]
# %%

#Forma explícita da posição da série
series_idades.iloc[0:2]
# %%

#Acessando por índice
series_idades.loc[40]
# %%

#Dando nome à série
series_idades.name = 'idades'
series_idades = pd.Series(idades, name='Idades')
series_idades
# %%