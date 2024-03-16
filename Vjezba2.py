#Ugrađene funkcije u Pythonu
#https://docs.python.org/3/library/functions.html

"""
abs(x)
Return the absolute value of a number. 
The argument may be an integer, a floating point number, or an object implementing __abs__(). 
If the argument is a complex number, its magnitude is returned.
"""

x=4+3j
print("x=",x,"=> |x|=",abs(x))
y=-56.45
print("y=",y,"=> |y|=",abs(y))

"""
bin(x)
Convert an integer number to a binary string prefixed with “0b”. 
The result is a valid Python expression. 
If x is not a Python int object, it has to define an __index__() method that returns an integer.
"""

print(bin(5))
print(bin(-9))

"""
bool(x=False)
Return a Boolean value, i.e. one of True or False. 
"""

print(bool(4<9))
print(bool(3==5))

"""
chr(i)
Return the string representing a character whose Unicode code point is the integer i. 
For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. 
This is the inverse of ord().
"""

print(chr(163))
print(ord("Č"))

"""
complex(real=0, imag=0)
class complex(string)
Return a complex number with the value real + imag*1j or convert a string or number to a complex number. 
"""

a=complex(real=7, imag=3)
print(a)
b=complex("4-5j")
print(b)

"""
divmod(a, b)
Take two (non-complex) numbers as arguments and return a pair of numbers consisting of 
their quotient and remainder when using integer division. 
With mixed operand types, the rules for binary arithmetic operators apply. 
For integers, the result is the same as (a // b, a % b). 
For floating point numbers the result is (q, a % b), where q is usually math.floor(a / b) but may be 1 less than that.
"""

print(divmod(7,4))
print(divmod(7.5,4))


"""
enumerate(iterable, start=0)
Return an enumerate object. iterable must be a sequence, an iterator, or some other object 
which supports iteration.
"""

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
L1=list(enumerate(seasons))
print(L1)
L2=list(enumerate(seasons, start=1))
print(L2)

"""
float(x=0.0)
Return a floating point number constructed from a number or string x.
"""

print(float('-3.643'))
print(float('1e-003'))
print(float('+1E6'))
print(float('-Infinity'))


"""
hex(x)
Convert an integer number to a lowercase hexadecimal string prefixed with “0x”. 
If x is not a Python int object, it has to define an __index__() method that returns an integer.
"""

print(hex(255))
print(hex(-42))

"""
id(object)
Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant 
for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.
CPython implementation detail: This is the address of the object in memory.
"""

"""
int(x=0)
int(x, base=10)
Return an integer object constructed from a number or string x, or return 0 if no arguments are given.
If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing 
an integer in radix base.
"""

print(int(134.21))
print(int("543"))


"""
isinstance(object, classinfo)
Return True if the object argument is an instance of the classinfo argument, 
or of a (direct, indirect, or virtual) subclass thereof. 
If object is not an object of the given type, the function always returns False. 
"""

m=3+2j
n=153
print(isinstance(m,complex))
print(isinstance(n,float))
print(isinstance(n,int))

"""
len(s)
Return the length (the number of items) of an object. 
The argument may be a sequence (such as a string, bytes, tuple, list, or range) 
or a collection (such as a dictionary, set, or frozen set).
"""

o = [1,2,3,4,5,6,7,8,9]
print(len(o))
