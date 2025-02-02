# %%

import pandas as pd
df = pd.read_excel("../data/transactions.xlsx")
df
# %%

df_last = (df.sort_values(by=['DtTransaction'],ascending=False)
            .drop_duplicates(subset=['IdCustomer'], keep='first'))

df_last
# %%

df_last['IdCustomer'].nunique()

# %%

# retorna uma lista bool onde a condição é true ou false
condicao = df['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3'
# %%

# retorna um df onde apenas aquela condição é satisfeita
df[condicao]
# %%

df_last[df_last['IdCustomer'] == '5f8fcbe0-6014-43f8-8b83-38cf2f4887b3']
# %%
