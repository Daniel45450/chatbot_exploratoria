from typing import Text, List, Any, Dict
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from swiplserver import PrologMQI
from rasa_sdk.events import SlotSet, ActiveLoop
from actions.consultarPL import *
from actions.config import *

class ValidateLoginForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_login_form"

    async def validate_correo_electronico(
        self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if not slot_value:
            dispatcher.utter_message(text="Por favor, proporciona tu correo electrónico.")
            return {"correo_electronico": None}
        return {"correo_electronico": slot_value}


    async def validate_contrasena(
        self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if not slot_value:
            dispatcher.utter_message(text="Por favor, proporciona una contraseña.")
            return {"contrasena": None}
        return {"contrasena": slot_value}
    
class Logear(Action):
    
    def name(self) ->Text:
        return "action_logear"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # obtengo los datos cargados desde mi form
        correo_electronico = tracker.get_slot('correo_electronico')
        contrasena = tracker.get_slot('contrasena')

        # creo un query para consultar prolog
        consulta_query = f'obtener_usuario(Nombre, "{correo_electronico}", Telefono, "{contrasena}", ProductosComprados, Direccion)'

        print(consulta_query)
        # realizo la consulta
        response = consultarPL(port, path_db, consulta_query)

        # si la respuesta es falsa no existe el usuario y reseteo los slots para que el que usuario vuelva a llenarlos en algun momento
        if not response:
            return [SlotSet("correo_electronico", None), SlotSet("contrasena", None), SlotSet("logged_in", False)]
        else: 
            # proceso los atributos del usuario enviados en la respuesta
            nombre = response[0].get('Nombre')
            telefono = response[0].get('Telefono')
            productos_comprados = response[0].get('ProductosComprados')
            direccion = response[0].get('Direccion')
            # seteo los slots con los datos correspondientes
            return [SlotSet("nombre", nombre), SlotSet("correo_electronico", correo_electronico), SlotSet("telefono", telefono), SlotSet("direccion_entrega", direccion), SlotSet("contrasena", contrasena), SlotSet("logged_in", True)] 