# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-16-2019
# 8-7_albums.py

# Description: This program uses a function that takes two or three parameters
#   and uses them to define a dictionary. It the returns the dictioary. The
#   function is called three times and the return values are printed.

# Passing num_tracks an empty string as it's default value and putting it
#   last makes it an optional parameter.
def make_album(artist_name, album_title, num_tracks=''):
    # Checks if num_tracks is empty or not.
    #   If not, use it's value for dictionary.
    if num_tracks:
        album = {'artist': artist_name, 'title': album_title, 'songs': str(num_tracks)}
    # If num_tracks is empty, only use the first two parameters.
    else:
        album = {'artist': artist_name, 'title': album_title}
    return album

# Uses default value for num_tracks parameter. Prints dictionary.
print(make_album('Jimi Hendrix', 'Axis Of Love'))

print(make_album('Eyedea and Abilities', 'First Born'))

# Passes an argument to num_tracks. Prints dictionary.
print(make_album('Kazam', 'Raindrops', 20))
