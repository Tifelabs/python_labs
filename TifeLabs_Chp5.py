#Labs 5-1
# ========================================= CONDITIONAL TESTS =========================================
#Fruits
print("Lab 5-1")
fruit = "Apple"
print("Is fruit == 'Apple'? I predict True.")
print(fruit == "Apple")

print("\nIs fruit == 'Mango' I predict False")
print(fruit == "Mango")
print("\n \n")

 #Language
Language = "English"
print("Is Language == 'English'? I predict True.")
print(Language == "English")

print("\nIs Language == 'Spanish' I predict False")
print(Language == "Spanish")
print("\n \n")

#Country
country = "Canada"
print("Is country == 'Canada' ? I predict True.")
print(country == "Canada")

print("\nIs Language == 'Spanish' I predict False")
print(country == "Spanish")
print("\n \n")


#Drink
drink = "Fanta"
print("Is drink == 'Fanta'? I predict True.")
print(drink == "Fanta")

print("\nIs drink == 'Pepsi' I predict False")
print(fruit == "Pepsi")
print("\n \n")

#Friends
friend = "Tooto"
print("Is friend == 'Tooto'? I predict True.")
print(friend == "Tooto")

print("\nIs friend == 'Ashleye' I predict False")
print(friend == "Ashleye")
print("\n \n")

#Lab 5-2
# ========================================= MORE CONDITIONAL TEST =========================================
print("Lab 5-2")
# Tests for equality and inequality with strings
first_name = "tife"
last_name = "Labs"
print(first_name == last_name) # False
print(first_name != last_name) # True
print("\n \n")

# Tests using the lower() method
nick_name = "TIFE"
print(nick_name.lower() == first_name) # True
print("\n \n")

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
first_digit = 18
second_digit = 40
print(first_digit == second_digit) # False
print(first_digit != second_digit) # True
print(first_digit > second_digit) # False
print(first_digit < second_digit) # True
print(first_digit >= second_digit) # False
print(first_digit <= second_digit) # True
print("\n \n")

#Tests using the and keyword and the or keyword
result = 20
print((first_digit < second_digit) and (second_digit < result)) # False
print((first_digit < second_digit) or (second_digit < result)) # True
print("\n \n")

# Test whether an item is in a list
my_girlfriends = ["Tooto","Felayna","kiki","Lisa"]
my_first_girl = "Lisa"
my_second_girl = "Tooto"
print(my_first_girl in my_girlfriends) # True
print(my_second_girl in my_girlfriends) # False
print("\n \n")

# Test whether an item is not in a list
print(my_first_girl not in my_girlfriends) # False
print(my_second_girl not in my_girlfriends) # True
print("\n \n")

#5-3
# ========================================= ALIEN COLORS #1 =========================================
print("Lab 5-3")
#the correct version giving some output
alien_color = "green"
if alien_color == "green":
    print("You just earn 5 points")

#The failed version giving no output:
alien_color = "red"
if alien_color == "green":
    print("You just earn 5 points")
print("\n \n")


#5-4
# ========================================= ALIEN COLORS #2 =========================================
print("Lab 5-4 ")
alien_color = input("Enter alien color: ")
if alien_color == "green":
    print('You just earned 5 points for shooting an alien')

if alien_color != "green":
    print("You just earned 10 points")
print("\n \n")

#Version that runs the if block and another that runs the else block.
alien_color = input("Enter alien color: ")
if alien_color == "green":
    print('You just earned 5 points for shooting an alien')

else:
    print("You just earned 10 points")
print("\n \n")


#5-5
# ========================================= ALIEN COLORS #3 =========================================
print("Lab 5-5")
alien_color = input("Enter Alien Color: ").lower()
if alien_color == "green":
    print("You just earned 5 points")
elif alien_color == "yellow":
    print("You just earned 10 points")
elif alien_color == "red":
    print("You just earned 15 points")
else:
    print("Please include  Text only")
print("\n \n")

#5-6
# ========================================= STAGES OF LIFE =========================================
print("Lab 5-6")
age = 20
if age < 2:
    print("The person is a baby.")
elif age >= 2 and age < 4:
    print("The person is a toddler.")
elif age >= 4 and age < 13:
    print("The person is a kid.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
print("\n \n")

#5-7
# ========================================= FAVORITE FRUIT =========================================
print("Lab 5-7")
#list of Favourite fruits
favorite_fruits = ["mango","apple","banana"]

if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'pineapple' in favorite_fruits:
    print("You really like pineapples!")
print("\n \n")

#5-8
# ========================================= HELLO ADMIN =========================================
print("Labs 5-8")
usernames = ["admin","ehiz","dave","ashley","dan"]

for usr in usernames:
    if usr == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {usr}, thank you for logging in again.")
print("\n \n")

#5-9
# ========================================= NO USER =========================================
print("Lab 5-9")
usernames = []

if not usernames:
    print("We need to find some users!")
else:
    for usr in usernames:
        if usr == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {usr}, thank you for logging in again.")
print("\n \n")

#5-10
# ========================================= CHECKING USERNAMES =========================================
current_users = ["julia","amara","patel","suraj","rashford","tife"]
new_users = ["daniel","patel","shawty","philip","ahmed","tife"]
for x in new_users:
    if x.lower() in current_users:
        print(f'Sorry,the username {x} is already taken. Please enter a new username')
    else:
        print(f"The username {x} is available.")
print("\n \n")

#5-11
# ========================================= ORDINAL NUMBERS =========================================
numbers = list(range(1, 10))
for y in numbers:
    if y == 1:
        print(f"{y}st")
    elif y == 2:
        print(f"{y}nd")
    elif y == 3:
        print(f"{y}rd")
    else:
        print(f"{y}th")
print("\n \n")

#5-12
# ========================================= STYLING IF STATEMENTS =========================================
# I Tife really make sure that all my conditional tests are checked appropriately

#5- 12
# MY IDEAS
# I Tife might consider making some sourt of grade score book, attendence sheet projects with what i have learnt so far.





 