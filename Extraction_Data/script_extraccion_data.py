# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 8:25:49 2018

@author: diego
"""

import csv
import pandas as pd
import numpy  as np
import pymysql
import matplotlib.pyplot as plt

# Lectura de Datos Pandas.
col=['TARJETA','HORA','ESTACION']
data = pd.read_csv("Prueba Datamining.csv", sep=',', names=col, encoding='latin-1')
print (data)
#%%
# Limpia el dataframe de nullos.
data_limp = data.dropna() 
# Crea un nuevo csv sin nullos y sin indice.
data_limp.to_csv('data_limp.csv', index = False)
# Realiza la lectura de la nueva data.
dt = pd.read_csv("data_limp.csv", encoding='latin-1')
#%% Describe el df con el conteo de registros, media, desviacion estandar, min y quartiles...
print (dt.describe(include='all')) 
#%% Indica la correlación entre las diferentes variables.
print (dt.corr())
#%% Indica la covarianza entre las diferentes variables.
print (dt.cov())
#%% Ordenar por numero de tarjeta y hora de manera ascendente.
dt_order = dt.sort_values(by=['TARJETA', 'HORA'])
print(dt_order)
#%% # Secuencia de transacciones teniendo en tarjeta, hora y estación.
# SQL: SELECT count(*) FROM dt_order GROUP BY TARJETA;
groupby_dt_order = dt_order.groupby('TARJETA').count() 
print(groupby_dt_order)
#%% # Agrupación por tarjeta para que solo muestre el conteo de hora.
# SQL: SELECT HORA, count(*) FROM dt_order GROUP BY TARJETA;
groupby_dt_order = dt_order.groupby('TARJETA')['HORA'].count() 
print(groupby_dt_order)
#%% # 1 Forma.Agrupación indicando qué funciones aplicar a columnas específicas.(Solo con valores numericos)
#SQL:SELECT TARJETA, COUNT(*) FROM dt_order GROUP BY TARJETA, HORA, ESTACION ;

groupby_dt_order = dt_order.groupby(['TARJETA','HORA','ESTACION'])['TARJETA'].agg(['mean', 'std'])
print(groupby_dt_order)

#%% # 2 Forma.Agrupación indicando qué funciones aplicar a columnas específicas.(Solo con valores numericos)
#SQL:SELECT TARJETA, COUNT(*) FROM dt_order GROUP BY TARJETA, HORA, ESTACION ;

groupby_dt_order = dt_order.groupby(['TARJETA','HORA','ESTACION'])['TARJETA'].agg({'Mean':np.mean,'Std':np.std, 'myMean': lambda x: (x.sum() / int(x.count())) })
print(groupby_dt_order)


















