# este es un comentario de una línea
"""
Este es
un comentario
de varias líneas
"""

num1 = 42 # variable declarada, datatypes primitive numbers
num2 = 2.3  # variable declarada, datatypes primitive float
boolean = True  # variable declarada, datatypes primitive boolean
string = 'Hello World' # variable declarada, datatypes primitive string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # Data types: composite: list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # Data types: composite: dictionary
fruit = ('blueberry', 'strawberry', 'banana') # Data types: composite: list
print(type(fruit)) # log statement
print(pizza_toppings[1]) # log statement. datatype: lista
pizza_toppings.append('Mushrooms') #datatypes: lista_ addvalue
print(person['name']) # datatypes_ lista: diccionario: access value
person['name'] = 'George' # datatypes_ lista: diccionario: change value
person['eye_color'] = 'blue' # datatypes_ lista: diccionario: change value
print(fruit[2]) # Data types: composite: list: access value

if num1 > 45: # condicional :if
    print("It's greater")
else: # condicional else
    print("It's lower")

if len(string) < 5: # condicional if
    print("It's a short word!")
elif len(string) > 15: # condicional elseif
    print("It's a long word!")
else: # condicional else
    print("Just right!")

for x in range(5): # for loop
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): # while loop: start & stop0
    print(x) 
    x += 1 # while loop: increment

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # Conditional if
        continue # Conditional : continue
    print('After 1st if statement')
    if topping == 'Olives': # Conditional if
        break # Conditional break

# function
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() # Call function


# function
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) # Call function

# function
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

# Call function
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)