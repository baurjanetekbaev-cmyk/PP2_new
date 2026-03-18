#1
import re
with open("pythonbasics5/input.txt","r",encoding="utf-8") as file:
    f=len(file.readlines())
    for i in range(f):
        if re.search(r"аб*",file.readline()):
            print("FOUND!")
        else:
            print("NOT FOUND")

#2
import re
text = "abbbb ak ab er asd asd" 
m=re.findall(r"ab{2,3}",text)
print(m)

#3
import re
text=input()
m=re.findall(r'[A-Z][a-z]+',text)
print(m)

#5
import re
text=input()
if re.search(r'a.*b',text):
    print("Match")
else:
    print("No Match")

#6
import re
text=input()
result=re.sub(r'[ ,.]',':',text)
print(result)

#7
import re
s_str=input()
c_str=re.sub(r'_([a-z])',lambda x:x.group(1).upper(),s_str)
c_str=c_str.rstrip('_')
print(c_str)

#8
import re
s=input()
words=re.findall(r'[A-Z][a-z]*',s)
print(words)

#9
import re
s=input()
res=re.sub(r'(?<!^)([A-Z])',r' \1',s)
print(res)

#10
import re
c_str=input()
s_str=re.sub(r'([A-Z])',lambda x:'_'+x.group(1).lower(),c_str)
s_str=s_str.lstrip('_')
print(s_str)