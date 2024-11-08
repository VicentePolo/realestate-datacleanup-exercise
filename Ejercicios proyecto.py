import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Exercise 00 Read the dataset assets/real estate and visualize
ds = pd.read_csv('assets/real_estate.csv', sep=';')
print(ds)

#Exercise 01 The MOST expensive

inmueble_mas_caro=ds.loc[ds['price'].idxmax()]

precio_mas_caro=inmueble_mas_caro['price']
direccion_mas_caro=inmueble_mas_caro['address']
print("El valor mas alto de venta de los inmuebles es ",precio_mas_caro, "y se encuentra en ", direccion_mas_caro)
print("---------------------------------\n")
#Exercise 02 The LESS expensive

print("Ejercicio 2. La casa mas cara y la mas barata")
inmueble_mas_barato=ds.loc[ds['price'].idxmin()]

precio_mas_barato=inmueble_mas_barato['price']
direccion_mas_barato=inmueble_mas_barato['address']
print("El valor mas bajo de venta de los inmuebles es ",precio_mas_barato, "y se encuentra en ", direccion_mas_barato)
print("---------------------------------\n")
print("Ejercicio 3. La casa mas grande y la mas pequeña")

inmueble_mas_grande=ds.loc[ds['surface'].idxmax()]
superficie_mas_grande=inmueble_mas_grande['surface']
direccion_mas_grande=inmueble_mas_grande['address']
print("El inmueble con la superficie mas grande dispone de una superficie de", superficie_mas_grande, "y se halla en ",direccion_mas_grande )
inmueble_mas_pequeno=ds.loc[ds['surface'].idxmin()]
superficie_mas_pequena=inmueble_mas_pequeno['surface']
direccion_mas_pequena=inmueble_mas_pequeno['address']
print("El inmueble con la superficie mas pequeña dispone de una superficie de", superficie_mas_pequena, "y se halla en ",direccion_mas_pequena)
print("---------------------------------\n")
print("Ejercicio 4. ¿Cuantas poblaciones?")
populations=' , '.join(ds['level5'].unique())
print(populations)
print("---------------------------------\n")
print("Ejercicio 5. ¿Hay NA por aquí?")

print(ds[ds.isna()])

print("---------------------------------\n")
print("Ejercicio 6. Delete NA")
dsclean=ds.dropna()
print(dsclean)
print("---------------------------------\n")

print("Exercise 7. Which is the mean on the population of Arroyomolinos and explain what you observe")

media_arroyo = ds[ds["level5"] == "Arroyomolinos(Madrid)"]["price"].mean()

print("El valor medio de los precios de Arroyomolinos es", media_arroyo)
print("---------------------------------\n")

print("Exercise 8. Plot the histogram of prices for the population of Arroyomolinos(Madrid)")

data = ds[ds["level5"] == "Arroyomolinos(Madrid)"]["price"]

plt.hist(data, bins=30, color='blue', edgecolor='black')

plt.xlabel('Poblacion')
plt.ylabel('Precio')
plt.title('Precios en Arroyomolinos')
 
plt.show()

print("Exercise 9. Comparativa de precios entre Valdemorillo y Galapagar")

data = ds[ds["level5"] == "Valdemorillo"]["price"]

plt.hist(data, bins=30, color='green', edgecolor='black')

plt.xlabel('Poblacion')
plt.ylabel('Precio')
plt.title('Precios en Valdemorillo')
 
plt.show()

data = ds[ds["level5"] == "Galapagar"]["price"]

plt.hist(data, bins=30, color='red', edgecolor='black')

plt.xlabel('Poblacion')
plt.ylabel('Precio')
plt.title('Precios en Galapagar')
 
plt.show()

print("Exercise 10. Comparativa de precios por metro cuadrado entre Valdemorillo y Galapagar")

ds["pps"]=ds["Price"]/ds["surface"]

valmor=[ds["level5"] == "Valdemorillo"]["pps"]
valgal=[ds["level5"] == "Galapagar"]["pps"]

print(valmor)
print(valgal)
