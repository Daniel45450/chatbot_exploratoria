from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionEliminarProducto(Action):

    def name(self) -> Text:
        return "action_eliminar_producto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # compruebo si la sesion esta iniciada
        logged_in = tracker.get_slot('logged_in')
        if logged_in == False:
            dispatcher.utter_message('Debes iniciar sesion para poder eliminar un producto del carrito')
            return []
        
        # obtengo el id del producto que debo eliminar
        id = tracker.get_slot('id')
        carrito = tracker.get_slot('carrito')
        # verifico si el carrito tiene elementos
        if carrito == None:
            dispatcher.utter_message(f'No hay elementos para borrar en el carrito')
            return []
        else:
            # creo un carrito y voy almacenando los distintos productos que hay en el original sin incluir el que debo eliminar
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
            # guardo el nuevo estado del carrito y reseteo id para reutilizarlo en otro momento
        return [SlotSet('carrito', nuevo_carrito), SlotSet('id', None)]
