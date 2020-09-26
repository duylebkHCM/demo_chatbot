from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class Accounting_start(Action):
    def name(self) -> Text:
        return "Accounting_start"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: Accounting_start")

        return []

class Confirmation_of_order_completion(Action):
    def name(self) -> Text:
        return "Confirmation_of_order_completion"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: Confirmation_of_order_completion")

        return []

class Tobacco_touch_confirmation(Action):
    def name(self) -> Text:
        return "Tobacco_touch_confirmation"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: Tobacco_touch_confirmation")

        return []

class Bag_confirmation(Action):
    def name(self) -> Text:
        return "Bag_confirmation"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: Bag_confirmation")

        return []

class Check_if_the_bag_is_the_same(Action):
    def name(self) -> Text:
        return "Check_if_the_bag_is_the_same"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: Check_if_the_bag_is_the_same")

        return []

class Accounting_confirmation(Action):
    def name(self) -> Text:
        return "Accounting_confirmation"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: Accounting_confirmation")

        return []

class Say_thanks(Action):
    def name(self) -> Text:
        return "Say_thanks"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: Say_thanks")

        return []

class action_custom_fallback(Action):
    def name(self) -> Text:
        return "action_custom_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Action: action_custom_fallback")

        return []

class Custom_Fallback(Action):
    def name(self) -> Text:
        return "action_custom_fallback"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Không hiểu.")

        return []