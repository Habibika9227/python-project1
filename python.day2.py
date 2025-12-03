#.ask user name for their name.
# name=input('whats your name? ').strip().title()
# first, last =name.split()
# print(f'your name is: {first}')


name = input("enter your first name: ")
name = name.strip().title()
first, last = name.split()
print(f"your name is: {first}")

