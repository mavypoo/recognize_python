num1 = 42 #variable_declaration, number_initialized
num2 = 2.3 #variable_declaration, float_initialized
boolean = True #variable_declaration, boolean_initialized
string = 'Hello World' #variable_declaration, string_initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list_initialized, variable_declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary_initialized, variable_declaration
fruit = ('blueberry', 'strawberry', 'banana') #tuples_initialized, variable_declaration
print(type(fruit)) #type_check, string
print(pizza_toppings[1]) #printing_to_console, access_value_index_1

pizza_toppings.append('Mushrooms') #adding_value_mushrooms, list
print(person['name']) #print_to_console_John, access_dictionary
person['name'] = 'George' #change_value, dictionary
person['eye_color'] = 'blue'#change_value, dictionary

#conditionals: if, elif, else
if num1 > 45: #evaluating 
    print("It's greater") #print_to_console 
else: #evaluating  
    print("It's lower") #print_to_console 

if len(string) < 5: #evaluating_if_conditional
    print("It's a short word!") #print_to_console 
elif len(string) > 15: #evaluating_elif_conditional
    print("It's a long word!") #print_to_console 
else: #evaluating, else_conditional
    print("Just right!") #print_to_console 

#for and while loops
for x in range(5):
    print(x) #print_to_console 
for x in range(2,5):
    print(x) #print_to_console 
for x in range(2,10,3):
    print(x) #print_to_console 
x = 0 #variable_declaration, number_initialized 
while(x < 5): #evaluating
    print(x) #print_to_console
    x += 1 #incremement

pizza_toppings.pop() #removes_last_value_in_the_list
pizza_toppings.pop(1) #removes_value_index1_in_the_list

print(person) #print_to_console
person.pop('eye_color') #remove_key_value_in_dictionary
print(person) #print_to_console

for topping in pizza_toppings:
    if topping == 'Pepperoni': #evaluating; pepperoni_not_included, conditionals_if
        continue #continue 
    print('After 1st if statement') #print to console
    if topping == 'Olives': #evaluating, stops_at_olives_does_not_continue, conditionals_if
        break #break

def print_hello_ten_times(): #def_function
    for num in range(10): #for_loop
        print('Hello') #print_to_console

print_hello_ten_times() #calling_function

def print_hello_x_times(x): #def_function, parameter_included
    for num in range(x): #for_loop
        print('Hello') #print_to_console

print_hello_x_times(4) #call_function_with_arguement

def print_hello_x_or_ten_times(x = 10):  #def_function, 
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #default_paramenter_print_to_console_10x
print_hello_x_or_ten_times(4) #arguement_print_to_console4x


"""
Bonus section
"""

print(num3)  #print_72
num3 = 72 #variable_declaration, initalized 
fruit[0] = 'cranberry' #replace_index0_value
print(person['favorite_team']) #print_to_console
print(pizza_toppings[7]) #print_index7
  print(boolean) #NameError: name <variable name> is not defined
fruit.append('raspberry') #add_value
fruit.pop(1) #remove_value_index1