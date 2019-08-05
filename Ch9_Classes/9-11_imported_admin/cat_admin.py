# Python Crash Course, Eric Matthes, no starch press
# Ch9 Classes

# Louis Lozano
# 4-01-2019
# cat_admin.py

# Python Version: 3.5.3
# Description: Imports the Admin class from the user module. Creates an
#   instance of that class. Calls a method to show the import works properly.

from user import Admin

admin_cat = Admin('squeaky', 'pscholka', 4, 'gimmiefood@maily.com')

admin_cat.privileges.show_privileges()
