'''
Converta a seguinte lista de dados para uma Series Pandas 
e obtenha:

Média
Desvio Padrão
Máximo Valor

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

'''

# %%
import pandas as pd

# %%

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]

series_dados = pd.Series(dados)
series_dados
# %%
series_dados.mean()
# %%
series_dados.std()
# %%
series_dados.max()
# %%
