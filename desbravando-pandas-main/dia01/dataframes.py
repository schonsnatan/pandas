# %%
import pandas as pd
# %%

data = {
    "nome":["teo","nah","lara","maria"],
    "sobrenome":["calvo","ataide", "schons", "silva"],
    "idade":[31,32,31,2]
}

data
# %%

data["idade"][-1]
# %%

df = pd.DataFrame(data)
df
# %%

df["idade"].iloc[0]
# %%

type(df['idade']) #série
# %%

df['sobrenome'][0]

# %%

#também uma série
df.iloc[0] 

# %%

df.index=[3,2,1,0]
df
# %%

df['idade'].loc[0]
# %%

df.index
# %%

df.columns
# %%

df.info()
# %%

df.info(memory_usage='deep')
# %%

df.dtypes
# %%

#atribuindo coluna nova
df['peso'] = [80,52,45,78]

df.describe()
# %%

sumario = df.describe()
sumario['peso']['mean']
# %%

# 5 primeiras linhas ou especificar numero
df.head()
# %%

# 5 últimas linhas por padrão
df.tail(2)
# %%
