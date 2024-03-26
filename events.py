class Event:
    def __init__(self, description, reward=None):
        self.description = description
        self.reward = reward

# Define game events
event_1 = Event("You discover a hidden treasure chest!", reward="Gold coins")
event_2 = Event("A mysterious stranger offers you a quest.", reward="Experience points")

# List of all game events
events_list = [event_1, event_2]
