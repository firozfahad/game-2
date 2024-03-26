import random
import time

from colorama import Fore

from events import events_list
from npc import NPC, Dialogue
from player import Player
from rooms import room_list


def start_game():
    print(Fore.GREEN + "Welcome to the Adventure Game!" + Fore.RESET)
    player_name = input("Enter your name: ")
    player_age = input("Enter your age: ")
    player_marital_status = input("Are you married? (yes/no): ")
    player_study_place = input("Where do you study? ")

    # Generate prediction based on player's answers
    prediction = generate_prediction(player_name, player_age, player_marital_status, player_study_place)
    print(Fore.YELLOW + "Here's your prediction:" + Fore.RESET)
    print(prediction)

def generate_prediction(name, age, marital_status, study_place):
    # Create a list of possible predictions
    predictions = [
        f"Hello {name}, based on your answers, it seems like you're destined for great success!",
        f"{name}, you're young and full of potential. Keep pursuing your dreams!",
        f"{name}, according to the stars, it's time for a big change in your life!",
        f"{name}, marriage may not be in the cards right now, but adventure certainly is!",
        f"{name}, embrace your independence and focus on your studies at {study_place}. The future looks bright!"
    ]

    # Select a random prediction
    prediction = random.choice(predictions)
    return prediction

if __name__ == "__main__":
    start_game()
