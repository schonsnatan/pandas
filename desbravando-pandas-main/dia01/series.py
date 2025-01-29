# %%
import pandas as pd


# %%

idades = [30, 42, 90, 34]
idades
# %%

media = sum(idades) / len(idades)

#desvio padrão (Variancia)

total = 0
for i in idades:
    total += (media - i)**2
variancia = total / len(idades) - 1

desvio_padrao = variancia**(1/2)

# %%

series_idades = pd.Series(idades)
series_idades
# %%
