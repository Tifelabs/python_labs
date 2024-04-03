#Lab 10 -1
# ========================================= LEARNING PYTHON =========================================
print("Lab 10-1")
with open('learning_python.txt', 'r') as file:
    # Read the entire file and print its contents
    contents = file.read()
    print("Printing the contents:")
    print(contents)

# Open and read the file again
with open('learning_python.txt', 'r') as file:
    # Read lines into a list and loop over each line
    lines = file.readlines()
    print("\nPrinting the contents by looping over each line:")
    for line in lines:
        print(line.strip())  
print("\n \n")

#Lab 10-2
# ========================================= LEARNING C =========================================
print('Lab 10-2')
with open('learning_python.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Replace 'Python' with 'C' and print the modified line
        modified_line = line.replace('Python', 'C')
        print(modified_line, end='')  

#Lab 10-3
# ========================================= SIMPLER CODE =========================================
print("Lab 10-3")
# file_reader.py
filename = 'sample.txt'
with open(filename) as file_object:
    for x in file_object.read().splitlines():
        print(x)
print("\n \n")

#Lab 10-4
# ========================================= GUEST =========================================
# Prompt the user for their name
name = input("Please enter your name: ")

# Open the file in write mode and write the name to it
with open("guest.txt", "w") as file:
    file.write(name)

print("Hello your name has been written to guest.txt.")
print("\n \n")

#Lab 10-5
# ========================================= GUEST BOOK =========================================
# Creating an empty list to store names
guest_list = []

# Creating a while loop to ask for names
while True:
    name = input("Hello!, enter your name (or type 'exit' to quit): ")
    
    # Check if the user wants to exit the loop
    if name.lower() == 'exit':
        break
    
    # Adding the name to the list
    guest_list.append(name)

# Open the file in write mode and write names to it, one per line
with open("guest_book.txt", "w") as file:
    for name in guest_list:
        file.write(name + "\n")

print("Names have been written to guest_book.txt.")

#Lab 10-6
# ========================================= ADDITION =========================================

while True:
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
        break  # exit the loop if successful
    except ValueError:
        print("Please enter valid numbers.")

# 10-7
# ========================================= Addition Calculator =========================================
while True:
    try:
        num1 = int(input("Enter the first digit: "))
        num2 = int(input("Enter the second digit: "))
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Please enter valid digits.")
    else:
        another = input("Do you want to add more numbers? (yes/no): ").lower()
        if another != 'yes':
            break

#Lab 10-8
# ========================================= CATS AND DOGS =========================================
try:
    with open('cats.txt') as cat_file:
        cat_names = cat_file.read().splitlines()
    with open('dogs.txt') as dog_file:
        dog_names = dog_file.read().splitlines()

    print("Cats:")
    for cat in cat_names:
        print(cat)
    print("\nDogs:")
    for dog in dog_names:
        print(dog)
except FileNotFoundError:
    print("One of the files is missing!")

#Lab 10-9. Silent Cats and Dogs
try:
    with open('cats.txt') as cat_file:
        cat_names = cat_file.read().splitlines()
    with open('dogs.txt') as dog_file:
        dog_names = dog_file.read().splitlines()

    print("Cats:")
    for cat in cat_names:
        print(cat)
    print("\nDogs:")
    for dog in dog_names:
        print(dog)
except FileNotFoundError:
    pass  

#Lab 10-10. 
# ========================================= COMMON WORDS =========================================
print('Lab 10-10')
def count_word_occurrences(file_name, word):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            return text.lower().count(word.lower())
    except FileNotFoundError:
        return 0
# Replace with actual file names
files_to_analyze = ['file1.txt', 'file2.txt', 'file3.txt']  
word_to_count = 'the'
for file_name in files_to_analyze:
    count = count_word_occurrences(file_name, word_to_count)
    print(f"The word '{word_to_count}' appears {count} times in {file_name}.")
print("\n \n")

#Lab 10-11
# ========================================= FAVOURITE NUMBER =========================================
print("Lab 10-11")
import json

favorite_number = input("What is your favorite number? ")
filename = 'favorite_number.json'

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
    print(f"We'll remember your favorite number: {favorite_number}")
print("\n \n")

#lab 10-12
# ========================================= FAVOURITE NUMBER REMEMBERED =========================================
print("Lab 10-12")
import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        favorite_number = json.load(f)
        print(f"I know your favorite number! It's {favorite_number}")
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
print("\n \n")

#Lab 10-13
# ========================================= USER DICTIONARY =========================================
print("Lab 10-13")
import json

filename = 'user_info.json'

try:
    with open(filename) as f:
        user_info = json.load(f)
        print(f"Welcome back, {user_info['username']}!")
        print(f"We know the following about you:")
        for key, value in user_info.items():
            if key != 'username':
                print(f"{key.capitalize()}: {value}")
except FileNotFoundError:
    user_info = {}
    user_info['username'] = input("Enter your username: ")
    user_info['favorite_number'] = input("What is your favorite number? ")
    user_info['city'] = input("Where are you from? ")
    
    with open(filename, 'w') as f:
        json.dump(user_info, f)
print("\n \n")

#Lab 10-14
# ========================================= VERIFY USER =========================================
print("Lab 10-14")
import json

filename = 'user_info.json'

def get_new_username():
    new_username = input("Enter your username: ")
    user_info['username'] = new_username
    with open(filename, 'w') as f:
        json.dump(user_info, f)

try:
    with open(filename) as f:
        user_info = json.load(f)
        username = input(f"Is your username {user_info['username']}? (yes/no) ")
        if username.lower() != 'yes':
            get_new_username()
        print(f"Welcome back, {user_info['username']}!")
        print(f"We know the following about you:")
        for key, value in user_info.items():
            if key != 'username':
                print(f"{key.capitalize()}: {value}")
except FileNotFoundError:
    user_info = {}
    get_new_username()
    user_info['favorite_number'] = input("What is your favorite number? ")
    user_info['city'] = input("Where are you from? ")
    
    with open(filename, 'w') as f:
        json.dump(user_info, f)





