from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SessionStarted, ActionExecuted

class ActionSessionStart(Action):

    def name(self) -> Text:
        return "action_session_start"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        mensaje_bienvenida = "¡Hola! ¿En qué puedo ayudarte hoy?"

        dispatcher.utter_message(mensaje_bienvenida)
        eventos = [SessionStarted(), ActionExecuted("action_listen")]

        return eventos
