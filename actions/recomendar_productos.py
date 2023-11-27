from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
import random
from datos.config import path_dataset, path_modelo

class RecomendarProductos(Action):

    def name(self) -> Text:
        return "action_recomendar_productos"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df = pd.read_csv(path_dataset)

        # Convierte las Categorias en variables dummy
        df = pd.get_dummies(df, columns=['Categoria_Producto'])

        # Divide en características (X) y etiquetas (y)
        X = df.drop(['Categoria_Producto_Electronica', 'Categoria_Producto_Moda', 'Categoria_Producto_Deportes', 'Categoria_Producto_Hogar'], axis=1)
        y = df[['Categoria_Producto_Electronica', 'Categoria_Producto_Moda', 'Categoria_Producto_Deportes', 'Categoria_Producto_Hogar']]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = Sequential([
            Dense(16, activation='sigmoid', input_shape=(X_train.shape[1],)),
            Dense(8, activation='relu'),
            Dense(y.shape[1], activation='softmax')
        ])

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        # Entrena el modelo
        model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.3, verbose=0)

        # Evalúa el modelo en el conjunto de prueba
        loss, accuracy = model.evaluate(X_test, y_test)

        print(f'Loss: {loss}, Accuracy: {accuracy}')

        model.save(path_modelo)

        # Genera datos aleatorios
        edad = random.randint(0, 100)
        salario = random.randint(25000, 60000)
        puntuacion = random.random()

        # Crea un DataFrame con los datos
        predecir = pd.DataFrame({
            'Edad': [edad],
            'Salario': [salario],
            'Puntuación': [puntuacion]
        })

        # Convierte las Categorias en variables dummy
        new_data = pd.get_dummies(predecir)

        # Hacer predicción
        resultados = model.predict(new_data)

        print('resultados: ', resultados)

        recomendar_categorias = []

        for indice, porcentaje in enumerate(resultados[0]):

            if(porcentaje > 0.25):
                if indice == 0:
                    recomendar_categorias.append('Electrónica')
                elif indice == 1:
                    recomendar_categorias.append('Moda')
                elif indice == 2:
                    recomendar_categorias.append('Deportes')
                elif indice == 3:
                    recomendar_categorias.append('Hogar')

        if recomendar_categorias:
            dispatcher.utter_message(f'Te recomiendo los siguientes productos: ')
            productos = f""
            for recomendacion in recomendar_categorias:
                productos += f"{recomendacion}\n"
            dispatcher.utter_message(f'Te recomiendo ver las secciones de productos: ')
            dispatcher.utter_message(productos)
        else:
            dispatcher.utter_message('No sé qué productos recomendarte')

        return []

