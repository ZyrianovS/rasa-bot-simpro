# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction


# class ActionJobCheck(Action):
#     """
#     Go and get today's jobs for the logged in employee and report the count
#     and give details about the first job (job number, address and description).
#     """
#     def name(self) -> Text:
#         return "action_job_check"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         date = tracker.get_slot("date")
#         num_jobs = 5
#         job_id = 123
#         address = "31 McKechnie Dr, Eight Mile Plains"
#         description = "Very important job"
#
#         message = """
#                     You have {} jobs on {}.
#                     Details of the first job:
#                     id: {}
#                     address: {}
#                     description: {}""".format(num_jobs,
#                                               date,
#                                               job_id,
#                                               address,
#                                               description)
#         dispatcher.utter_message(message)
#
#         return [SlotSet("job_id", job_id),
#                 SlotSet("address", address),
#                 SlotSet("description", description)]


class ActionNextJob(Action):
    """
    Go into schedule to find based on the schedule time, what are the details for the next job.
    Return with the job number, customer, the address and the description of the job.
    """
    def name(self) -> Text:
        return "action_next_job"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        job_id = 123
        customer = "simPRO"
        address = "31 McKechnie Dr, Eight Mile Plains"
        description = "Very important job"
        message = """
                    Details of you next job:
                    id: {}
                    customer: {}
                    address: {}
                    description: {}""".format(job_id,
                                              customer,
                                              address,
                                              description)
        dispatcher.utter_message(message)

        return [SlotSet("job_id", job_id),
                SlotSet("customer", customer),
                SlotSet("address", address),
                SlotSet("description", description)]


# class ActionLocateTech(Action):
#     """
#     Go and find the schedule for a tech at the moment (based on the scheduled time)
#     and return with the job number and the site.
#     """
#     def name(self) -> Text:
#         return "action_locate_tech"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         tech_name = tracker.get_slot("tech_name")
#         job_id = 123
#         customer = "simPRO"
#         address = "31 McKechnie Dr, Eight Mile Plains"
#
#         message = """
#                     {} is on the job {}.
#                     Customer: {}
#                     Address: {}
#                     """.format(tech_name,
#                                job_id,
#                                customer,
#                                address)
#         dispatcher.utter_message(message)
#
#         return [SlotSet("job_id", job_id),
#                 SlotSet("customer", customer),
#                 SlotSet("address", address)]


class DateForm(FormAction):
    """Custom form action to fill date slot."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "date_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["date"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"date": self.from_entity(entity="date",
                                         intent=["inform",
                                                 "job_check"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        date = tracker.get_slot("date")
        num_jobs = 5
        job_id = 123
        address = "31 McKechnie Dr, Eight Mile Plains"
        description = "Very important job"

        message = """
                    You have {} jobs on {}.
                    Details of the first job:
                    id: {}
                    address: {}
                    description: {}""".format(num_jobs,
                                              date,
                                              job_id,
                                              address,
                                              description)
        dispatcher.utter_message(message)

        return [SlotSet("job_id", job_id),
                SlotSet("address", address),
                SlotSet("description", description)]


class TechForm(FormAction):
    """Custom form action to fill tech_name slot."""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "tech_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["tech_name"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"tech_name": self.from_entity(entity="tech_name",
                                              intent=["inform",
                                                      "locate_tech"])}

    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]
               ) -> List[Dict]:

        tech_name = tracker.get_slot("tech_name")
        job_id = 123
        customer = "simPRO"
        address = "31 McKechnie Dr, Eight Mile Plains"

        message = """
                    {} is on the job {}.
                    Customer: {}
                    Address: {}
                    """.format(tech_name,
                               job_id,
                               customer,
                               address)
        dispatcher.utter_message(message)

        return [SlotSet("job_id", job_id),
                SlotSet("customer", customer),
                SlotSet("address", address)]

