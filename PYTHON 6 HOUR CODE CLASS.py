
course = 'Python for "Beginners"'
print(course[0]) #strings


first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder '
msg = f'{first} [{last}] is a coder '
print (msg) 

first = 'owen'
last  = 'akpiama'
message = first + '['+ last + '] is a coder' #formatted strings
msg = f' {first} [{last}] is a coder'
print (msg)  

 
course = 'Python for Beginners'
print(course.upper())  #string methods
print(course.lower())
print(course.replace('Beginners','Absolute Beginners'))

x = 10 + 3 * 2 ** 2
print(x)
 

is_hot = False

if is_hot:
 print("Its's a hot day")
 print("Drink plenty of water")
else: 
 print("Its's a cold day")
 print("Wear warm clothes ")
 print("Enjoy your day")