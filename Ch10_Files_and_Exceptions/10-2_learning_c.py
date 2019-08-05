# Python Crash Course, Eric Matthes, no starch press
# Ch10 Files and Exceptions
# Textbook Exercises

# Louis Lozano
# 06-20-2019
# 10-2_learning_c.py

# Python Version: 3.5.3
# Description: Prints the contents of a text file replacing instances of
#   'Python' with 'C'.

# Stores the file name of the file we are working with in a varibale.
filename = 'learning_python.txt'

# Opens the file with 'file_object' representing the file.
# 'with' keyword is used to automatically close the file when it is no longer
# needed.
with open(filename) as file_object:
    # Reads file contents and stores it in the varibale 'contents'.
    contents = file_object.read()
    # 'replace()' method is used to replace 'Python' with 'C' in the files text.
    print(contents.replace('Python', 'C'))
