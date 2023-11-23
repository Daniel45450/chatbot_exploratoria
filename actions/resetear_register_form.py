from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, ActiveLoop

class ResetearRegisterForm(Action):

    def name(self) -> Text:
        return "action_resetear_register_form"

    def run(self, dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        return [SlotSet('nombre',None), SlotSet('correo_electronico', None), SlotSet('telefono', None), SlotSet('direccion_entrega', None),
                SlotSet('contrasena', None), ActiveLoop('registro_form')]