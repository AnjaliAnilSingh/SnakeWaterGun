import random
import tkinter as tk

# Function to handle the game logic
def play_game():
    y = int(entry.get())

    if y < 1 or y > 3:
        result_label.config(text="Invalid input. Please enter 1, 2, or 3.")
    else:
        x = random.randrange(1, 4)
        computer_choice_label.config(text=f"AI: {x}")
        user_choice_label.config(text=f"You: {y}")

        if x == y:
            result_label.config(text="Tie")
        elif (x == 1 and y == 2) or (x == 2 and y == 3) or (x == 3 and y == 1):
            result_label.config(text="AI won")
        else:
            result_label.config(text="You won")

# Create a Tkinter window
window = tk.Tk()
window.title("Snake Water Gun Game")

# Create labels and entry fields
instruction_label = tk.Label(window, text="Choose your move (1. Snake, 2. Water, 3. Gun):")
entry = tk.Entry(window)
play_button = tk.Button(window, text="Play", command=play_game)
computer_choice_label = tk.Label(window, text="AI:")
user_choice_label = tk.Label(window, text="You:")
result_label = tk.Label(window, text="Result:")

# Pack widgets
instruction_label.pack()
entry.pack()
play_button.pack()
computer_choice_label.pack()
user_choice_label.pack()
result_label.pack()

# Start the Tkinter main loop
window.mainloop()
