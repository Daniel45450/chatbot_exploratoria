from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionAgregarProducto(Action):

    def name(self) -> Text:
        return "action_eliminar_producto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        id = tracker.get_slot('id')
        carrito = tracker.get_slot('carrito')
        if carrito == None:
            dispatcher.utter_message(f'No hay elementos para borrar en el carrito')
        else:
            nuevo_carrito = []
            encontrado = False
            for producto in carrito:
                if(producto.get('id') != id):
                    nuevo_carrito.append(producto)
                else:
                    encontrado = True
        if(encontrado):
            dispatcher.utter_message(response= 'utter_carrito_elemento_eliminado')
        else:
            dispatcher.utter_message(response= 'utter_carrito_elemento_no_encontrado')
        return [SlotSet('carrito', nuevo_carrito), SlotSet('id', None)]
