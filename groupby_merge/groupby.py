# %%
import pandas as pd

df = pd.read_excel("../data/transactions.xlsx")
df

# %%

df_user = df[df['IdCustomer'] =='5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']
df_user
# %%

df_user['Points'].sum()

# %%

df_summary = df.groupby(['IdCustomer'])['Points'].sum().reset_index()

# %%
import datetime

date1 = df['DtTransaction'][0]
now = datetime.datetime.now()

(now - date1).days

# %%
condiçao = df['IdCustomer']=='5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
df_user = df[condiçao]

# %%

# o x são todas datas do usuário (uma série)
# função de agregação personalizadas (deve retornar um elemento)
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return diff.days

(df.groupby(['IdCustomer'])
        .agg({
            'Points':'sum',
            'UUID':'count',
            'DtTransaction':['max', recencia],
            })
        .rename(columns={'Points':'Valor',
                 'UUID':'Frequencia',
                 'DtTransaction':'UltimaData'
                 })
        .reset_index())

# %%
