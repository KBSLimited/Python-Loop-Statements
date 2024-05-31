#Task 1: Random Choice Game

import random

# List of items
items = ["apple", "banana", "cherry", "date", "grape", "kiwi", "orange"]

# Randomly select an item from the list
selected_item = random.choice(items)

# Game loop
while True:
    # Take user's guess
    guess = input("Guess which item was selected: ")
    
    # Check if the guess is correct
    if guess.lower() == selected_item:
        print("Congratulations! You guessed correctly.")
        break  # Exit the game loop
    else:
        print("Sorry, that's not the correct item. Try again.")