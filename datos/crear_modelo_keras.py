import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow import keras

df = pd.read_csv('./datos/dataset.csv')

# Convierte las categorías en variables dummy
df = pd.get_dummies(df, columns=['Categoría_Producto'])

# Divide en características (X) y etiquetas (y)
X = df.drop(['Categoría_Producto_Electrónica', 'Categoría_Producto_Moda', 'Categoría_Producto_Deportes', 'Categoría_Producto_Hogar'], axis=1)
print(X)
y = df[['Categoría_Producto_Electrónica', 'Categoría_Producto_Moda', 'Categoría_Producto_Deportes', 'Categoría_Producto_Hogar']]
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Sequential([
    keras.layers.Input(shape=(X_train.shape[1],)),
    keras.layers.Dense(16, activation="sigmoid"),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(y.shape[1], activation="softmax"),
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrena el modelo
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.3)

# Evalúa el modelo en el conjunto de prueba
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Loss: {loss}, Accuracy: {accuracy}')

predecir = pd.DataFrame({
    'Edad': [28],
    'Salario': [60000],
    'Puntuación': [0.8]
})

# Convierte las categorías en variables dummy
new_data = pd.get_dummies(predecir)

# Hacer predicciones en nuevos datos
resultado = model.predict(predecir)

print('resultados: ', resultado)

