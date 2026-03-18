#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exists

f = open("demofile.txt")

with open("demofile.txt") as f:
  print(f.read(5))

with open("demofile.txt") as f:
  print(f.readline())

with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())

with open("demofile.txt") as f:
  for x in f:
    print(x)

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")
with open("demofile.txt") as f:
  print(f.read())

import os
os.remove("demofile.txt")

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")
