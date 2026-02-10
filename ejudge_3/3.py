dict_l = {
    "ONE" : "1",
    "TWO" : "2",
    "THR" : "3",
    "FOU" : "4",
    "FIV" : "5",
    "SIX" : "6",
    "SEV" : "7",
    "EIG" : "8",
    "NIN" : "9",
    "ZER" : "0"}
dict_d = {
    "1" : "ONE",
    "2" : "TWO",
    "3" : "THR",
    "4" : "FOU",
    "5" : "FIV",
    "6" : "SIX",
    "7" : "SEV",
    "8" : "EIG",
    "9" : "NIN",
    "0" : "ZER"
} 

num=input()
if "+" in num:
    op="+"
elif "-" in num:
    op="-"
else:
    op="*"
left,right=num.split(op)
def letters_to_number(s):
    res=""
    for i in range(0,len(s),3):
        res+=dict_l[s[i:i+3]]
    return int(res)
a=letters_to_number(left)
b=letters_to_number(right)
if op=="+":
    result=a+b
elif op=="-":
    result=a-b
else:
    result=a*b
answer=""
for d in str(result):
    answer+=dict_d[d]
print(answer)