# %%

import pandas as pd

df = pd.read_csv(r"path", sep=";")
df

# %%

# fixando as colunas
df = df.set_index(['cod','nome','período'])
df

# %%

# stack (pivotando a tabela)
df_stack = df.stack().reset_index().rename(columns={'level_3':'Tipo Homicidio',
                                         0:'quantidade'})

# %%

# transpondo o stack (primeiro setar o index antes de fazer isso)
df_unstack = (df_stack
            .set_index(['cod','nome','período','Tipo Homicidio'])
            .unstack()
            .reset_index())

homicidios = df_unstack['quantidade'].columns.tolist()
homicidios

df_unstack.columns = ['cod','nome','período'] + homicidios
df_unstack
# %%
