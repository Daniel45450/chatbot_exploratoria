import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Text, Dict, Any, List

class AccionRespuestaAnimo(Action):

    def name(self) -> Text:
        return "action_respuesta_animo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Lista de respuestas disponibles
        opciones_respuesta = ["utter_animo_bueno", "utter_animo_malo"]

        # Seleccionar aleatoriamente una respuesta
        respuesta_seleccionada = random.choice(opciones_respuesta)
        
        # Enviar la respuesta al usuario    
        dispatcher.utter_message(response = respuesta_seleccionada)

        return []