# %%
import pandas as pd
import numpy as np
from dateutil.relativedelta import relativedelta

# criando o dataset
data = {
    "idTransaction": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "idCliente": [1, 2, 3, 3, 3, 2, 2, 1, 1, 2],
    "dtTransaction": ["10/01/2024", "18/01/2024", "04/02/2024", "22/02/2024", "05/03/2024",
                      "20/02/2024", "10/03/2024", "14/01/2024", "06/03/2024", "19/03/2024"],
    "Valor": [250, 300, 450, 230, 35, 12, 467, 1200, 670, 324],
    "Parcelas": [2, 3, 3, 2, 1, 1, 3, 5, 3, 2],
}

# criando o dataframe
df = pd.DataFrame(data)

# formatando a coluna de data
df['dtTransaction'] = pd.to_datetime(df['dtTransaction'],format='%d/%m/%Y')

# nova coluna com valor da parcela
df['ValorParcela'] = df.apply(lambda row: [row['Valor'] / row['Parcelas'] for i in range(row['Parcelas'])],axis=1)

'''
# FUNÇÃO
def dividir_parcelas(row):
    return [row['Valor'] / row['Parcelas']] * row['Parcelas']

df['Parcelas_Valor'] = df.apply(dividir_parcelas,axis=1)
'''

# explode da lista de valores em mais linhas
df_fatura = df.explode('ValorParcela')
df_fatura = df_fatura.drop(['Valor','Parcelas'],
                           axis=1)

# adicionamos a coluna months_add para rankear as parcelas, ranqueando por transação
df_fatura['Months_add'] = df_fatura.groupby("idTransaction")['dtTransaction'].rank('first').astype(int)

# adicionamos nova coluna usando apply para mostrar as datas da fatura
def add_months(row):
    new_date = row['dtTransaction'] + relativedelta(months=row['Months_add'])    
    dt_str = new_date.strftime("%Y-%m")
    return dt_str

df_fatura['dtFatura'] = df_fatura.apply(add_months, axis=1)
df_fatura

# %%

# agrupando a soma das parcelas de todas compras por cliente mes a mes
df_fatura_mes = (df_fatura.groupby(['idCliente','dtFatura'])['ValorParcela']
                          .sum()
                          .reset_index())
df_fatura_mes

# %%

# posso pivotar a coluna dtFatura  
df_fatura_mes = (df_fatura_mes.pivot_table(columns='dtFatura', 
                                           index='idCliente', 
                                           values='ValorParcela')
                                            .fillna(0)
                                            .reset_index()
                                            )
df_fatura_mes
# %%
