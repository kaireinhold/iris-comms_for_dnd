import random
import time
import sys

players = ["Kai", "Luca", "Andrew", "Jacob", "Crimson", "test1", "test2", "test3"]
tasks = [
    f"Steal a resource from {players[random.randint(0, len(players) - 1)]} without them noticing you. If they notice you, you fail.",
    f"Be {players[random.randint(0, len(players) - 1)]}'s friend for 30 minutes of the session without them getting suspicious of it being your task.", "Give another player a gift, and have them give you something in return.", f"Steal a resource from {players[random.randint(0, len(players) - 1)]} without them noticing you. If they notice you, you fail.",
    f"Be {players[random.randint(0, len(players) - 1)]}'s friend for 30 minutes of the session without them getting suspicious of it being your task.", "Give another player a gift, and have them give you something in return.", "You are the Boogeyman. Kill another player by the end of the session. If you fail, you get put to your last life.", f"Steal a resource from {players[random.randint(0, len(players) - 1)]} without them noticing you. If they notice you, you fail."
]

print(tasks)

while players:
    current_player = players.pop(random.randint(0, len(players) - 1))
    print(f"It is {current_player}'s turn.")
    character_name = input("What is your character's name? ")

    if tasks:
        user_task = tasks.pop(random.randint(0, len(tasks) - 1))
        print(user_task)
        if current_player in user_task:
            tasks.append(user_task)
            user_task = tasks.pop(random.randint(0, len(tasks) - 1))
        else:
            print(f"Hello, {character_name}. Your task is: {user_task}")
    else:
        print("No tasks left!")

    print(tasks)
    time.sleep(1)
