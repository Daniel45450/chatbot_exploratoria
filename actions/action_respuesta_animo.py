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

        opciones_respuesta = ["utter_animo_bueno", "utter_animo_malo"]
        respuesta_seleccionada = random.choice(opciones_respuesta)

        dispatcher.utter_message(template=respuesta_seleccionada)

        return []