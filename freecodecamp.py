# Discussing different data types in python.

my_int_variable=34  #integer: is a no. without decimals
print(f'integer:{my_int_variable}', sep='_', end=' ')


my_float_var=12.8 #Float:a no. with decimal 
print(f'your float value is: {my_float_var}')

set_var={4,5,0} #Set:an unordered collection of elements.
print('your unordered sets: ',set_var)

dict_var={'name':'Ahmed', 'age':23} #.Dict:holds key value in curl braces
print(dict_var)

range_var={2.6,90}  #.Range:sequence of no. that usually used in loops.
print('your range is: ', range_var)

list_var=[22,11.9, 'hell']#.list:is an ordered collection of elements that suports different data types.
print(list_var)

greetings='hi'  #.Strings are immutable
greetings='Hello world'
greetings[0]='h' + greetings[1:]
print(greetings)


