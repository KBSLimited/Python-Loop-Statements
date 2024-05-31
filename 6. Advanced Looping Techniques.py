#Task 1: The Selective DJ

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# Create a sublist of genres from the second to the fourth track
sublist_genres = genres[1:4]

# Loop through the sublist of genres
for genre in sublist_genres:
    print(genre)

#Task 2: The One-Liner Band with List Comprehensions

# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

# List comprehension to append "Music" to each genre
genres_with_music = [genre + " Music" for genre in genres]

# Print the new list
print(genres_with_music)

#Task 3: Numerical Beats with range

# Loop using range() to print countdown
for i in range(10, 0, -1):
    print(i)

# Print the message after countdown
print("The beat drops now!")
