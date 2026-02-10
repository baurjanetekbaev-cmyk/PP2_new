def my_function(): #To call a function
    print("Hello from a function")
my_function()

#With functions - repetitive code:
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32)*5/9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

#A function that returns a value:
def get():
    return "Hello from a function"
mes=get()
print(mes)

#A function with one argument:
def myfunc(f):
    print(f+" Refsnes")
myfunc("Emil")
myfunc("Tobias")
myfunc("Linus")

#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the actual value that is sent to the function when it is called.
def myfunc(name): #name is a parametr
    print("Hello", name)
myfunc("Ayala") #"Ayala" is an argument

#This function expects 2 arguments, and gets 2 arguments::
def myf(fname,lname):
    print(fname+ " " +lname)
myf("Ayala","Shaisultan")

#Default Parameter Values
def myfu(name = "friend"):
    print("Hello",name)
myfu("Emil")
myfu("Tobias")
myfu()
myfu("Linus")

#You can send arguments with the key = value syntax.
def my_f(animal,name):
    print("I have a",animal)
    print("My",animal + "s name is", name)
my_f(animal="dog",name="Buddy")

#When you call a function with arguments without using keywords, they are called positional arguments.
#Positional arguments must be in the correct order:
def my_fu(animal,name):
    print("I have a",animal)
    print("My",animal + "s name is",name)
my_fu("dog","buddy")

#You can send any data type as an argument to a function (string, number, list, dictionary, etc.).
def my_func(fruits):
    for fruit in fruits:
        print(fruit)
my_fr=["apple","banana","cherry"]
my_func(my_fr)

#Sending a dictionary as an argument:
def my_funct(person):
    print("Name",person["name"])
    print("Age",person["age"])
my_person={"name":"Emil","age":"25"}
my_funct(my_person)

#Functions can return values using the return statemen
def my_function(x,y):
    return x+y

result = my_function(5,3)
print(result)

#A function that returns a list:
def my_ff():
    return ["apple","banana","cherry"]
fruits=my_ff()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def myff():
    return(10,20)
x,y=myff()
print("x:",x)
print("y:",y)

#Positional-Only Arguments
def muf(name,/):
    print("Hello",name)
muf("Emil") #We cannot write name="emil" in breaket

#Keyword-Only Arguments
def myf1(*,name):
    print("Hello",name)
myf1(name="Emil") #We can not write just "Emil"

#Arguments before / are positional-only, and arguments after * are keyword-only:
def myf2(a,b,/,*,c,d):
    return a+b+c+d
result=myf2(5,10,c=15,d=20)
print(result)

#Arbitrary Arguments - *args
def mf(*kids):
    print("The youngest child is" + kids[2])
mf("Emil","Tobias","Linus")

#The *args parameter allows a function to accept any number of positional arguments
#Inside the function, args becomes a tuple containing all the passed arguments:
def mm(*args):
    print("Type:",type(args))
    print("First argument:",args[0])
    print("Second argument:",args[1])
    print("All arguments",args)
mm("Emil","Tobias","Linus")

#Using *args with Regular Arguments
def mmu(greeting,*names):
    for name in names:
        print(greeting,name)
mmu("Hello","Emil","Tobi","Linus")

#Practical Example with *args
def mf(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total
print(mf(1,2,3))
print(mf(10,20,30,40))
print(mf(5))

#Finding the maximum value:
def mmf(*numbers):
    if len(numbers)==0:
        return None
    max_num=numbers[0]
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num
print(mmf(3,7,2,9,1))

#Arbitrary Keyword Arguments - **kwargs
def mmy(**kid):
    print("His last name is "+kid["lname"])
mmy(fname="Tobias",lname="Refsnes")

#Inside the function, kwargs becomes a dictionary containing all the keyword arguments
def m1(**myvar):
    print("Type:",type(myvar))
    print("Name:",myvar["name"])
    print("Age:",myvar["age"])
    print("All data:",myvar)
m1(name="Tobias",age=30,city="Bergen")

#Combining *args and **kwargs
def mfu(title,*args,**kwargs):
    print("Title:",title)
    print("Positional arguments:",args)
    print("Keyword arguments:",kwargs)
mfu("User Info","Emil","Tobias",age=25,city="Oslo")

#Unpacking Arguments
def fum(a,b,c):
    return a+b+c
numbers=[1,2,3]
result=fum(*numbers) #Same as: fum(1,2,3)
print(result)

#Unpacking Dictionaries with **
def myf(fname,lname):
    print("Hello",fname,lname)
person={"fname":"Emil","lname":"Refsnes"}
myf(**person) #Same as: myf(fname="Emil",lname="Refsnes")

#A variable created inside a function is available inside that function:
def myfuns():
    x=300
    print(x)
myfuns()

#Function Inside Function
def hfun():
    x=300
    def fin():
        print(x)
    fin()
hfun()

#Global Scope
x=300
def myf():
    print(x)
myf()
print(x)

#The function will print the local x, and then the code will print the global x
x=300
def func():
    x=200
    print(x)
func()
print(x)

#If you use the global keyword, the variable belongs to the global scope
def ff():
    global x
    x=300
ff()
print(x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x=300
def df():
    global x
    x=200
df()
print(x)

#If you use the nonlocal keyword, the variable will belong to the outer function
def myf1():
    x="Jane"
    def myf2():
        nonlocal x
        x="hello"
    myf2()
    return x
print(myf1())

#The LEGB Rule
#Local - Inside the current function
#Enclosing - Inside enclosing functions (from inner to outer)
#Global - At the top level of the module
#Built-in - In Python's built-in namespace
x="global"
def outer():
    x="enclosing"
    def inner():
        x="local"
        print("Inner:",x)
    inner()
    print("Outer:",x)
outer()
print("Global:",x)

#Basic Decorator
#Define the decorator first, then apply it with @decorator_name above the function.
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Hello Sally"
print(myfunction())

#By placing @changecase directly above the function definition, the function myfunction is being "decorated" with the changecase function.
#The function changecase is the decorator.

#The expression is executed and the result is returned:
x=lambda a: a+10
print(x(5))

#Multiply argument a with argument b and return the result:
x=lambda a,b:a*b
print(x(5,6))

#Use that function definition to make a function that always doubles the number you send in:
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))

#The map() function applies a function to every item in an iterable:
numbers=[1,2,3,4,5]
doubled=list(map(lambda x :x*2,numbers))
print(doubled)

#A simple recursive function that counts down from 5:
def countdoown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdoown(n-1)
countdoown(5)

#Identifying base case and recursive case:
def factorial(n):
    #Base case
    if n==0 or n==1:
        return 1
    #Recursive case
    else:
        return n*factorial(n-1)
print(factorial(5))

#Find the 7th number in the Fibonacci sequence
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(7))

#A simple generator function:
def my_generator():
    yield 1
    yield 2
    yield 3
for valuee in my_generator():
    print(valuee)


