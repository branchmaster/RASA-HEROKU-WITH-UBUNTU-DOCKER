from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk import Action
from rasa_sdk.forms import FormAction
import json



class NearestAttraction(Action):
 def name(self):
  """name of the custom action"""
  return "action_nearest_attractions"

 def run(self,dispatcher,tracker,domain):	
  data = {
        "payload": 'cardsCarousel',
        "data": [
            {
                "image": "https://b.zmtcdn.com/data/pictures/1/18602861/bd2825ec26c21ebdc945edb7df3b0d99.jpg",
                "title": "Taftoon Bar & Kitchen",
                "ratings": "4.5",
            },
            {
                "image": "https://b.zmtcdn.com/data/pictures/4/18357374/661d0edd484343c669da600a272e2256.jpg",

                "ratings": "4.0",
                "title": "Veranda"
            },
            {
                "image": "https://b.zmtcdn.com/data/pictures/4/18902194/e92e2a3d4b5c6e25fd4211d06b9a909e.jpg",

                "ratings": "4.0",
                "title": "145 The Mill"
            },
            {
                "image": "https://b.zmtcdn.com/data/pictures/3/17871363/c53db6ba261c3e2d4db1afc47ec3eeb0.jpg",

                "ratings": "4.0",
                "title": "The Fatty Bao"
            },
        ]
    }

  dispatcher.utter_message(json_message=data)
  return []
class BookRooms(Action):
 def name(self):
  """name of the custom action"""
  return "action_book_rooms"

 def run(self,dispatcher,tracker,domain):	
  gt = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                                                {
                            "title": "Deluxe Room",
                            "image_url":"https://d2e5ushqwiltxm.cloudfront.net/wp-content/uploads/sites/125/2017/05/25023446/Rooms-Suites-Section-2nd-Room-Deluxe-Room.jpg",
                            "subtitle": "These Deluxe Rooms let you relax as you admire a beautiful view of the pool. Stay connected as you enjoy our free WiFi and watch movies with our 32-inch LCD TV and DVD player.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/dulex_room_details",
                                    "title": "Read More"
                                },
                              {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                },  
                            ]
                        },
                        {
                            "title": "Junior Suite",
                            "image_url":"https://www.discoverysuites.com/files/2015/06/Junior-Suite-Deluxe.jpg",
                            "subtitle": "Large bedroom with exquisitely embroidered queen or king size bed. Elegant, luxury decor with rich fabrics. Separate sitting room with sofa and armchairs.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/junior_suite_details",
                                    "title": "Read More"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                },
                            ]
                        },
                        {
                            "title": "Club Suite",
                            "image_url":"https://media-cdn.tripadvisor.com/media/photo-s/12/77/d8/18/club-suite-living-room.jpg",
                            "subtitle": "The Club Suite is the ideal choice for a comfortable and lavish stay for both small families and business travelers alike. The gently soothing views and the calming ambiance of the suite add to an enriching experience for our guests.",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "payload": "/club_suite_details",
                                    "title": "Read More"
                                },
                                {
                                    "type": "postback",
                                    "payload": "/book_room_now",
                                    "title": "Book Now"
                                }, 
                            ]
                        },
                        
                    ]
                }
            }
        }
  dispatcher.utter_custom_json(gt)
  return []  

class BookRoomForm(FormAction):
 def name(self):
  return "book_room_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["check_in","check_out","adults","child","room","name","phno","email"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
    return {
            "check_in": [
                self.from_text(),
            ],
            "check_out": [
                self.from_text(),
            ],
            
            "adults": [
                self.from_text(),
            ],
            "child": [
                self.from_text(),
            ],
            "room": [
                self.from_text(),
            ],
            "name": [
                self.from_text(),
            ],
            "phno": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_message("Your booking details are here")    
    return []
class BookRoomsDetails(Action):
 def name(self):
  """name of the custom action"""
  return "action_book_rooms_details"

 def run(self,dispatcher,tracker,domain):
  check_in=tracker.get_slot("check_in")
  check_out=tracker.get_slot("check_out")
  adults=tracker.get_slot("adults")
  child=tracker.get_slot("child")
  room=tracker.get_slot("room")
  name=tracker.get_slot("name")
  phno=tracker.get_slot("phno")
  email=tracker.get_slot("email")
  message="BOOKING DETAILS:"+"\n\n"+"Checkin Date:"+check_in+"\n"+"Checkout Date:"+check_out+"\n"+"No. of Adults:"+adults+"\n"+"No. of Children:"+child+"\n"+"No.of Rooms:"+room+"\n"+"Phone Number:"+phno+"\n"+"Email:"+email
  dispatcher.utter_message(message)  