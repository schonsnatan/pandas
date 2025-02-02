# %%
import pandas as pd
import numpy as np

data = {
    "nome":["Téo", "Nah", "Lah", "Mah", "Jo"],
    "idade":[31,32,34,12,np.nan],
    "renda":[np.nan,3245,357,12432,np.nan],
}
# %%
data
# %%

df = pd.DataFrame(data)
df
# %%

df['idade'].isna().sum()
# %%

df.isna().sum()
 # %%

# taxa de nans
df.isna().mean()

# %%

# analise ok usar mean, ML nao
df.fillna({
        'idade':df['idade'].mean(),
        'renda':df['renda'].mean(),
        })
# %%

# all ou any
df.dropna(subset=['idade','renda'], how='any')
# %%

df.dropna(axis=1, how='any')
# %%

# thresh: quant nao nulos para manter coluna
df.dropna(axis=1, thresh=3)
# %%
