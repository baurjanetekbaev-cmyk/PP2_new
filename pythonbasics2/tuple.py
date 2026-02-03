#A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#To determine how many items a tuple has, use the len() function:
thistuple=("apple","banana","cherry")
print(len(thistuple))


#One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple items can be of any data type:
tuple1 = ("abc", 34, True, 40, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #tuple()

#Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#Packing a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

#you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#You can loop through the tuple items by using a for loop.
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#while()
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#count() Returns the number of times a specified value occurs in a tuple
#index() Searches the tuple for a specified value and returns the position of where it was found





