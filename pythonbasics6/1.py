#1.File handing exercises
with open("practice_6/text.txt","w") as f:
    f.write("Www")
    f.write("Python")

with open("practice_6/text.txt","r") as f:
    print(f.read())

with open("practice_6/text.txt","a") as f:
    f.write("new line")

import shutil
import os
shutil.copy("practice_6/text.txt","practice_6/copy.txt")
if os.path.exists("practice_6/copy.txt"):
    os.remove("practice_6/copy.txt")

#2.Directory exercises
#import os
#os.mkdir("my_folder")
#print(os.listdir())
#print(os.getcwd())

import shutil
shutil.move("text.txt","my_folder/text.txt")

#3 Built-in functions
from functools import reduce
nums=[5,9,6,1]
print(list(map(lambda x: x**2,nums))) #map
print(list(filter(lambda x: x%2==0,nums))) #filter
print(reduce(lambda x,y: x+y,nums)) #reduce


names=["Aya","Za","Lina"]
nm=["12","13","14"]
for i,name in enumerate(names):
    print(i,name)
for n,num in zip(names,nm):
    print(n,nm)