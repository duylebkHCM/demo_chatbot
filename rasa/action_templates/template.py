from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

{% for action in actions %}
class {{action}}(Action):
    def name(self) -> Text:
        return "{{action}}"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: {{action}}")

        return []

{% endfor %}
class Custom_Fallback(Action):
    def name(self) -> Text:
        return "action_custom_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Không hiểu.")

        return []