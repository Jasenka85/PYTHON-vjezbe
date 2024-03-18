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
class bool(x=False)
Return a Boolean value, i.e. one of True or False. 
"""

print(bool(4<9))
print(bool(3==5))

"""
chr(i)
Return the string representing a character whose Unicode code point is the integer i. 
For example, chr(97) returns the string 'a', while chr(8364) returns the string '€'. 
This is the inverse of ord().

ord(c)
Given a string representing one Unicode character, return an integer representing the Unicode code point 
of that character. For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. 
"""

print(chr(163))
print(ord("Č"))

"""
class complex(real=0, imag=0)
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
eval(expression, globals=None, locals=None)
The return value is the result of the evaluated expression.
The arguments are a string and optional globals and locals. 
If provided, globals must be a dictionary. 
If provided, locals can be any mapping object.
"""

p = 5
print(eval('p+3'))




"""
class float(x=0.0)
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
class int(x=0)
class int(x, base=10)
Return an integer object constructed from a number or string x, or return 0 if no arguments are given.
If x is not a number or if base is given, then x must be a string, bytes, or bytearray instance representing 
an integer in radix base.
"""

print(int(134.21))
print(int("543"))
print(int('120221', base=3))
print(int('2310423', base=5))


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

"""
class list
class list(iterable)
Rather than being a function, list is actually a mutable sequence type
"""

g="NIGHTSHADOW"
print(list(g))

#ne može napraviti listu od broja
#h=123456789
#print(list(h))



"""
map(function, iterable, *iterables)
Return an iterator that applies function to every item of iterable, yielding the results.
"""



"""
max(iterable, *, key=None)
max(iterable, *, default, key=None)
max(arg1, arg2, *args, key=None)
Return the largest item in an iterable or the largest of two or more arguments.
The key argument specifies a one-argument ordering function like that used for list.sort(). 
The default argument specifies an object to return if the provided iterable is empty. 
If the iterable is empty and default is not provided, a ValueError is raised.
If multiple items are maximal, the function returns the first one encountered. 
"""

w = {1,2,5,3,7,8,3,9,5,4}
print(max(w))

"""
min(iterable, *, key=None)
min(iterable, *, default, key=None)
min(arg1, arg2, *args, key=None)
Return the smallest item in an iterable or the smallest of two or more arguments.
"""

print(min(w))


"""
next(iterator)
next(iterator, default)
Retrieve the next item from the iterator by calling its __next__() method. 
If default is given, it is returned if the iterator is exhausted, otherwise StopIteration is raised.
"""

"""
oct(x)
Convert an integer number to an octal string prefixed with “0o”. 
"""

print(oct(8))
print(oct(-56))

"""
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
Open file and return a corresponding file object. If the file cannot be opened, an OSError is raised. 
See https://docs.python.org/3/tutorial/inputoutput.html#tut-files for more examples of how to use this function.
file is a path-like object giving the pathname (absolute or relative to the current working directory) 
of the file to be opened or an integer file descriptor of the file to be wrapped. 
(If a file descriptor is given, it is closed when the returned I/O object is closed unless closefd is set 
to False.)
mode is an optional string that specifies the mode in which the file is opened. 
It defaults to 'r' which means open for reading in text mode. 
Other common values are 'w' for writing (truncating the file if it already exists), 
'x' for exclusive creation, and 'a' for appending
"""

"""
pow(base, exp, mod=None)
Return base to the power exp; 
if mod is present, return base to the power exp, modulo mod 
(computed more efficiently than pow(base, exp) % mod). 
The two-argument form pow(base, exp) is equivalent to using the power operator: base**exp.
"""

print(pow(5,3))
print(5**3)

print(pow(2,-3))
print(2**(-3))

print(pow(25,0.5))
print(pow(-16,0.5))
print(pow(27,1/3))

#ovo je malo čudno
#print(pow(-32,1/5))

"""
print(*objects, sep=' ', end='\n', file=None, flush=False)
Print objects to the text stream file, separated by sep and followed by end. 
sep, end, file, and flush, if present, must be given as keyword arguments.
"""

"""
class property(fget=None, fset=None, fdel=None, doc=None)
Return a property attribute.
fget is a function for getting an attribute value. 
fset is a function for setting an attribute value. 
fdel is a function for deleting an attribute value. 
And doc creates a docstring for the attribute.

