import pandas as pd

# Crear un DataFrame con los datos

data = {
    'Edad': [25, 30, 28, 35, 22, 40, 32, 27, 38, 26, 33, 29, 36, 24, 31, 34, 37, 23, 39, 28],
    'Salario': [50000, 60000, 55000, 70000, 48000, 75000, 62000, 52000, 68000, 49000, 63000, 56000, 71000, 47000, 59000, 66000, 73000, 51000, 69000, 54000],
    'Categoría_Producto': ['Electrónica', 'Moda', 'Deportes', 'Hogar', 'Electrónica', 'Moda', 'Deportes', 'Hogar', 'Electrónica', 'Moda', 'Deportes', 'Hogar', 'Electrónica', 'Moda', 'Deportes', 'Hogar', 'Electrónica', 'Moda', 'Deportes', 'Hogar'],
    'Puntuación': [0.8, 0.6, 0.9, 0.7, 0.5, 0.8, 0.7, 0.6, 0.9, 0.5, 0.8, 0.7, 0.6, 0.9, 0.8, 0.7, 0.6, 0.9, 0.8, 0.7],
}

df = pd.DataFrame(data)


# Guardar el DataFrame como un archivo CSV
df.to_csv('./datos/dataset.csv', index=False)
