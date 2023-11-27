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
        
        #recupero el slot logged_in para ver si el usuario inicio sesion
        logged_in = tracker.get_slot('logged_in')

        #si no inicio sesion se envia un mensaje que no esta logeado y no puede agregar el producto al carrito
        if logged_in == False:
            dispatcher.utter_message(response= "utter_not_logged_in")
            return []

        # obtengo los valores de mi lista de productos que contiene los ultimos productos que el usuario visito
        productos = tracker.get_slot('productos')

        if productos == None:
            dispatcher.utter_message(response= "utter_producto_no_encontrado")
            return []
        # busco si el ultimo mensaje del usuario tiene la entidad id que representa el producto que quiere agregar al carrito, 
        # si no esta devuelvo None
        id = next(tracker.get_latest_entity_values("id"), None)

        print(type(id), id)
        carrito = tracker.get_slot('carrito')
        producto_seleccionado = {}

        # verifico que el id coincida con alguno de los ultimos productos buscados
        for producto in productos:
            print(type(producto), producto)
            if(producto.get('id') == id):
                producto_seleccionado = producto
                break

        # si coincide lo agrego al carrito e imprimo un mensaje diciendo que se agrego exitosamente
        if producto_seleccionado:
            if carrito == None:
                carrito = []
            carrito.append(producto_seleccionado)
            dispatcher.utter_message(response="utter_producto_agregado")
        else:
            # si no lo encontro significa que el bot no conoce el producto y se lo informa al usuario
            dispatcher.utter_message(response= "utter_producto_no_encontrado")
            # guardo el nuevo estado del carrito
        return [SlotSet('carrito', carrito)]
