 #Labs 4 -1
print("Labs 4-1")
favourite_pizza = ["pepperoni","chesse","vegetable"]
for x in favourite_pizza:
    print(f"I love {x} pizza")
print("I really love eating pizzas")
print("\n \n")

#Labs 4-2
print("Labs 4-2")
animals = ["goat","rabbit","dog"]
for y in animals:
     print(f"A {y} would make a great pet")
print("Any of these animals would make a great pet")
print("\n \n")

#Labs 4-3
print("Labs 4-3")
for number in range(1, 21):
    print(number)
print("\n \n")

#LAbs 4-4
print("Labs 4-4")
for number in range(1, 1000001):
    print(number)
print("\n \n")

#Labs 4-5
print("Labs 4-5")
numbers = list(range(1, 1000001)) 
min_number = min(numbers)
max_number = max(numbers)

# Calculate the sum of all the numbers in the list
total_sum = sum(numbers)

print("Minimum:", min_number)
print("Maximum:", max_number)
print("Sum:", total_sum)
print("\n \n")

#Labs 4-6
for number in range(1, 21, 2):
    print(number)
print("\n \n")

#Labs 4-7
print("Labs 4-7")
multiples_of_three = list(range(3, 31, 3)) 

for number in multiples_of_three:
    print(number)
print("\n \n")

#Labs 4-8
print("Labs 4-8")
cubes = [] 

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# Print out the values of the cubes
for cube in cubes:
    print(cube)
print("\n \n")

#Labs 4-9
print("Labs 4-9")
cubes = [number ** 3 for number in range(1, 11)]

# Print out the values of the cubes
for cube in cubes:
    print(cube)
print("\n \n")

#Labs 4-10
print("Labs 4-10")
numbers = list(range(1, 11))

# Print the first three items in the list
print("The first three items in the list are:")
print(numbers[:3])

# Print three items from the middle of the list
print("Three items from the middle of the list are:")
print(numbers[3:6])

# Print the last three items in the list
print("The last three items in the list are:")
print(numbers[-3:])
print("\n \n")

#Labs 4-11
print("Labs 4-11")
Tife_pizzas = ['Meat', 'Pepperoni', 'Vegetarian']

# Create a copy of your favorite pizzas for your friend
friend_pizzas =Tife_pizzas.copy()

# Add a new pizza to your list
Tife_pizzas.append('Hawaiian')

# Add a different pizza to your friend's list
friend_pizzas.append('Skushis')

# Print your favorite pizzas
print("My favorite pizzas are:")
for pizza in Tife_pizzas:
    print(pizza)

# Print your friend's favorite pizzas
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
print("\n \n")

#Labs 4-12
print("Labs 4-12")
my_foods = ['Pizza', 'Pasta', 'Burger', 'Sushi', 'Ice Cream']

# friend's favorite foods
friend_foods = ['Steak', 'Salad', 'Tacos', 'Sushi', 'Chocolate Cake']

# Print your favorite foods using a for loop
print("My favorite foods:")
for food in my_foods:
    print(food)

# Print your friend's favorite foods using a for loop
print("\nMy friend's favorite foods:")
for food in friend_foods:
    print(food)
print("\n \n")

#LAbs 4-13
print("LAbs 4-13")
menu = ('Pizza', 'Burger', 'Salad', 'Pasta', 'Fries') 

#restaurant food offers using a for loop
print("Original menu:")
for food in menu:
    print(food)

#restaurant changed its menu
menu = ('Sushi', 'Burger', 'Tacos', 'Pasta', 'Soup')

# Print each item on the revised menu using a for loop
print("\nRevised menu:")
for food in menu:
    print(food)
print("\n \n")




