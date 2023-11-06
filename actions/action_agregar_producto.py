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

        productos = tracker.get_slot('productos')
        id = tracker.get_slot('id')
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
            dispatcher.utter_message(f"El producto {id} se agrego al carrito con exito")
        else:
            dispatcher.utter_message(f'No tengo conocimiento de ese producto')
        return [SlotSet('carrito', carrito), SlotSet('id', None)]
