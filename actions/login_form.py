from typing import Text, List, Any, Dict
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from swiplserver import PrologMQI
from rasa_sdk.events import SlotSet, ActiveLoop

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

        consulta_db = "consult('E:/Tercer año/Exploratoria/Rasa/Primer_proyecto/prolog/conocimiento_prolog.pl')"

        correo_electronico = tracker.get_slot('correo_electronico')
        contrasena = tracker.get_slot('contrasena')

        consulta_query = f'obtener_usuario(Nombre, "{correo_electronico}", Telefono, "{contrasena}", ProductosComprados, Direccion)'


        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query(consulta_db)
                response = prolog_thread.query(consulta_query)
                print(str(response), type(response))

                if response == False:
                    dispatcher.utter_message(text= "Error: Este usuario no esta en nuestro sistema")
                    return [SlotSet("correo_electronico", None), SlotSet("contrasena", None)]
                if response == True: 
                    nombre = response[0]['Nombre']
                    telefono = response[0]['Telefono']
                    productos_comprados = response[0]['ProductoComprados']
                    direccion = response[0]['Direccion']
                    dispatcher.utter_message(text="Logeado con exito")
                    return [SlotSet("nombre", nombre), SlotSet("correo_electronico", correo_electronico), SlotSet("telefono", telefono), SlotSet("direccion_entrega", direccion), SlotSet("contrasena", contrasena), SlotSet("logged_in", True)] 