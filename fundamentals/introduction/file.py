num1 = 42       #variable declaration
num2 = 2.3      #variable declaration
boolean = True
string = 'Hello World'
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']         #strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #strings
fruit = ('blueberry', 'strawberry', 'banana')       #strings
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])

if num1 > 45:   #if conditional
    print("It's greater")
else:           #else conditional
    print("It's lower")

if len(string) < 5:     #if conditional
    print("It's a short word!")
elif len(string) > 15:  #else if conditional
    print("It's a long word!")
else:                   #else conditional
    print("Just right!")    

for x in range(5):  #for start
    print(x)        #for stop
for x in range(2,5):    #for start
    print(x)            #for stop
for x in range(2,10,3): #for start
    print(x)            #for stop
x = 0   #variable declaration
while(x < 5):   #while loop
    print(x)
    x += 1      #end while loop

pizza_toppings.pop()    #delete value
pizza_toppings.pop(1)   #add value

print(person)   
person.pop('eye_color') #delete value -string
print(person)

for topping in pizza_toppings:  #same as text file
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():    #function
    for num in range(10):       
        print('Hello')          #return

print_hello_ten_times()     #function

def print_hello_x_times(x):     #function
    for num in range(x):
        print('Hello')          #return

print_hello_x_times(4)  #function

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x):
        print('Hello')

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