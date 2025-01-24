import tkinter as tk
from tkinter import messagebox
import random

# Initialize data
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

current_player = None  # To track the current player
task_assigned = False  # To track if a task has been assigned


# GUI Logic
def next_turn():
    global players, current_player, task_assigned

    # Ensure a task is assigned before moving to the next turn
    if not task_assigned and current_player is not None:
        messagebox.showwarning("Task Required", "Please assign a task before moving to the next turn!")
        return

    # Clear the current task display
    task_label.config(text="")
    task_assigned_label.config(text="Task assigned: No")
    assign_task_button.config(state="normal")  # Enable the "Assign Task" button
    task_assigned = False  # Reset task assigned flag

    # Check if there are players left
    if not players:
        messagebox.showinfo("Game Over", "All players have had their turns!")
        root.destroy()  # Close the GUI
        return

    # Select the next player
    current_player = players.pop(random.randint(0, len(players) - 1))
    current_player_label.config(text=f"Current Player: {current_player}")


def assign_task():
    global tasks, current_player, task_assigned

    # Ensure a player is selected before assigning a task
    if current_player is None:
        messagebox.showwarning("Turn Error", "Please start the next turn first!")
        return

    # Validate character name input
    character_name = name_entry.get().strip()
    if not character_name:
        messagebox.showwarning("Input Error", "Please enter your character's name!")
        return

    # Assign a task
    if tasks:
        user_task = tasks.pop(random.randint(0, len(tasks) - 1))
        if current_player in user_task:
            tasks.append(user_task)  # Return task to pool
            user_task = tasks.pop(random.randint(0, len(tasks) - 1))
        task_label.config(
            text=f"Hello, {character_name}. Your task is: {user_task}"
        )
        task_assigned = True  # Mark task as assigned
        task_assigned_label.config(text="Task assigned: Yes")
        assign_task_button.config(state="disabled")  # Disable "Assign Task" button after assigning
        print(f"{current_player}'s task: {user_task}")
    else:
        task_label.config(text="No tasks left!")


# Create Tkinter GUI
root = tk.Tk()
root.title("Task Assignment Game")

# Widgets
title_label = tk.Label(root, text="Task Assignment Game", font=("Helvetica", 16))
title_label.pack(pady=10)

current_player_label = tk.Label(root, text="Current Player: ", font=("Helvetica", 12))
current_player_label.pack(pady=5)

name_label = tk.Label(root, text="Enter Character Name:")
name_label.pack(pady=5)

name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

next_turn_button = tk.Button(root, text="Next Turn", command=next_turn)
next_turn_button.pack(pady=10)

assign_task_button = tk.Button(root, text="Assign Task", command=assign_task)
assign_task_button.pack(pady=10)

task_label = tk.Label(
    root, text="Your task will appear here.", font=("Helvetica", 12), wraplength=400, justify="center"
)
task_label.pack(pady=20)

task_assigned_label = tk.Label(root, text="Task assigned: No", font=("Helvetica", 10), fg="blue")
task_assigned_label.pack(pady=5)

# Start the main loop
root.mainloop()
