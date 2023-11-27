from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionVerCarrito(Action):

    def name(self) -> Text:
        return "action_ver_carrito"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        # se comprueba si la sesion esta iniciada 
        login_in = tracker.get_slot('logged_in')
        if not login_in:
            dispatcher.utter_message(response= "utter_not_logged_in_carrito")
            return []
        else:    
            # objeto el valor del carrito
            carrito = tracker.get_slot('carrito')
            if carrito == None:
                # si esta vacio mando un mensaje al respecto 
                dispatcher.utter_message(response= "utter_carrito_vacio")
            else:
                total = 0 # se utiliza para calcular el total a pagar
                dispatcher.utter_message(response= "utter_mostrar_carrito")
                for producto in carrito:
                    # recorro el carrito e imprimo los elementos
                    dispatcher.utter_message(f'ID: {producto.get("id")} Descripcion: {producto.get("descripciones")} Cantidad disponible: {producto.get("stock")} Precio: {producto.get("precio")} Tienda: {producto.get("tienda")}\n')
                    total += int(producto.get('precio')) # calculo el total
                dispatcher.utter_message(f'Total: {total}')
        return []