class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

  If c is an instance of C, 
  c.x will invoke the getter, 
  c.x = value will invoke the setter, 
  and del c.x the deleter.  

  A property object has getter, setter, and deleter methods usable as decorators that create a copy 
  of the property with the corresponding accessor function set to the decorated function. 
  
  class C:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        #I'm the 'x' property.
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

"""

"""
class range(stop)
class range(start, stop, step=1)
Rather than being a function, range is actually an immutable sequence type, 
as documented in Ranges and Sequence Types — list, tuple, range.
"""

"""
repr(object)
Return a string containing a printable representation of an object. 
A class can control what this function returns for its instances by defining a __repr__() method.

class Person:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def __repr__(self):
      return f"Person('{self.name}', {self.age})"
"""

"""
reversed(seq)
Return a reverse iterator. 
"""

y = [4,6,5,7,3,2,1,8,9]
z=list(reversed(y))
print(z)

"""
round(number, ndigits=None)
Return number rounded to ndigits precision after the decimal point. 
If ndigits is omitted or is None, it returns the nearest integer to its input.
"""

print(round(342143.231231))
print(round(-2313141.3213))
print(round(54323.234752, 3))
print(round(-5358.5352576,4))

"""
class set
class set(iterable)
Return a new set object, optionally with elements taken from iterable. set is a built-in class.
"""

u=['mačka','pas',123,-3.14]
print(set(u))



"""
setattr(object, name, value)
This is the counterpart of getattr(). 
The arguments are an object, a string, and an arbitrary value. 
The string may name an existing attribute or a new attribute. 
The function assigns the value to the attribute, provided the object allows it. 
For example, setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
"""

"""
class slice(stop)
class slice(start, stop, step=None)
Slice objects are also generated when extended indexing syntax is used. 
For example: a[start:stop:step] or a[start:stop, i]. 
"""

y = [1,2,3,4,5,6,7,8,9]
print(y)
print(y[2])
print(y[3:7])
print(y[5:])
print(y[0:9:2])




"""
sorted(iterable, /, *, key=None, reverse=False)
Return a new sorted list from the items in iterable.
"""

w = {5,7,3,4,6,8,9,11,2,10}
print(w)
print(sorted(w))
z=sorted(w, reverse=True)
print(z)
z.insert(3,1)
print(z)
print(sorted(z))


"""
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')
Return a str version of object. See str() for details.
"""

print(str(345.2413))
print(str(w))
print(str(z))


"""
sum(iterable, /, start=0)
Sums start and the items of an iterable from left to right and returns the total. 
The iterable’s items are normally numbers, and the start value is not allowed to be a string.
For some use cases, there are good alternatives to sum(). 
The preferred, fast way to concatenate a sequence of strings is by calling ''.join(sequence). 
To add floating point values with extended precision, see math.fsum(). 
To concatenate a series of iterables, consider using itertools.chain().
"""

print(sum(w))
print(sum(z,start=5))

seasons = ('Spring', 'Summer', 'Fall', 'Winter')
print(" ".join(seasons))

words = ["How","are","you","doing","?"]
print(' '.join(words))

"""
class tuple
class tuple(iterable)
Rather than being a function, tuple is actually an immutable sequence type
"""

print(tuple(words))

#ne može napraviti tuple od broja
#print(tuple(123142341))


"""
class type(object)
class type(name, bases, dict, **kwds)
With one argument, return the type of an object.
"""

a = 81
b= -241.54
c= 6-2j
d="Klokan"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

"""
zip(*iterables, strict=False)
Iterate over several iterables in parallel, producing tuples with an item from each one.
More formally: zip() returns an iterator of tuples, 
where the i-th tuple contains the i-th element from each of the argument iterables.
Another way to think of zip() is that it turns rows into columns, and columns into rows. 
This is similar to transposing a matrix.
By default, zip() stops when the shortest iterable is exhausted. 
It will ignore the remaining items in the longer iterables, 
cutting off the result to the length of the shortest iterable.
zip() is often used in cases where the iterables are assumed to be of equal length. 
In such cases, it’s recommended to use the strict=True option. 
"""

for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)

m=list(zip(range(3), ['fee', 'fi', 'fo', 'fum']))
print(m)

#Ako dodamo strict, dobit ćemo grešku:
#ValueError: zip() argument 2 is longer than argument 1
#for item in zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True):  
#    print(item)
