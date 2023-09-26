from typing import Text, List, Any, Dict
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from swiplserver import PrologMQI
from rasa_sdk.events import SlotSet, ActiveLoop
class ValidateRegistroForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_registro_form"

    async def validate_nombre(
        self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if not slot_value:
            dispatcher.utter_message(text="Por favor, proporciona tu nombre.")
            return {"nombre": None}
        return {"nombre": slot_value}

    async def validate_correo_electronico(
        self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if not slot_value:
            dispatcher.utter_message(text="Por favor, proporciona tu correo electrónico.")
            return {"correo_electronico": None}
        return {"correo_electronico": slot_value}

    async def validate_telefono(
        self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if not slot_value:
            dispatcher.utter_message(text="Por favor, proporciona tu número de teléfono.")
            return {"telefono": None}
        return {"telefono": slot_value}

    async def validate_direccion_entrega(
        self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if not slot_value:
            dispatcher.utter_message(text="Por favor, proporciona la direccion de entrega.")
            return {"direccion_entrega": None}
        return {"direccion_entrega": slot_value}

    async def validate_contrasena(
        self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> Dict[Text, Any]:
        if not slot_value:
            dispatcher.utter_message(text="Por favor, proporciona una contraseña.")
            return {"contrasena": None}
        return {"contrasena": slot_value}

class Registrar(Action):
    
    def name(self) ->Text:
        return "action_registrar"
    
    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        consulta_db = "consult('E:/Tercer año/Exploratoria/Rasa/Primer_proyecto/prolog/conocimiento_prolog.pl')"

        correo_electronico = tracker.get_slot('correo_electronico')

        consulta_query = f'existe_usuario("{correo_electronico}")'

        with PrologMQI(port=8000) as mqi:
            with mqi.create_thread() as prolog_thread:
                prolog_thread.query(consulta_db)
                response = prolog_thread.query(consulta_query)
                print(str(response))

                if response == True:
                    dispatcher.utter_message(text= "Error: Este usuario ya esta en nuestro sistema, ingresa los datos nuevamente")
                    return [SlotSet("nombre", None), SlotSet("correo_electronico", None), SlotSet("telefono", None), SlotSet("direccion_entrega", None), SlotSet("contrasena", None), ActiveLoop("registro_form")]
                if response == False: 
                    nombre = tracker.get_slot('nombre')
                    telefono = tracker.get_slot('telefono')
                    contrasena = tracker.get_slot('contrasena')
                    direccion_entrega = tracker.get_slot('direccion_entrega')
                    consulta_query = f'agregar_usuario("{nombre}", "{correo_electronico}", "{telefono}", "{contrasena}","{direccion_entrega}")'
                    response = prolog_thread.query(consulta_query)
                    dispatcher.utter_message(text="Registrado con exito")
                    return []    