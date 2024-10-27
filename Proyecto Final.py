#Numero de Filas
import pandas as pd

df = pd.read_csv('ProyectoDataset.csv')
nro_filas = len(df)

#Numero de Columnas
nro_columnas = df.shape[1]

#Costo de vida promedio
costo_promedio = df['Cost of Living'].mean()

#Pais con costo de vida mas alto
pais_costo_alto = df.loc[df['Cost of Living'].idxmax(), 'Countries']

#Pais con costo de vida mas bajo
pais_costo_bajo = df.loc[df['Cost of Living'].idxmin(), 'Countries']

#Costo de vida en Peru
costo_peru = df.loc[df['Countries'] == 'Perú', 'Cost of Living'].values[0]

#Ranking de Peru
ranking_peru = df.loc[df['Countries'] == 'Perú', 'Global Rank'].values[0]

#Los 10 paises con el costo de vida mas alto
import matplotlib.pyplot as plt

top_10_altos = df.nlargest(10, 'Cost of Living')
plt.barh(top_10_altos['Countries'], top_10_altos['Cost of Living'])
plt.title('Los 10 países con el costo de vida más alto')
plt.xlabel('Costo de Vida')
plt.show()

#Los 10 paises con el costo de vida mas bajo
top_10_bajos = df.nsmallest(10, 'Cost of Living')
plt.barh(top_10_bajos['Countries'], top_10_bajos['Cost of Living'])
plt.title('Los 10 países con el costo de vida más bajo')
plt.xlabel('Costo de Vida')
plt.show()

#El costo de vida de los paises en America
america = df[df['Countries'].isin(['lista_de_paises_de_america'])]
plt.barh(america['Countries'], america['Cost of Living'])
plt.title('Costo de vida en países de América')
plt.xlabel('Costo de Vida')
plt.show()
