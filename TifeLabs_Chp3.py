#Lab 3-1
print("Lab 3-1")
names = ["Tooto","Gbenga","Ehiz"]
print(names[0])
print(names[1])
print(names[2])
print("\n  \n")

#Lab 3-2
print("Lab 3-2")
names = ["Tooto","Gbenga","Ehiz"]
message = "Hello!"
print(f"{message}, {names[0]}")
print(f"{message}, {names[1]}")
print(f"{message}, {names[2]}")
print("\n  \n")

#Lab 3-3
print("Lab 3-3")
favourite_transport = ["Plane","Boat","Car"]
print(f"I would like to own a big boeing {favourite_transport[0]}")
print(f"I would like to own a speed {favourite_transport[1]}")
print(f"I would like to own a super {favourite_transport[2]}")

#Lab 3-4
print("Lab 3 - 4")
guest = ["Tooto","Gbenga","Ehiz"]
invitation = "I would like to invite you for a dinner out"
print(f"Hello {guest[0]}, {invitation}")
print(f"Hello {guest[1]}, {invitation}")
print(f"Hello {guest[2]}, {invitation}")
print("\n \n")

# Lab 3-5
print("Lab 3-5")
# My Guest List
guests = ["Tooto", "Gbenga", "Ehiz","Royce"]

# My guest invitation
for x in guests:
    print(f"Hello {x}, I would like to invite you for a dinner out")

# Guest who won't be able to make it
cannot_attend = 'Ehiz'

# Print guest who can't make it
print(f"\nDamn, {cannot_attend} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new guest
new_guest = 'Sean'
guests[guests.index(cannot_attend)] = new_guest

# for loop for the new list
for y in guests:
    print(f"Hello {y}, I would like to invite you for a dinner out")
print("/n /n")


#Lab 3-6
print("Lab 3-6")
guests = ["Tooto", "Gbenga", "Ehiz","Royce"]

for x in guests:
    print(f"Hello {x}, I would like to invite you for a dinner out")

# Guest who can't make it
cannot_attend = 'Ehiz'

# Print guest who can't make it
print(f"\nDamn, {cannot_attend} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new guest
new_guest = 'Sean'
guests[guests.index(cannot_attend)] = new_guest

# for loop for the updated list
for y in guests:
    print(f"Hello {y}, I would like to invite you for a dinner out")

# Inform about the bigger table
print("\nWow! I found a bigger dinner table.\n")

# Add new guests using insert() and append()
guests.insert(0, 'Amanda')  # Add at the beginning
guests.insert(len(guests) // 2, 'Michael')  # Add in the middle
guests.append('Sophia')  # Add at the end

# Print invitation messages for all guests
for y in guests:
    print(f"Hello {y}, I would like to invite you for a dinner out")
print("/n /n")

#Lab 3-7
print("Lab 3-7")
guests = ["Tooto", "Gbenga", "Ehiz", "Sean", "Royce"]

# My guest invitation
for x in guests:
    print(f"Hello {x}, I would like to invite you for a dinner out")

# Guest who can't make it
cannot_attend = 'Ehiz'

# Print guest who can't make it
print(f"\nUnfortunately, {cannot_attend} can't make it to the dinner.\n")

# Replace the guest who can't make it with a new guest
new_guest = 'David'
guests[guests.index(cannot_attend)] = new_guest

# for loop for the updated list
for y in guests:
    print(f"Hello {y}, I would like to invite you for a dinner out")

# Inform about the bigger table
print("\nWow! I found a bigger dinner table.\n")

# Add new guests using insert() and append()
guests.insert(0, 'Lekan')  
guests.insert(len(guests) // 2, 'Derrick')
guests.append('Kashif') 

# Print invitation messages for all guests
for guest in guests:
    print(f"Hello {guest}, I would like to invite you for a dinner out")

# Inform that there's only space for two guests
print("\nSorry, I can only invite two people for dinner.")

# Use pop() to remove guests until only two are left
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to the dinner.")

# Print invitation messages for the two remaining guests
for remaining_guest in guests:
    print(f"You're still invited, {remaining_guest}!")

# Use del to empty the list
del guests[:]
print("\nAfter removing all guests, the list is now:", guests)
print("\n \n")

#Lab 3-8             
print("Lab 3-8")
dream_city = ["San fransico", "Tokyo", "New York", "Huwaii", "Cape"]

# Print the list in its original order
print("Original order:", dream_city)

# Print the list in alphabetical order without modifying the actual list
print("Alphabetical order:", sorted(dream_city))

# Show that the list is still in its original order
print("Original order:", dream_city)

# Printing our reverse-alphabetical order without changing the original list
print("Reverse alphabetical order:", sorted(dream_city, reverse=True))

# Show that the list is still in its original order
print("Original order:", dream_city)

# Use reverse() to change the order of your list
dream_city.reverse()
print("Reversed order:", dream_city)
# Using reverse() to change the order of your list again
dream_city.reverse()
print("Original order:", dream_city)

# changing your list to stored in alphabetical order
dream_city.sort()
print("Alphabetical order:", dream_city)

# storing in reverse-alphabetical order
dream_city.sort(reverse=True)
print("Reverse alphabetical order:", dream_city)
print("/n /n")

#Lab 3-9
guests = ["Tooto", "Gbenga", "Ehiz","Royce"]
print(f"I am inviting {len(guests)} friends to my party")
print("/n /n")

#Lab 3-10
language = ["French","spanish","mandari","chinese","Yoruba"]
print("Original list:", language)

# Append an element to the list
language.append("igbo")
print("New Language:", language)