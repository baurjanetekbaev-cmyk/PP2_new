#return an iterator from a tuple ,and print each value
mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

#Strings are also iterable objects, containing a sequence of characters
mystr="banana"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#We can also use a for loop to iterate through an iterable object:
myt=("apple","banana","cherry")
for x in myt:
    print (x)

#iterate the characters of a string:
myself="banana"
for x in myself:
    print(x)

#CREATE AN ITERATOR
#To create an object/class as an iterator you have to implement the methods __iter
#As you will learn in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
#The __next__() method also allows you to do operations, and must return the next item in the sequence.
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#STOPITERATION
class MyNumbers:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)
for x in myiter:
    print(x)

#Create a tuple
mytuple=("apple","banana","cherry")
myit=iter(mytuple)
print(next(myit))

 #PYTHON GENERATIONS
def my_generator():
    yield 1
    yield 2
    yield 3
for i in my_generator():
    print(i)

#Generator that yields numbers:
def count_up(n):
    count=1
    while count <=n:
        yield count
        count +=1
for n in count_up(5):
    print(n)

#Generator for large sequence(n):
def  large(n):
    for i in range(n):
        yield i
#This doesnot create a million numbers in memory
gen=large(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

#Using next()
def simple():
    yield "Emil"
    yield "Tobias"
    yield "Linus"
gen = simple()
print(next(gen))
print(next(gen))
print(next(gen))

#GENERATOR EXPRESSIONS 
lisd=[x * x for x in range(5)]
print(lisd)
gen_e=(x*x for x in range(5))
print(gen_e)
print(list(gen_e))

#Using a generator expression with sum
total=sum(x*x for x in range(10))
print(total)

#Generate 100 Fibonnacci numbers
def fibonacci():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
#get first 100 fibonacci numbers
gen=fibonacci()
for i in range(100):
    print(next(gen))

#send() method
def echo():
    while True:
        received=yield
        print("Received:",received)
gen=echo()
next(gen) #Prime the generator
gen.send("Hello")
gen.send("World")

#close() method
def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")
gen=my_gen()
print(next(gen))
gen.close()

#DATES
import datetime
x=datetime.datetime.now()
print(x)

#Return the year and name of weekday
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))

#Create a date object
import datetime
x=datetime.datetime(2020,5,17)
print(x)

#The strftime() method
import datetime
x=datetime.datetime(2018,6,1)
print(x.strftime("%B"))
#%a	Weekday, short version	Wed	
#%A	Weekday, full version	Wednesday	
#%w	Weekday as a number 0-6, 0 is Sunday	3	
#%d	Day of month 01-31	31	
#%b	Month name, short version	Dec	
#%B	Month name, full version	December	
#%m	Month as a number 01-12	12	
#%y	Year, short version, without century	18	
#%Y	Year, full version	2018	
#%H	Hour 00-23	17	
#%I	Hour 00-12	05	
#%p	AM/PM	PM	
#%M	Minute 00-59	41	
#%S	Second 00-59	08	
#%f	Microsecond 000000-999999	548513	
#%z	UTC offset	+0100	
#%Z	Timezone	CST	
#%j	Day number of year 001-366	365	
#%U	Week number of year, Sunday as the first day of week, 00-53	52	
#%W	Week number of year, Monday as the first day of week, 00-53	52	
#%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
#%C	Century	20	
#%x	Local version of date	12/31/18	
#%X	Local version of time	17:41:00	
#%%	A % character	%	
#%G	ISO 8601 year	2018	
#%u	ISO 8601 weekday (1-7)	1	
#%V	ISO 8601 weeknumber (01-53)	01

import datetime
x=datetime.datetime.now()
print(x.year)

#MATH
x=min(5,10,25)
y=max(5,10,25)
print(x)
print(y)

#The abs()
x=abs(-7.25)
print(x)
#The pow(x,y)
x=pow(4,3)
print(x)

#The Math Module
import math
x=math.sqrt(64)
print(x)

#The math.ceil()
import math
x=math.ceil(1.4)
y=math.floor(1.4)
print(x) #returns 2
print(y) #returns 1

#math.pi
import math
x=math.pi
print(x)

#JSON in Python
import json
x='{"name":"John","age":30,"city":"New York"}'
#parse x:
y=json.loads(x)
#the result is a Python dictionary:
print(y["age"])

import json
#a Python object (dict):
x={
    "name":"John",
    "age":30,
    "city":"New York"
}
#convert into JSON:
y=json.dumps(x)
#the result is a JSON string:
print(y)

#Convert a Python object containing all the legal data types
import json
x={
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("Ann","Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge","mpg":24.1}
    ]
}
print(json.dumps(x))

#IMPORT JSON
import json
x='{"name":"Emil","age":30}'
y=json.loads(x)
print(y["age"])