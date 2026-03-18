#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)

#1
f=open("pythonbasics6/demofile.txt")
print(f.read())

#2
with open("pythonbasics6/demofile.txt") as f:
    print(f.read())

#3 Close Files
f=open("pythonbasics6/demofile.txt")
print(f.readline())
f.close()

#4 Read Only Parts of the File
with open("pythonbasics6/demofile.txt") as f:
    print(f.read(5))

#5 Read Lines
with open("pythonbasics6/demofile.txt") as f:
    print(f.readline())

#6
with open("pythonbasics6/demofile.txt") as f:
    print(f.readline())
    print(f.readline())

#7
with open("pythonbasics6/demofile.txt") as f:
    for x in f:
        print(x)


#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content
with open("pythonbasics6/demofile.txt","a") as f:
    f.write("Now the file has moore content!")
with open("pythonbasics6/demofile.txt") as f:
    print(f.read())

#1
with open("pythonbasics6/demofile.txt","w") as f:
    f.write("Woops! I have deleted the content")
with open("pythonbasics6/demofile.txt") as f:
    print(f.read())

#"x" - Create - will create a file, returns an error if the file exists
#"a" - Append - will create a file if the specified file does not exists
#"w" - Write - will create a file if the specified file does not exists
f=open("pythonbasics6/myfile.txt","x")

#DELETE FILE


#2
import os
if os.path.exists("pythonbasics6/demofile.txt"):
    os.remove("pythonbasics6/demofile.txt")
else:
    print("The file does not exist")

