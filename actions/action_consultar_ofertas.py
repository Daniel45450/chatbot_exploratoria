from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from swiplserver import PrologMQI
from actions.consultarPL import consultarPL
from rasa_sdk.events import SlotSet
from actions.config import *

class AccionOfertasProductos(Action):
    def name(self):
        return "action_consultar_ofertas"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        consulta_query = "buscar_ofertas(Tiendas)"
        result = consultarPL(port, path_db, consulta_query)
        for tienda in result[0].get('Tiendas'):
            nombre = tienda.get('args')[0]
            descuento = tienda.get('args')[1]*100
            print (descuento)
            dispatcher.utter_message(f'En {nombre} descuento {descuento}% en efectivo')
        return []
