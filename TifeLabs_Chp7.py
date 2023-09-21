#Lab 7-1
# ========================================= RENTAL CAR =========================================
print("Lab 7-1")
Message = input("What kind of rental car would you like?: ").title()
print(f"Let me see if I can find you a {Message}")
print("\n \n")

#Lab 7-2
# ========================================= RESTAURANT SEATING =========================================
print("Lab 7-2")
num_people = int(input("How many people are in your dinner group? "))
if num_people > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")
print("\n \n")

#Lab 7-3
# ========================================= MULTIPLES OF TEN ========================================
print("Lab 7-3")
user_number= int(input("Enter a number: "))
if user_number % 10 == 0:
    print("This is a multiple of 10")
else:
    print("This is not a multiple of 10")
print("\n \n")

#Lab 7-4
# ========================================= PIZZA TOPPINGS =========================================
print("Lab 7-4")
while True:
    toppings = input("Enter pizza  toppings('enter quit to finish'): ")
    if toppings == "quit":
        break
    print(f"I will add {toppings} to the pizza")
    
#Lab 7-5
# ========================================= MOVIE TICKETS =========================================
print("Lab 7-5")
while True:
    try:
        age = int(input("Enter your age (or enter 'quit' to exit): "))
    except ValueError:
        print("Invalid input. Please enter a valid age.")
        continue
    
    if age == "quit":
        break  # Exit the loop if the user enters '0'

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

print("Thank you for using our movie ticket service!")
print("\n \n")

#Lab 7-6
# ========================================= THREE EXITS =========================================
print("Lab 7-4")
# Using a conditional test in the while statement to stop the loop

while True:
    age = int(input("Enter your age (or enter '0' to finish): "))
    
    if age == 0:
        break  # Exit the loop if the user enters '0'

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

print("Thank you for using our movie ticket service!")
print("\n \n")

# Using an active variable to control how long the loop runs
active = True

while active:
    age = int(input("Enter your age (or enter '0' to finish): "))
    
    if age == 0:
        active = False  # Set active to False to exit the loop

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

print("Thank you for using our movie ticket service!")
print("\n \n")

# Using a break statement to exit the loop when the user enters 'quit' value
while True:
    age = int(input("Enter your age (or enter '0' to finish): "))
    
    if age == 0:
        break  

    if age < 3:
        print("Your ticket is free.")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

print("Thank you for using our movie ticket service!")
print("\n \n")

#Lab 7-7
# ========================================= INFINITY =========================================
print("Lab 7-7")
#while True:
   # print("I love Mangoes")

#Lab 7-8
# ========================================= DELI =========================================
print("Lab 7-8")
sandwich_orders = ["titus", "turkey", "club", "pork belly", "pastrami", "ham"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()  # Take the last sandwich order
    
    # Simulate making the sandwich
    print(f"I made your {current_sandwich} sandwich.")
    
    # Add the finished sandwich to the list
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())  # Capitalize the sandwich names for better formatting
print("\n \n")

#Lab 7-9
# ========================================= NO PASTRAMI =========================================
print("Lab 7-9")
# Create a list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ["tuna", "pastrami", "turkey", "pastrami", "club", "pastrami", "blt", "ham"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Notify the deli has run out of pastrami
print("Sorry, we've run out of pastrami sandwiches.")

# Remove all occurrences of 'pastrami' from sandwich_orders using a while loop
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through the list of sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()  # Take the last sandwich order
    
    # Simulate making the sandwich
    print(f"I made your {current_sandwich} sandwich.")
    
    # Add the finished sandwich to the list
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.capitalize())  # Capitalize the sandwich names for better formatting
print("\n \n")

#Lab 7-10
# ========================================= DREAM VACATION =========================================
# Create an empty list to store the poll responses
dream_vacations = []

# Set up a flag to continue polling
polling_active = True

while polling_active:
    # Prompt the user for their dream vacation destination
    response = input("If you could visit one place in the world, where would you go? ")
    
    # Add the response to the list
    dream_vacations.append(response)
    
    # Ask if they want to continue polling
    another_response = input("Would you like to poll another person? (yes/no): ")
    
    if another_response.lower() != 'yes':
        polling_active = False  # End the poll if the user doesn't want to continue

# Polling is complete, print the results
print("\n--- Poll Results ---")
for index, destination in enumerate(dream_vacations, start=1):
    print(f"Person {index}: {destination}")









