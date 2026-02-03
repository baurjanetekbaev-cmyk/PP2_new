#Set items are unchangeable, but you can remove items and add new items.
#Create a set
thisset = {"apple", "banana", "cherry"}
print(thisset)

#The values True and 1 are considered the same value in sets, and are treated as duplicates:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#also
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

#len()
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#data type()
set1 = {"abc", 34, True, 40, "male"}

#set()
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#add()
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#update()
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#remove()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#loop by using a for:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)



# union() and update() methods joins all items from both sets
# intersection() method keeps ONLY the duplicates
# difference() method keeps the items from the first set that are not in the other sets
# symmetric difference() method keeps all items Except the duplicates
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) # we can use set3=set1|set2
print(set3)


#update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#intersection()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)  #also we can use &
print(set3)

#intersection update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)

#Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)

#difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) #also we can write with -
print(set3)

#symmetric difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) #also we can write ^
print(set3)

#symmetric difference update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

#frozenset()
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))





