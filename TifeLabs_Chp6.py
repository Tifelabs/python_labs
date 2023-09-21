#6-1
# ========================================= PESRON =========================================
print("Lab 6-1")
personal_info = {
    "first_name": "Tootoleyin",
    "last_name" :"Ogunlana",
    "age": 20,
    "city" : "Montreal"
}

print(personal_info["first_name"])
print(personal_info["last_name"])
print(personal_info["age"])
print(personal_info["city"])
print("\n \n")

#6-2
# ========================================= FAVORITE NUMBERS =========================================
print("Labs 6-2")
favorite_number = {
    "Tife": 8,
    "Tooto" : 30,
    "Nana" : 18,
    "Ashley": 21,
    "Jim" : 9
}
for key,value in favorite_number.items():
    print(f"{key}'s favorite number is {value}.")
print("\n \n")

#6-3
# ========================================= GLOSSARY #1 =========================================
print("Lab 6-3")
programming_words = {
    "Variable": "This is used for storing data and information",
    "List" : "This is use for listing and storing array of items",
    "Boolean" : "This is a True or False value",
    "String" : "This is basically series of characters",
    "Input" : " This is used for prompting user to enter an input"
    }
for key,value in programming_words.items():
    print(f"{key} {value}")
print("\n \n")

#6-4
# ========================================= GLOSSARY #2 =========================================
# Add five more terms to the glossary
programming_words["Dictionary"] = "A collection of key-value pairs."
programming_words["Conditionals"] = "This is an if-else statement"
programming_words["Module"] = "A file containing Python code that can be imported and reused."
programming_words["Algorithm"] = "A step-by-step procedure for solving a problem."
programming_words["Integer"] = "This is used as a number representation."

# Print the updated glossary using a loop
for key, value in programming_words.items():
    print(f"{key} : {value}\n")
print("\n \n")

#6-5
# ========================================= RIVERS =========================================
rivers = {
    "Nile": "Egypt",
    "Niger": "Nigerian",
    "Missisippi" : "Unites States"
}
for key,value in rivers.items():
    print(f'The {key} river run through {value}\n')
# --- --- ---
for key in rivers:
    print(f'{key}\n')
# --- --- ---
for key,value in rivers.items():
    print(f'{value}\n')

# ========================================= POLLING =========================================
#6-6
print("Lab 6-6")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

poll_list =["shewa","sarah","edward","josh","danny"]

for users in poll_list:
    if users in favorite_languages:
        print(f"{users.title()} Thanks for taking the poll\n")
    else:
        print(f"{users.title()} please take the poll.\n")
print("\n \n")

#6-7
# ========================================= PEOPLE ========================================= 
print("Lab 6-7")
people = [
    {
        "first_name": "Tootoleyin",
        "last_name" :"Ogunlana",
        "age": 20,
        "city" : "Montreal"
    },

    {
        "first_name": "Tessy",
        "last_name" :"Rays",
        "age": 19,
        "city" : "Oshawwa"
    },

    {
        "first_name": "David",
        "last_name" :"Malan",
        "age": 40,
        "city" : "Michigan"
    }
]
for x in people:
    full_name = f"{x['first_name']} {x['last_name']}"
    print(f"Full Name: {full_name}")
    print(f"Age: {x['age']}")
    print(f"City: {x['city']}")
    print("\n \n")

#6-8
# ========================================= PETS =========================================
pets = [{"Pet type" : "Dog",
        "Owners Name": "Mr. Johnson"
        },

{"Pet type" : "Cat",
"Owners Name": "Cassy"
    },

{"Pet type" : "Parrot",
"Owners Name": "Ravin"
    },

{"Pet type" : "Rabbit",
"Owners Name": "Drake"
    },

{"Pet type" : "Deer",
"Owners Name": "Jenna"
}
]
for info in pets :
    print(f'Pet Type : {info["Pet type"]}') 
    print(f"Owner Name: {info['Owners Name']}\n")     
print('\n \n')

#6-9
# ========================================= FAVOURITE PLACES =========================================
favorite_places = {
    'Tife': ['Paris', 'Tokyo', 'New York'],
    'Spikey': ['London', 'San Francisco'],
    'Charlie': ['Rome']
}
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print("\n \n")
 
#6-10
# ========================================= FAVORITE NUMBER =========================================
print("Labs 6-10")                                        
favorite_number = {
    "Tife": [8, 2, 6],
    "Tooto": [30, 17, 5],
    "Nana": [18, 1, 7],
    "Ashley": [21, 9, 0],
    "Jim": [3, 9, 4]
}

for key, value in favorite_number.items():
    print(f"{key}'s favorite numbers are {value}.")
print("\n \n")

#6-11
# ========================================= CITES =========================================
print("Lab 6-11")
cities = {
    'New York': {
        'country': 'United States',
        'population': 8398748,
        'fact': 'The Statue of Liberty is located on Liberty Island in New York Harbor.'
    },
    'London': {
        'country': 'United Kingdom',
        'population': 8982000,
        'fact': 'London is home to the famous Big Ben clock tower.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is known for its efficient and extensive public transportation system.'
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print("\n \n")

#6-12
# ========================================= EXTENSIONS =========================================
favorite_things = {
    "Tife": {
        'favorite_numbers': [8, 2, 6],
        'favorite_colors': ['blue', 'green', 'red']
    },
    "Tooto": {
        'favorite_numbers': [30, 17, 5],
        'favorite_colors': ['purple', 'orange', 'yellow']
    },
    "Nana": {
        'favorite_numbers': [18, 1, 7],
        'favorite_colors': ['pink', 'teal', 'black']
    },
    "Ashley": {
        'favorite_numbers': [21, 9, 0],
        'favorite_colors': ['white', 'brown', 'gray']
    },
    "Jim": {
        'favorite_numbers': [3, 9, 4],
        'favorite_colors': ['violet', 'cyan', 'magenta']
    }
}

# Loop through the dictionary and print each person's favorite numbers and colors
for person, favorites in favorite_things.items():
    print(f"{person}'s favorites are:")
    print(f"Favorite Numbers: {favorites['favorite_numbers']}")
    print(f"Favorite Colors: {favorites['favorite_colors']}")
    print("\n \n")


