from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionAgregarProducto(Action):

    def name(self) -> Text:
        return "action_agregar_producto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        logged_in = tracker.get_slot('logged_in')
        if logged_in == False:
            dispatcher.utter_message(response= "utter_not_logged_in")
            return []

        productos = tracker.get_slot('productos')
        id = next(tracker.get_latest_entity_values("id"), None)
        print(type(id), id)
        carrito = tracker.get_slot('carrito')
        producto_seleccionado = {}
        for producto in productos:
            print(type(producto), producto)
            if(producto.get('id') == id):
                producto_seleccionado = producto
                break
        if producto_seleccionado:
            if carrito == None:
                carrito = []
            carrito.append(producto_seleccionado)
            dispatcher.utter_message(response="utter_producto_agregado")
        else:
            dispatcher.utter_message(response= "utter_producto_no_encontrado")
        return [SlotSet('carrito', carrito)]
