# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 9:12:32 2018

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
dt_order['SECUENCIA']=1
#%%
tarjetas = dt_order['TARJETA'].unique()
for i in range(len(tarjetas)):
    if(tarjetas[i]==256673):
        print(tarjetas[i])