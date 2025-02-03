# %%

import pandas as pd
import sqlalchemy

# %%

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

# traz a tabela inteira
df_transactions_cart = pd.read_sql_table('transactions_cart',engine)
df_transactions_cart
# %%

query = '''
SELECT * 
FROM customers 
LEFT JOIN transactions
ON customers.UUID = transactions.IdCustomer
LIMIT 10'''

df_join = pd.read_sql_query(query, engine)
df_join
# %%


data_01 = {
    "id": [1,2,3,4],
    "nome":["Teo", "Mat", "Nah", "Mah"],
    "idade": [31,31,32,32]
}

df_01 = pd.DataFrame(data_01)
df_01

# %%

data_02 = {
    "id": [5,6,7,8],
    "nome":["Jose", "Nathan", "Arnaldo", "Mario"],
    "idade": [23,33,19,21]
}

df_02 = pd.DataFrame(data_02)
df_02
# %%

df_01.to_sql('tb_1',engine, index=False)
# %%

df_02.to_sql('tb_1', engine, index=False, if_exists='append')