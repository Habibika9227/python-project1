#Defining a function using def
def add(a, b):
    return a+b

#Declare a variable called x
x = add(2,3)
print("x =", x)

#create a greeting.
def greet(name):
    return "hello, " + name + "!"
message =greet("abdullahi")
print(message)
assert greet("A") == "Hello"
