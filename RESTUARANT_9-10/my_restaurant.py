from restuarant import Restaurant
# Creating an instance of the Restaurant
restaurant = Restaurant("Tife Foods", "Canadian")

# Printing the attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()