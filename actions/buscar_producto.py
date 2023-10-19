from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from actions.Producto import Producto
from swiplserver import PrologMQI
from actions.consultarPL import consultarPL

class AccionBuscarProducto(Action):
    def name(self):
        return "action_buscar_producto"

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
        print(consulta_query)
        result = consultarPL(port, path_db, consulta_query)

        print(str(result))
                   
        dispatcher.utter_message(f"Buscando producto: Categoria - {categoria}, Color - {color}, Talle - {talle}")

        return []
