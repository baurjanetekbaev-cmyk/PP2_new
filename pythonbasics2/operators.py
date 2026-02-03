#In the example below, we use the + operator to add together two values:
print(10+5)


#Although the + operator is often used to add together two values, like in the example above, it can also be used to add together a variable and a value, or two variables:
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)





# + addition 
# - subtraction 
# * multiplication 
# / division
# % modulus
# ** exponentiation
# // floor division


#Here is an example using different arithmetic operators:
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


#Python has two division operators:
#/ - Division (returns a float)
#// - Floor division (returns an integer)
x = 12
y = 5
print(x / y)


#Floor division always returns an integer.
# It rounds down to the nearest integer:
x = 12
y = 5
print(x // y)





# = x=5     # *= x*=5   # //= x//=3
# += x+=5   # /= x/=5   # **= x**=5
# -= x-=5   # %= x%=5   # & x&=5
# |= x|=5   # ^= x^=5   # >>= x>>=5
# <<= x<<=5 # := print(x:=5)


#Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger expression:
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3:
    print(f"List has {count} elements")





# == equal   # != not equal
# > greater than  # < less than
# >= greater than or equal to
# <= less than or equal to


#Comparison operators return True or False based on the comparison:
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
 

#Python allows you to chain comparison operators:
x = 5
print(1 < x < 10)
print(1 < x and x < 10)






# and-Returns True if both statements are true
# or-Returns True if one of the statements id true
# not-Reverse the result,returns False if the result is true


#Test if a number is greater than 0 and less than 10:
x = 5
print(x > 0 and x < 10)


#Test if a number is less than 5 or greater than 10:
x = 5
print(x < 5 or x > 10)


#Reverse the result with not:
x = 5
print(not(x > 3 and x < 10))





# is - Returns True if both variables are the same object
# is not - Returns True if both variables are not the same object


#The is operator returns True if both variables point to the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)


#The is not operator returns True if both variables do not point to the same objec
x = ["apple", "banana"]
y = ["apple", "banana"]
print(x is not y)


# is - Check if both variables point to the same object in memory
# == - Check if the values of both variables are equal
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)




# in - Returns True if a sequence with the specified value is present in the object
# not in - Returns True if a sequence with the specified value is not present in the object


#check if "banana" is present in a list
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)

#Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)

#The membership operators also work with strings
text="Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)




# $ AND - Sets each bit to 1 if both bits are 1
# | OR - Sets each bit to 1 if one of two bits is 1
# ^ XOR - Sets each bit to 1 if only one if two bits is 1
# ~ NOT - inverts all the bits
# << Zero fill left shift - Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >> Signed right shift - Shift right by pushinr copies of thr leftmost bit in from the left, and let the rightmost bits fall off


#The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:
print(6&3)
#the binary representation of 6 is 0110
#the binary representation of 3 is 0011
#then the & operator compares the bits and return 0010,which is 2 in decimal


#The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:
print(6|3)
#the binary representation of 6 is 0110
#the binary representation of 3 is 0011
#then the | operator compares the bits and returns 0111,which is 7 in decimal


#The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:
print(6^3)
#the binary representation of 6 is 0110
#the binary representation of 3 is 0011
#Then the ^ operator compares the bits and returns 0101,which is 5 in decimal


#Operator precedence describes the order in which operations are performed.
print((6+3)-(6+3))


#Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:
print(100+5*3)





# () Parentheses
# ** Exponentiation
# +x -x ~x Unary plus<unary minus,and bitwise NOT
# *  /  //  %	Multiplication, division, floor division, and modulus
# +  -	Addition and subtraction
# <<  >>	Bitwise left and right shifts
# &	Bitwise AND
# ^	Bitwise XOR
# |	Bitwise OR
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT
# and	AND
# or	OR


#Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right:
print(5+4-7+3)
