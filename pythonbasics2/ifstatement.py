#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
a=33
b=200
if b>a:
    print("b is greater than a")


#using boolean variable
is_log=True
if is_log:
    print("Welcome")


#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#Categorizing age groups:
age = 25
if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")

# The else statement must come last. You cannot have an elif after an else
number = 7
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#Validating user input:
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")


#One-line if/else that prints a value:
a = 2
b = 330
print("A") if a > b else print("B")

#You can also use a one-line if/else to choose a value and assign it to a variable:
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#Setting a default value:
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

#Test if a is greater than b, AND if c is greater than a
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


#Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#Test if a is NOT greater than b:
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#You can have if statements inside if statements. This is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#Could also be written with and:
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")

#The pass statement is a null operation - nothing happens when it executes. It serves as a placeholder.
a = 33
b = 200
if b > a:
  pass

#Placeholder for future implementation:
age = 16
if age < 18:
  pass #  Add underage logic later
else:
  print("Access granted")

#Using pass in different branches:
value = 50
if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")


