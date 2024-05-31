#Task 1: Your Mood Today

import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm"]

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through days of the week
for day in days_of_week:
    # Randomly select a mood
    selected_mood = random.choice(moods)
    # Print the mood for the day
    print(f"On {day}, you were feeling {selected_mood}.")