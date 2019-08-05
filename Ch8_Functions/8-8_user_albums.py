# Python Crash Course, Eric Matthes, no starch press
# Ch8 Functions
# Textbook Exercises

# Louis Lozano
# 3-16-2019
# 8-8_user_albums.py

# Description: This program uses a function that takes two or three parameters
#   and uses them to define a dictionary. It the returns the dictioary. A
#   while loop allows the user to input their own arguments for the parameters.
#   The user can exit the loop at any time by entering "q". The dictionary
#   made with the users input is printed at the end of the loop.

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

# A while loop that lets the user input arguments for the functions parameters.
# A quit condition is given so the user can exit the loop at any time.
while True:
    # Displays quit condition.
    print('(Enter "q" at any time to quit.)')

    # Prompts user for input
    user_artist = input('Enter the album artist: ')
    # Exits loop if user enters "q".
    if user_artist == 'q':
        break
    
    user_title = input('Enter the album title: ')
    if user_title == 'q':
        break
    
    user_num_tracks = input('Enter the number of tracks (Press Enter to skip): ')
    if user_num_tracks == 'q':
        break
    
    # The dictionary made with the users input is printed.
    print(make_album(user_artist, user_title, user_num_tracks))
