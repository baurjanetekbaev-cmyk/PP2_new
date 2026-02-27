#1
import json
def connection():
    str='''Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 '''
    print(str)
    with open("pythonbasics4/sample-data.json","r") as file:
        fromFile=json.load(file)
        array=fromFile["imdata"]
        for i in range(len(array)):
            tn =array[i]["l1PhysIf"]["attributes"]["dn"]
            description=array[i]["l1PhysIf"]["attributes"]["descr"]
            speed=array[i]["l1PhysIf"]["attributes"]["speed"]
            mtu=array[i]["l1PhysIf"]["attributes"]["mtu"]
            print(f"{tn}        {description}        {speed}        {mtu}")
        file.close()

connection()


#2 Python date
from datetime import date, timedelta
current = date.today()
ago = current - timedelta(days=5)
print("Current Date:", current)
print("Five days ago:",ago)


from datetime import date, timedelta
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)


import datetime
now = datetime.datetime.now()
ms = now.replace(microsecond=0)
print("With microseconds:", now)
print("Without microseconds:",ms)


from datetime import datetime
d1 = datetime(2024, 5, 20, 12, 0, 0)
d2 = datetime(2024, 5, 18, 10, 30, 0)
diff = d1 - d2
seconds_diff = diff.total_seconds()
print(f"The difference is {seconds_diff} seconds.")

#3 iterators and generators
def squ(n):
    for i in range(n + 1):
        yield i ** 2
n_val = int(input("Enter N: "))
for square in squ(n_val):
    print(square)


n = int(input("Enter n: "))
evens = (str(i) for i in range(0, n + 1) if i % 2 == 0)
print(",".join(evens))


def div(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
for num in div(50):
    print(num)


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
for val in squares(3, 7):
    print(val)


def c(n):
    while n >= 0:
        yield n
        n -= 1
for i in c(5):
    print(i)


#4 Math
import math
d=float(input("Input degree:"))
r=math.radians(d)
print(f"Output radian: {r}")


height = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
area = ((b1 + b2) / 2) * height
print(f"Expected Output: {area}")


import math
n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))
area = (n * s**2) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area:.0f}")


bas = float(input("Length of base: "))
hei = float(input("Height of parallelogram: "))
ar = bas * hei
print(f"Expected Output: {ar}")

