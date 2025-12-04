#. Positional Arguments.

# def display_pets(animal_type,animals_name):
#     """describe animals type && animals name"""
#     print(f"\nI have {animal_type}")
#     print(f"It's name is: {animals_name}")

# # display_pets("Cat","Hamister")
# # display_pets("Dog","kilo")
# display_pets(animal_type="cat",animals_name="humi"

# def make_shirt(size,message):
#     """described what should the parameters be"""
#     print(f"the size is {size} and {message}")

# make_shirt("XXL", "it's quite big")
# make_shirt(size="XXL",message="it's quite big")

# #-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message.
# def make_shirt(size="large",message="I love python"):
#     print(f"make a {size} shirt and  {message}")
    
# make_shirt()  # prints make a large shirt and i love python.
# make_shirt("medium")
# make_shirt("small")
# make_shirt()


# def setting_defaults():
#     print("defaults not set")


# setting_defaults()

# Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.

# def describe_cty(city="",country="Kenya"):
#     print(f"{city} is in {country}")


# describe_cty(city="Nairobi")
# describe_cty(city="Mandera")
# describe_cty(city="Mogadishu",country="somalia")


#.Create a function that returns fullname i.e first,middle(optional) && last name.

def area(width,length):
    return width*length
    
    #rint(str(width*length)+"square feet")


def main():
   name=area(50,20)
   extra=area(50,50)
   total=name+extra
   print(f"the total area is {total} feet")

main()