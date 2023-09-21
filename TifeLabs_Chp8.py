#Lab 8-1
# ========================================= MESSAGE =========================================
"""
print("Lab 8-1")
def display_message():
    print('I am learning functions in this chapter ')

display_message( )
print("\n \n")

#Lab 8-2
# ========================================= FAVORITE BOOK =========================================
print("Lab 8-2")
def favorite_book(title):
    print(f"One of my favorite books is, {title}")

favorite_book("Alice in Wonderland")
print("\n \n")

#Lab 8-3
# ========================================= T-SHIRT =========================================
print("Lab 8-3")
def make_shirt(size,message):
    print(f"My shirt size is {size} medium with {message} written on it")

make_shirt(35,"Louis Vutton")
make_shirt(message="Louis Vutton",size=35)
print("\n \n")

#Lab 8-4
# ========================================= LARGE SHIRTS =========================================
print("Lab 8-3")
def make_shirt(size='large', message='I love Python'):
    print(f"\nThe size of the shirt is {size},with {message} as the tag.")

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message='Tife is a programmer')

#Lab 8-5
# ========================================= CITIES =========================================
print("Lab 8-5")
def describe_city(city_name,country = "Canada"):
    print(f"{city_name} is in {country}")

describe_city("Montreal")
describe_city("Toronto")
describe_city(city_name="Tokyo",country="Japan")
print("\n \n")

#Lab 8-6
# ========================================= CITY NAMES =========================================
print("Lab 8-6")
def city_country(city,country):
    info = f"{city.title()}, {country.title()}"
    return info

print(city_country("winnipeg", "canada"))
print(city_country("new york", "united states"))
print(city_country("tokyo", "japan"))
print("\n \n")

#Lab 8-7
# ========================================= ALBUM =========================================
print("Lab 8-7")
def make_album(artist_name,album_title,song_list=None):
    full_info = {"Artist" :artist_name,
                "Album Title": album_title}
    if song_list:
        full_info ["Number of Songs"] = song_list
    return full_info

print(make_album("Fireboy",'Laughter,Tears & Goosebumps'))
print(make_album("Olamide","Unruly"))
print(make_album("Rema","Rave & Roses "))
full_info = make_album("Tife", "Hot Tears",4)
print(full_info)
print("\n \n")

# Lab 8-8
# ========================================= USER ALBUMS =========================================
print("Lab 8-8")
def make_album(artist, album_title, songs_list=None):
    full_info = {"Artist": artist, "Album Title": album_title}
    if songs_list is not None:
        full_info["Number of Songs"] = songs_list
    return full_info

while True:
    print("Enter album information (or 'quit' to  exit):")
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'quit':
        break

    album_title = input("Enter the album title: ")
    if album_title.lower() == 'quit':
        break

    songs_list = input("Enter the number of songs (optional, press Enter to skip): ")
    if songs_list.lower() == 'quit':
        break
    elif songs_list:
        full_info = make_album(artist, album_title, int(songs_list))
    else:
        full_info = make_album(artist, album_title)

    print("Album information:")
    print(full_info)
print("\n \n")

#Lab 8-9
# ========================================= MESSAGE =========================================
print("Lab 8-9")
def show_messages(messages):
    for message in messages:
        print(message)

text_messages = ["Hello Mr. Sean\n", "My name is Tife\n", "I love Gaming\n", "Eat Well"]

show_messages(text_messages)
print("\n \n")

#Lab 8-10
# ========================================= SENDING MESSAGE =========================================
def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print("Sending message:", message)
        sent_messages.append(message)

text_messages = ["Hello Mr. Sean\n", "My name is Tife\n", "I love Gaming\n", "Eat Well"]

sent_messages = []

send_messages(text_messages, sent_messages)


print("Messages:")
print(text_messages)  
print("\nSent Messages:")
print(sent_messages)  

#Lab 8-11
# ========================================= ARCHIEVED MESSEGES =========================================
def send_messages(messages, sent_messages):
    while messages:
        message = messages.pop(0)
        print("Sending message:", message)
        sent_messages.append(message)

# Create a list of text messages
text_messages = ["Hello Mr. Sean\n", "My name is Tife\n", "I love Gaming\n", "Eat Well"]

# Create a copy of the list for sending
messages_copy = list(text_messages)

sent_messages = []

# Call the send_messages() function with the copy
send_messages(messages_copy, sent_messages)

print("Original Messages:")
print(text_messages)  
print("\nSent Messages:")
print(sent_messages)  
print("\n \n")
"""
#Lab 8-12
# ========================================= SANDWICHES =========================================
def sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for x in items:
        print(f"- {x}")
    print("Your sandwich is ready!")

# Call the function with different number of arguments
sandwich('ham', 'cheese', 'lettuce')
sandwich('turkey', 'bacon', 'tomato', 'mayo')
sandwich('peanut butter', 'jelly')
print("\n \n")

#Lab 8-13
# ========================================= USER PROFILE =========================================
# user_profile.py

def build_profile(first_name, last_name, **user_info):
    #Build user profile dictionary
    my_profile = {
        'first_name': first_name,
        'last_name': last_name,
    }
    for key, value in user_info.items():
        my_profile[key] = value
    return my_profile

# About myself
my_profile = build_profile(
    first_name='Tife',
    last_name='Labs',
    age=20,
    city='Moncton',
    hobbies=['Sleeping', 'Reading', 'Coding']
)

# Print the user profile
for key, value in my_profile.items():
    print(f"{key}: {value}")

print("\n \n")

#Lab 8-14
# =========================================  CARS =========================================
def car(manufacturer, model, **car_info):
    about_car = {
        "Manufacturer": manufacturer,
        "Model": model
    }
    for key, value in car_info.items():
        about_car[key] = value
    return about_car

about_car = car(
    manufacturer="Nissan",
    model="GTR",
    year=2023,
    speed="800 hp"
)

for key, value in about_car.items():
    print(f"{key}: {value}")
print("\n \n")


#Lab 8-15
# ========================================= PRINTING MODELS =========================================
print("Lab 8-15")
import printing_functions as tife

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

tife.print_models(unprinted_designs, completed_models)

import printing_functions as tife
tife.show_completed_models(completed_models)