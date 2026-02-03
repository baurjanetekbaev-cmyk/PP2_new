#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)


#with the break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#continue()
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#range()
for x in range(2, 6):
  print(x)

#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)


#The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
  print(x)
else:
  print("Finally finished!")


#The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#Print each adjective for every fruit
#The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)


for x in [0, 1, 2]:
  pass