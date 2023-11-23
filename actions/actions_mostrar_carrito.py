from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionAgregarProducto(Action):

    def name(self) -> Text:
        return "action_ver_carrito"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        login_in = tracker.get_slot('logged_in')
        if not login_in:
            dispatcher.utter_message(response= "utter_not_logged_in_carrito")
            return []
        else:    
            carrito = tracker.get_slot('carrito')
            if carrito == None:
                dispatcher.utter_message(response= "utter_carrito_vacio")
            else:
                total = 0
                dispatcher.utter_message(response= "utter_mostrar_carrito")
                for producto in carrito:
                    print
                    dispatcher.utter_message(f'ID: {producto.get("id")} Descripcion: {producto.get("descripciones")} Cantidad disponible: {producto.get("stock")} Precio: {producto.get("precio")} Tienda: {producto.get("tienda")}\n')
                    total += int(producto.get('precio'))
                dispatcher.utter_message(f'Total: {total}')
        return []
