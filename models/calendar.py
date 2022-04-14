from models.event import *

event1 = Event("Thursday", "Nuclear War", "Operations Room", "This is how the world ends.", False)
event2 = Event("Friday", "Clean-up Day", "Kitchen", "Clean up after Thursday.", True)
all_events = [event1, event2]

def add_new_event(event):
    all_events.append(event)
    