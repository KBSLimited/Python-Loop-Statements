#Task 1: Your Mood Tracker

import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Tired", "Excited", "Angry", "Content"]

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Times of the day
times_of_day = ["morning", "afternoon", "evening"]

# Nested loops to track mood for each day and time
for day in days_of_week:
    for time in times_of_day:
        # Randomly select a mood
        selected_mood = random.choice(moods)
        # Print the mood for the day and time
        print(f"On {day} {time} you were {selected_mood}.")