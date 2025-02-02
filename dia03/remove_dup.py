# %%
import pandas as pd

data = {
    "Nome": ["Téo", "Nah", "Maria", "Nah", "Lara", "Téo"],
    "Idade": [32,33,2,33,31,32],
    "updated_at":[1,2,3,1,2,3]
}

df = pd.DataFrame(data)
df
# %%

# só remove se for tudo igual
df.drop_duplicates()
# %%

# antes de remover duplicatas, ordenamos para encontrar o mais atualizado
df = df.sort_values(by='updated_at',ascending=False)
df

# %%

# subset remove baseado nos parametros
df.drop_duplicates(subset=['Nome','Idade'],keep='first')

# %%

# encadeando comandos

df = (df.sort_values(by='updated_at',ascending=False)
    .drop_duplicates(subset=['Nome','Idade'],keep='first'))

df
# %%
