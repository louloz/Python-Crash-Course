# Ch9 Classes

# Louis Lozano
# 4-01-2019
# cat_admin.py

# Python Version: 3.5.3
# Description: Demonstrates import working with multiple modules.

from admin import Admin

admin_cat = Admin('squeaky', 'pscholka', 4, 'gimmiefood@maily.com')

admin_cat.privileges.show_privileges()
