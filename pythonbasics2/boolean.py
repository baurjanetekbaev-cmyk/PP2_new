#in programming you often need to know if an expression is True or False
#when you compare two values ,the expression is evaluated and python returns the boolean answer:
print(10>9)
print(10==9)
print(10<9)


#when you run a conditional in an if statement,Python returns True or False:
#print a message based on weather the condition is True or False:
a=200
b=33
if b>a:
    print("b is greater than a")
else:
    print("b is not greater than a")


#the bool() function allows you to evaluate any value,and give you True or False in returns:
#evaluate a string and a number
print(bool("Hello"))
print(bool(15))


#evaluate two variables:
x="Hello"
y=15
print(bool(x))
print(bool(y))


#Almost any value is evaluaed to True if it has some sort of content
#Any string is True ,except empty strings
#Any number is True,except 0
#Any list,tuple,set ,and dictionary are True,except empty ones
print(bool("abc"))
print(bool(123))
print(bool(["apple","cherry","banana"]))


#in fact ,there are not many values that evaluate to False,except empty values,such as(),[],{},"",the number 0,and the value None.And of course the value False evaluates to False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


#One more value ,or object in this case,evaluates to False,and that is if you have an object that is made from a class with a _len_ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#you can create functions that retirns a boolean value:
def myFunction():
   return True 
print(myFunction())


#you can execute code based on the Boolean answer of a function
def myFunction():
   return True
if myFunction():
   print("YES!")
else:
   print("NO!")


#isinstance() function,which can be used to determine if an object is of a certain data type:
x=200
print(isinstance(x,int))
