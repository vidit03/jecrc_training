Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def myfun():
    print('this is my  first function')
    myfun()
myfun()
SyntaxError: invalid syntax
myfun()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    myfun()
NameError: name 'myfun' is not defined
def myfun():
    print('thi is my first fun')

    

myfun()
thi is my first fun
a=myfun()
thi is my first fun
priint(a)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    priint(a)
NameError: name 'priint' is not defined. Did you mean: 'print'?
print(a)
None
def second():
    return 'w'

second()
'w'
b=second()
b
'w'
print(b)
w
w
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    w
NameError: name 'w' is not defined
def third(x):
    print('hello')
third(x)
SyntaxError: invalid syntax
third(a)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    third(a)
NameError: name 'third' is not defined
thrid('a')
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    thrid('a')
NameError: name 'thrid' is not defined
def third(x):
    print('hello')
third('x')
SyntaxError: invalid syntax
third('a')
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    third('a')
NameError: name 'third' is not defined
third('abc')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    third('abc')
NameError: name 'third' is not defined
def third(x):
    print('hello')

third('abc')
hello

def fourth(x):
    return x*10

fourth(5)
50
def fourth():
    print('hi')
    print('bye')
    print('golu')
    print('bhg jaye')
    return x*10

fourth(4)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    fourth(4)
TypeError: fourth() takes 0 positional arguments but 1 was given
def fourth(x):
    print('hi')
    print('bye')
    print('golu')
    print('bhg jaye')
    return x*10

fourth(10)
hi
bye
golu
bhg jaye
100

def fourth(x):
    print('hii')
    return x**2
    print('hello')
    print('world')

    
fourth(9)
hii
81
def five(x,y,z):
    return x+y+z
five(10,20,30)
SyntaxError: invalid syntax
def five(x,y,z):
    return x+y+z
five(10,20,30)
SyntaxError: invalid syntax
def five(x,y,z):
    return x+y+z

five(1,3,2)
6
five(9,77,65)
151
five(9,77,65)
151
def five(x,y,z):
    return x+y+z,x*y*z,(x+y)/z

five(2,3,4)
(9, 24, 1.25)
def five(x=2,y=3,z=4):
    return x+y+z,x*y*z,(x+y)/z

def five(x,y,z):
    return x+y+z,x*y*z,(x+y)/z

five(x=2,y=3,z=4)
(9, 24, 1.25)
def seven(x,y,z=1)
SyntaxError: expected ':'
def seven(x,y,z=1):
    return x+y+z

seven(4,5,6)
15
seven(4,5)
10
def seven(x=2,y,z=1):
    return x+y+z
SyntaxError: non-default argument follows default argument
def seven(x,y=2,z):
    return x+y+z
SyntaxError: non-default argument follows default argument
def eight(*x):
    return x

eight()
()
eight(2)
(2,)
eight(2,3,4)
(2, 3, 4)
def nine(**x):
    return x

nine(name='popu',email='popupapa@gmail.com')
{'name': 'popu', 'email': 'popupapa@gmail.com'}
nine(n1=0,)
{'n1': 0}
def hbd(x):
    return 'happy birthday {x}'

hbd(golu)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    hbd(golu)
NameError: name 'golu' is not defined
def hbd(x):
    return 'happy birthday x'

hbd(golu)
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    hbd(golu)
NameError: name 'golu' is not defined
def hbd('x'):
    return 'happy birthday x'
SyntaxError: invalid syntax
def hbd(x):
    print('happy birthday')
  return x
SyntaxError: unindent does not match any outer indentation level
def hbd(x):
    print('happy birthday')
    return x

hbd(pasha)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    hbd(pasha)
NameError: name 'pasha' is not defined. Did you mean: 'hash'?
def hbd(x):
    print('happy birthday')
    return x

hbd('pasha')
happy birthday
'pasha'
'pasha'
'pasha'
def hbd(x):
    print('happy birthday to you')
    print('happy birthday to you')
    print(f'happy birthday dear{x}')
    print('happy birthday to you')

    
hbd('golu')
happy birthday to you
happy birthday to you
happy birthday deargolu
happy birthday to you
def hbd(x):
    print('happy birthday to you')
    print('happy birthday to you')
    print(f'happy birthday dear {x}')
    print('happy birthday to you')

    
hbd('golu')
happy birthday to you
happy birthday to you
happy birthday dear golu
happy birthday to you
myadd=lambda x,y,z:x+y+z
myadd(2,3,4)
9
import math
math.pi
3.141592653589793
math.sqrt(81)
9.0
math.pow(2,3)
8.0
math,factorial(5)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    math,factorial(5)
NameError: name 'factorial' is not defined
math.factorial(5)
120
import math as m
m.pi
3.141592653589793
from math import sqrt
sqrt(4)
2.0
import datetime as dt
aaj_ki_date=dt.date.today()
print(aaj_ki_date)
2022-09-19
import calender
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    import calender
ModuleNotFoundError: No module named 'calender'
import calendar
print(calendar.calendar(2022))
                                  2022

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6          1  2  3  4  5  6
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       7  8  9 10 11 12 13
10 11 12 13 14 15 16      14 15 16 17 18 19 20      14 15 16 17 18 19 20
17 18 19 20 21 22 23      21 22 23 24 25 26 27      21 22 23 24 25 26 27
24 25 26 27 28 29 30      28                        28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3                         1             1  2  3  4  5
 4  5  6  7  8  9 10       2  3  4  5  6  7  8       6  7  8  9 10 11 12
11 12 13 14 15 16 17       9 10 11 12 13 14 15      13 14 15 16 17 18 19
18 19 20 21 22 23 24      16 17 18 19 20 21 22      20 21 22 23 24 25 26
25 26 27 28 29 30         23 24 25 26 27 28 29      27 28 29 30
                          30 31

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
             1  2  3       1  2  3  4  5  6  7                1  2  3  4
 4  5  6  7  8  9 10       8  9 10 11 12 13 14       5  6  7  8  9 10 11
11 12 13 14 15 16 17      15 16 17 18 19 20 21      12 13 14 15 16 17 18
18 19 20 21 22 23 24      22 23 24 25 26 27 28      19 20 21 22 23 24 25
25 26 27 28 29 30 31      29 30 31                  26 27 28 29 30

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                1  2  3  4
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       5  6  7  8  9 10 11
10 11 12 13 14 15 16      14 15 16 17 18 19 20      12 13 14 15 16 17 18
17 18 19 20 21 22 23      21 22 23 24 25 26 27      19 20 21 22 23 24 25
24 25 26 27 28 29 30      28 29 30                  26 27 28 29 30 31
31

>>> print(calendar.month(2022,9))
   September 2022
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30

