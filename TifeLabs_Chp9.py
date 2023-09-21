#Lab 9-1
# ========================================= RESTAURANT =========================================
print('Lab 9-1')
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name} and it serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating an instance of the Restaurant
restaurant = Restaurant("Tife Foods", "Canadian")

# Printing the attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n \n")

#Lab 9-2
# ========================================= THREE RESTAURANTS =========================================
print("Lab 9-2")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name} and it serves {self.cuisine_type} cuisine.")

# Creating three instances of the Restaurant class
restaurant1 = Restaurant("Tife Foods", "Canadian")
restaurant2 = Restaurant("Mama put", "Africa")
restaurant3 = Restaurant("Bing Chilling", "Indian")

# Calling the describe_restaurant method for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
print("\n \n")

 #Lab 9-3
 # ========================================= USERS =========================================
print("Lab 9-3")
class User:
    def __init__(self,first_name,second_name):
        self.first_name = first_name
        self.second_name = second_name
        
    def decribe_user(self):
        print(f'Hello Sir!, Your first name is {self.first_name} and your second name is {self.second_name}.')
    def greet_user(self):
        print(f"Good Morning {self.first_name}, hope you are having a good day!")
    
user_profile1 = User("Boluwatife","Olusegun")
user_profile2 = User("Derrick","Hammond")
user_profile3 = User("Lekan","Akpo")
#Calling the method fror the  instance
user_profile1.decribe_user()
user_profile2.decribe_user()
user_profile3.decribe_user()
print('\n \n')
#Calling method 2
user_profile1.greet_user()
user_profile2.greet_user()
user_profile3.greet_user()

#Lab 9-4
# ========================================= NUMBER SERVED =========================================
print("Lab 9-4")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served  # Initialize number_served with a default value of 0

    def describe_restaurant(self):
        print(f"The restaurant's name is {self.restaurant_name} and it serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

# Creating an instance of the Restaurant
restaurant = Restaurant("Tife Foods", "Canadian")

# Printing the attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
print(f"Number of customers served: {restaurant.number_served}")

# Calling the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Setting the number of customers served using the set_number_served method
restaurant.set_number_served(15)
print(f"The number of customers served are {restaurant.number_served}")

# Incrementing the number of customers served using the increment_number_served method
restaurant.increment_number_served(40)
print(f"The number of customers served are {restaurant.number_served}")

print("\n \n")

#Lab 9-5
# ========================================= LOGIN ATTEMPTS =========================================
print('Lab 9-5')
class User:
    def __init__(self, first_name, second_name, login_attempts=0):
        self.first_name = first_name
        self.second_name = second_name
        self.login_attempts = login_attempts
        
    def describe_user(self):  # Corrected the method name from 'decribe_user' to 'describe_user'
        print(f'Hello Sir!, Your first name is {self.first_name} and your second name is {self.second_name}.')
        
    def greet_user(self):
        print(f"Good Morning {self.first_name}, hope you are having a good day!")
        
    def increment_login_attempts(self, increment):
        self.login_attempts += increment
        
    def reset_login_attempts(self):
        self.login_attempts = 0  

user_profile1 = User("Boluwatife", "Olusegun")
user_profile2 = User("Derrick", "Hammond")
user_profile3 = User("Lekan", "Akpo")

# Call increment_login_attempts multiple times
user_profile1.increment_login_attempts(1)
user_profile1.increment_login_attempts(2)
user_profile1.increment_login_attempts(3)

# Print the value of login_attempts to verify the increment
print(f"Login attempts: {user_profile1.login_attempts}")

# Call reset_login_attempts to reset login_attempts to 0
user_profile1.reset_login_attempts()

# Print login_attempts again to confirm it was reset to 0
print(f"Login attempts after reset: {user_profile1.login_attempts}")
print("\n \n")

#Lab 9-6
# ========================================= ICE CREAM STAND =========================================
print('Lab 9-6')
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print(f"These are my favorite flavors:{', '.join(self.flavors)}")

# Create an instance of IceCreamStand
flavors = ["Vanilla", "Chocolate", "Strawberry", "Apple", "Oreos"]
my_ice_cream_stand = IceCreamStand("Cool Treats", "Ice Cream", flavors)

# Call the display_flavors method
my_ice_cream_stand.display_flavors()
print("\n \n")

#Lab 9-7
# ========================================= ADMIN =========================================
class User:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

class Admin(User):
    def __init__(self, first_name, second_name, privileges):
        super().__init__(first_name, second_name)
        self.privileges = privileges

    def show_privileges(self):
        print("Administrator Privileges:")
        for x in self.privileges:
            print(x)

# list of privileges
privilege_list = ["can add post", "can delete post", "can ban user"]

# Create an instance of Admin with privileges
admin_user = Admin("Tife", "Tooto", privilege_list)

# Call the show_privileges method
admin_user.show_privileges()
print("\n \n")

#Lab 9-8
# ========================================= PRIVILEGES =========================================
print('Lab 9-8')
class User:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = []

    def show_privileges(self):
        print("Administrator Privileges:")
        for privilege in self.privileges:
            print(privilege)

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

# List of privileges
privilege_list = ["can add post", "can delete post", "can ban user"]

# Creating an  instance of Privileges
admin_privileges = Privileges(privilege_list)

# Creating an instance of Admin and assign the privileges
admin_user = Admin("Tife", "Tooto")
admin_user.privileges = admin_privileges.privileges

# Call the show_privileges method
admin_user.show_privileges()
print("\n \n")

#Lab 9-9
# ========================================= BATTERY UPGRADE =========================================
print("Lab 9-9")
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

class Battery:
    def __init__(self, battery_size=40):
        """Initialize the battery attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade the battery to 65 kWh if it's not already."""
        if self.battery_size != 65:
            print("Upgrading the battery to 65 kWh.")
            self.battery_size = 65
        else:
            print("The battery is already upgraded to 65 kWh.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize an electric car."""
        super().__init__(make, model, year)
        self.battery = Battery()

# Create an electric car with the default 40 kWh battery.
my_leaf = ElectricCar('Nissan', 'Leaf', 2024)

print(my_leaf.get_descriptive_name())

# Describe the initial battery.
my_leaf.battery.describe_battery()

# Get the range with the initial battery size.
my_leaf.battery.get_range()

# Upgrade the battery.
my_leaf.battery.upgrade_battery()

# Describe the upgraded battery.
my_leaf.battery.describe_battery()

# Get the range after upgrading the battery.
my_leaf.battery.get_range()
print("\n \n")