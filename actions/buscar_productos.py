from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.Producto import *
from swiplserver import PrologMQI
from actions.consultarPL import consultarPL
from rasa_sdk.events import SlotSet

class AccionBuscarProductos(Action):
    def name(self):
        return "action_buscar_productos"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        categoria = tracker.get_slot("categoria")
        color = tracker.get_slot("color")
        talle = tracker.get_slot("talle")
        material = tracker.get_slot("material")
        tamano = tracker.get_slot("tamano")
        gusto = tracker.get_slot("gusto")
        marca = tracker.get_slot("marca")

        path_db = "consult('E:/Tercer año/Exploratoria/Rasa/Primer_proyecto/prolog/conocimiento_prolog.pl')"
        port = 8000

        variables_sin_comillas = [categoria, marca]
        parametros = [categoria, color, material, talle, tamano, gusto, marca]
        consulta_query = "filtrarProductos("
        for parametro in parametros:
            if parametro is not None:
                if parametro in variables_sin_comillas:
                    consulta_query += f'{parametro},'
                else:
                    consulta_query += f'"{parametro}",'
            else:
                consulta_query += '[],'
        consulta_query += f'Productos).'
        result = consultarPL(port, path_db, consulta_query)
        lista_productos = []

        ultimo_intent = tracker.get_intent_of_latest_message()
        for resultado in result[0].get('Productos', []):  # Accede a la lista de productos en el resultado
            consulta_query = f'buscar_producto({resultado}, Producto).'
            result_p = consultarPL(port, path_db, consulta_query)
            if result_p:
                producto = result_p[0].get('Producto').get('args')
                id = producto[0]
                categorias = producto[1]
                atributos = {}
                for atributo in producto[2]:
                    clave = atributo.get('args')[0]
                    valor= atributo.get('args')[1]
                    atributos[clave] = valor

                descripciones = producto[3]
                marca = producto[4]
                precio = producto[6]
                stock = producto[5]     
             
                if(ultimo_intent == "comprar_zapatos"):
                        # Verificar si la categoría es 'zapato' antes de crear una instancia de Zapato
                        color = atributos.get('color')
                        talle = atributos.get('talle')
                        tipo = atributos.get('tipo')
                        
                        zapato = Zapato(id, marca, talle, color, categorias, tipo)
                        
                        lista_productos.append(zapato.to_dict())  # Añade el producto a la lista de productos
                if(ultimo_intent == "comprar_camisetas"):
                        color = atributos.get('color')
                        talle = atributos.get('talle')
                        tipo = atributos.get('tipo')
                        material = atributos.get('material')
                        
                        camiseta = Camiseta(id, marca, talle, color, categorias, material, tipo)    
                        lista_productos.append(camiseta.to_dict())  # Añade el producto a la lista de productos                


        print(str(lista_productos))

        dispatcher.utter_message(f"Buscando producto: Categoria - {categoria}, Color - {color}, Talle - {talle}")

        return [SlotSet('productos', lista_productos)]
