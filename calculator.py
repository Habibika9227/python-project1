# x =input("what's x ")
# y =input("what's y ")
# z =int(x)+int(y)
# print(z)


# How about modifying previous code to something new.
# x = int(input("enter a valid integer of x: ")) #. Here we perfomed nesting functions.
# y = int(input("enter a valid integer of y: "))
# print(x+y)

# .Roundind off and floating
# x=float(input("put ur float value: "))
# y=float(input("put ur float value: " ))
# z= round(x+y)
# print(z)


# .including commaor any sperator

# x=float(input("what's your float value x: "))
# y=float(input("what's your float value y: "))
# z=round(x+y)
# print(f"the result is: {z:_}")

# Rounding to the nearest number
# x=float(input("enter a valid x value: "))
# y=float(input("enter a valid value of y:"))
# z=round(x/y ,3 ) #. follow this format round(number [,ndigits])
# print(f"ur value is: {z}")

# .Another way of rounding.
# x=float(input("enter value of x: "))
# y=float(input("enter value of y: "))
# #. z=round(x/y, 2).. this is one way to do desired rounding.
# z=x/y
# print(f"Your result is:{z:.4f}")


# .Starting function defining.

# def hello(mauu):
#     """describing my message"""
#     print("Hi" , mauu)
# #.Ask user name
# name=input("what's ur name? ")
# hello(name)

# function is block of reusable code.

# def happy_birthday(name,age):
#     print(f"happy birthday to you{name}") 
#     print(f"you are {age} years old")
#     print("eat well") 
# happy_birthday("Ahmed",20)

# .Second exercise

# def greeting_user(name=input("enter your name darling: ")):
#     print("hello world ")
#     print(f"Hello, {name}")
#     print(f"you are {name}")

# greeting_user("name")

#.more trial
# def greeting_user(name,age):
#     print("Hello world!")
#     print(f"Hello, {name}")
#     print("your age is: ", {age})

# name=input("Enter your name: ")
# name=name.strip().title()
# age=input("Enter valid number: ")  # i want to seperator within my code
# greeting_user(name,age)


# def hallo(greetings="World", age=" "):
#     print("Hello,", greetings) # prints hello+world
# def hallo(greetings="World", age=" "):
#     print("Hello,", greetings) # prints hello+world
#     # print("you are:" ,age, "years old.")
# hallo() # invokes hallo functions
# name=input("Enter your name: ") #. asking user an input
# hallo(name) #passing as an argument whatever the user types as nameto hallo to only print that
# age=input("Enter your age: ")
# print(f"you are: {age} years old")
# # hallo(age)

#.def man()
# def display_invoice(username,amount,due_date="04/12/2025"):
#     print(f"Hello, {username}")
#     print(f"your amount is: ${amount:.3f} and your due_date{due_date}")

# username=input("put your name here: ")
# username=username.strip().title()
# amount=float(input(f"what's your amount? "))


# display_invoice(username,amount)

def main():
    x=int(input("put valid integer: "))
    print("x squared is,", square(x))

def square(n):
    return n*n
main()









































































def hallo(greetings="World", age=" "):
    print("Hello,", greetings) # prints hello+world

