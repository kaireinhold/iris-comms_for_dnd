#Created by Kai Reinhold (kaireinhold on GitHub)

import random
import time
import sys

#names and tasks are all just for testing at the moment.
players = ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9"]
players_for_task = players.copy()

tasks = [
    f"Steal a resource from {players_for_task.pop(random.randint(0, len(players_for_task) - 1))} without them noticing you. If they notice you, you fail.",
    f"Be {players_for_task.pop(random.randint(0, len(players_for_task) - 1))}'s friend for at least 30 minutes of the session without them getting suspicious of it being your task.",
    "Give another player a gift, and have them give you something in return.",
    f"Mess with {players_for_task.pop(random.randint(0, len(players_for_task) - 1))}'s base without them noticing you. If they notice you, you fail.",
    f"Give {players_for_task.pop(random.randint(0, len(players_for_task) - 1))} something randomly, and don't answer any questions they have about it for 10 minutes.",
    "Make a pun at every opportunity within a 5+ minute conversation.",
    "You are the Boogeyman. Kill another player by the end of the session. If you fail, you get put to your last life.",
    f"You now have social anxiety. You cannot talk to only one person, and if you get left alone with one person you must run away screaming.",
    "Play tic-tac-toe with every player at least once by the end of the session."
]

while players:
    current_player = players.pop(random.randint(0, len(players) - 1))
    print(f"It is {current_player}'s turn.")
    character_name = input("What is your character's name? ")

    if tasks:
        user_task = tasks.pop(random.randint(0, len(tasks) - 1))
        if current_player in user_task:
            tasks.append(user_task)
            user_task = tasks.pop(random.randint(0, len(tasks) - 1))
        else:
            None
        print(f"Hello, {character_name}. Your task is: {user_task}")
    else:
        print("No tasks left!")

    time.sleep(1)
