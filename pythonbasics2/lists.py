#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:
#create a list
thislist = ["apple", "banana", "cherry"]
print(thislist)


#Since lists are indexed, lists can have items with the same value
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


#List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]


#From Python's perspective, lists are defined as objects with the data type 'list':
mylist = ["apple", "banana", "cherry"]  #<class 'list'>
print(type(mylist))


#it is also possible to use the list(), constructor when creating a new list
thislist=list(("apple","banana","cherry")) #note the double round-brackets
print(thislist)





# List - is a collection which is ordered and changeable.Allows duplicate members
# Tuple - Is a collection which is ordered and unchangeable.Allows duplicate members
# Set - is a collection which is unordered ,unchangeable*,and unidexed.No duplicate members
# Dictionary - is a collection which is ordered** and changeable.No duplicate members


#list items are indexed and you can access them by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])


#Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


#You can specify a range of indexes by specifying where to start and where to end the range.
#When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#By leaving out the end value, the range will go on to the end of the list:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])





#To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#To change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)


#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)





#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#To insert a list item at a specified index, use the insert() method.
#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


#To append elements from another list to the current list, use the extend() method.
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#The remove() method removes the specified item.
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #remove "banana"
print(thislist)


#if there are more than one item with the specified value, the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


#The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#If you do not specify the index, the pop() method removes the last item.
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


#The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


#The del keyword can also delete the list completely.
thislist = ["apple", "banana", "cherry"]
del thislist


#The clear() method empties the list.
#The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)




#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#You can also loop through the list items by referring to their index number.
#Use the range() and len() functions to create a suitable iterable.
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#You can loop through the list items by using a while loop
#Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1


#List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#With list comprehension you can do all that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#The condition is like a filter that only accepts the items that evaluate to True.
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if x != "apple"]
print(newlist)

#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
fruits=["apple","banana","cherry","kiwi","mango"]
newlist = [x for x in fruits]
print(newlist)

#You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

#Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#To sort descending, use the keyword argument reverse = True:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#You can use the built-in List method copy() to copy a list.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) #mylist = thislist[:]
print(mylist)

#One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3] #for x in list2: list1.append(x)
list3 = list1 + list2 #extend(list2)
print(list3)



#append() Adds an element at the end of the list
#clear() Removes all the elements from the list
#copy() Returns a copy of the list
#count() Returns the number of elements with the specified value
#extend() Add the elements of a list (or any iterable), to the end of the current list
#index() Returns the index of the first element with the specified value
#insert() Adds an element at the specified position
#pop() Removes the element at the specified position
#remove() Removes the item with the specified value
#reverse() Reverses the order of the list
#sort() Sorts the list


















