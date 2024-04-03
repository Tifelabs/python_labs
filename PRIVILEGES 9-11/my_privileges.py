from privileges import Admin,Privileges
# List of privileges
privilege_list = ["can add post", "can delete post", "can ban user"]

# Creating an  instance of Privileges
admin_privileges = Privileges(privilege_list)

# Creating an instance of Admin and assign the privileges
admin_user = Admin("Tife", "Tooto")
admin_user.privileges = admin_privileges.privileges

# Call the show_privileges method
admin_user.show_privileges()