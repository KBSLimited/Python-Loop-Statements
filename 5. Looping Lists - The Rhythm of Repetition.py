#Task 1: The for Loop DJ Set

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Iterating through genres with a counter
for index, genre in enumerate(genres, start=1):
    print(f"Track {index}: Genre - {genre}")

#Task 2: The Remix Artist with while

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Initialize track counter
track_number = 1

# Iterate through genres using a while loop
index = 0
while index < len(genres):
    # Get the genre at the current index
    genre = genres[index]
    
    # Print the track number and genre
    print(f"Track {track_number}: Genre - {genre}")
    
    # Check if the genre is "Hip-hop"
    if genre == "Hip-hop":
        print("Hip-hop genre encountered. Stopping the loop.")
        break  # Exit the loop
        
    # Move to the next genre
    index += 1
    track_number += 1

#Task 3: Light Show Technician Loop

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Loop through genres by index using range()
for index in range(len(genres)):
    # Get the genre at the current index
    genre = genres[index]
    
    # Check if the genre is not suitable for the light show
    if genre == 'Classical':
        print(f"Skipping {genre} genre.")
        continue  # Skip to the next iteration
    
    # Calculate the track number (index + 1)
    track_number = index + 1
    
    # Print the track number and message indicating light show readiness
    print(f"Track {track_number}: Light show ready for {genre}.")