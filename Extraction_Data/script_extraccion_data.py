# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:55:49 2018

@author: diego
"""

import csv
import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

# Lectura de Datos Pandas
col=['Airline ID','Name','Alias','IATA','ICAO','Callsign','Country','Active']
data = pd.read_csv("airlines.csv", sep=',', names=col, encoding='latin-1')
print (data)
#%%
# Limpia el dataframe de nullos
data_limp = data.dropna() 
# Crea un nuevo csv sin nullos y sin indice
data_limp.to_csv('data_limp.csv', index = False)
# Realiza la lectura de la nueva data
dt = pd.read_csv("data_limp.csv", encoding='latin-1')
#%%
# Describe el df con el conteo de registros, media, desviacion estandar, min y quartiles...
print (dt.describe(include='all')) 
#%%
# Indica la correlación entre las diferentes variables
print (dt.corr())
#%%
# Indica la covarianza entre las diferentes variables
print (dt.cov())
#%%
#Revisamos aerolinas activas y no activas....
A_Activas = dt[dt.Active == 'Y']
print(len(A_Activas))
A_NoActivas = dt[dt.Active == 'N']
print(len(A_NoActivas))
#%%
# Aerolinas en francia ....
Francia = dt[dt.Country == 'France']
con_Francia = np.sum(Francia)
print(len(con_Francia))
#%%
print(len(data))
print(len(data) - (len(data) - len(dt)))


#for year in enumerate(years):
#print Antioquia[year]
#cafe_antioquia = np.sum(Antioquia[2002:2016])

#print Antioquia
#print cafe_antioquia

#print data.info() # indica informacion del dataframe ...
#print data.dtypes # indica tipo de dato...
#print data.describe() # indica el conteo de registros, media, desviacion estandar, min y quartiles...
#print data.tail(5) # muestra los ultimos 5 registros...
#print data[2000:2005] #  rebanar los datos....
#print data['Name'] # selecciona la columna indicada de la data....
#print data[['Name', 'Active']].head() # seleccionar varias columnas de la data...
#print '\n'
#col_buscar = ['IATA','ICAO']
#print data[col_buscar].head() # imprime en dos bloquees diferentes las columnas listadas
#print data[(data.Country =='Estonia') | (data.Country =='Pakistan')].head(5) # Se utiliza un filtro para realizar busquedas o intervalos de data..
#print data.set_index('Name', inplace=True) # Si desea modificar su DataFrame existente, utilice el parámetro inplace.
#print data.head(10)
#print len(data) # Indica el tamaño del dataframe...

#Revisamos aerolinas activas y no activas....
#A_Activas = data[data.Active == 'Y']
#A_NoActivas = data[data.Active == 'N']

# Aerolinas en francia ....
#Francia = data[data.Country == 'France']
#con_Francia = np.sum(Francia)

# Aerolinas en japon ....
#Japon = data[data.Country == 'Japan']
#con_Japon = np.sum(Japon)


#print con_Japon

#figure1 = plt.figure(1)
#plt.plot(14, cafe_antioquia, 'c', label='Antioquia')
#plt.legend(loc='upper righ')
#plt.ylabel('Hectareas')
#plt.xlabel('Anio')
#plt.title('Grafico Area Cultivada')
#plt.show()