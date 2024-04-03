from user import User
from privilege_admin import Admin

# Create an Admin instance
admin_user = Admin("Tife", "Labs", "TifeLabs", "TifeLabs@gmail.com")

# Call show_privileges() for the Admin instance
admin_user.privileges.show_privileges()
