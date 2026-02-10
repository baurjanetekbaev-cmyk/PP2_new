#A lambda function is a small anonymous function.
x = lambda a : a + 10
print(x(5))

#Lambda functions can take any number of arguments:
x = lambda a, b : a * b
print(x(5, 6))

#Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))

#Or, use the same function definition to make a function that always triples the number you send in
def myfunc(b):
    return lambda a : a * b
mytripler=myfunc(3)
print(mytripler(11))

#Or, use the same function definition to make both functions, in the same program:
def myfunc(n):
    return lambda a:a*n
myd=myfunc(2)
myt=myfunc(3)
print(myd(11))
print(myt(11))

#The map() function applies a function to every item in an iterable:
numbers=[1,2,3,4,5]
doubled=list(map(lambda x:x*2,numbers))
print(doubled)

#The filter() function creates a list of items for which a function returns True:
numbers=[1,2,3,4,5,6,7,8]
odd=list(filter(lambda x:x%2!=0,numbers))
print(odd)

#The sorted() function can use a lambda as a key for custom sorting:
students=[("Emil",25),("Tobias",22),("Linus",28)]
sortedd=sorted(students,key=lambda x:x[1])
print(sortedd)
