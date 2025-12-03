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
def greeting_user(name,age):
    print("Hello world!")
    print(f"Hello, {name}")
    print("your age is: ", {age})

name=input("Enter your name: ")
name=name.strip().title()
age=input("Enter valid number: ")
greeting_user(name,age)
