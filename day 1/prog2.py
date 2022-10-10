Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a='''golu ghda
    golu bhngi
    golu gdura'''
print(a)
golu ghda
    golu bhngi
    golu gdura
b= 'revenge'
print(b)
revenge
a='hello world'
print(a)
hello world
a[0]
'h'
a[5]
' '
a[6]
'w'
a[0,1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[0,1]
TypeError: string indices must be integers
a='hello world'
a[0:2]
'he'
a[3:5]
'lo'
a[-12:-10]
'h'
a[-7:-9]
''
a[-9:-7]
'll'
a[0:10:2]
'hlowr'
a[0:10:-1]
''
a[-1:-12:-1]
'dlrow olleh'
a[::-1]
'dlrow olleh'
a
'hello world'
a=a.capitalize()

a='hello world'
a=a.capitalize()
print(a)
Hello world
a.center(50)
'                   Hello world                    '
a.center(50,'#')
'###################Hello world####################'
a.count('l')
3
a.lstrip()
'Hello world'
a.rstrip()
'Hello world'
a=a.center()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a=a.center()
TypeError: center expected at least 1 argument, got 0
a=a.center(50)
a.lstrip()
'Hello world                    '
a.rstrip()
'                   Hello world'
a.upper()
'                   HELLO WORLD                    '
a.lower()
'                   hello world                    '
a.startwith('he')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.startwith('he')
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith('he')
False
b='akshat123@gmail.com'
b=b.split('@')
b
['akshat123', 'gmail.com']
'@'.join(b)
'akshat123@gmail.com'
#######################################################################

m=[12,'hi',2.3,500]
m[0]
12
m[1:3]
['hi', 2.3]
'hi' in m
True
'bye' in m
False
2*m
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
50*m
[12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500, 12, 'hi', 2.3, 500]
m+=['new val']
m
[12, 'hi', 2.3, 500, 'new val']
m.append('abc')
m
[12, 'hi', 2.3, 500, 'new val', 'abc']
m.append('x','y')
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    m.append('x','y')
TypeError: list.append() takes exactly one argument (2 given)
m.extend(['x','y'])
m
[12, 'hi', 2.3, 500, 'new val', 'abc', 'x', 'y']
m.insert('hello',2)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    m.insert('hello',2)
TypeError: 'str' object cannot be interpreted as an integer
m.insert(2,'insert')
m
[12, 'hi', 'insert', 2.3, 500, 'new val', 'abc', 'x', 'y']
m.pop()
'y'
mp=m.pop()
mp
'x'
m.clear()
m
[]
n=[1,2,3,4]
n.reverse()
n
[4, 3, 2, 1]
n.sort()
n
[1, 2, 3, 4]
max(n)
4
min(n)
1
m.index('3')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    m.index('3')
ValueError: '3' is not in list
n.index(3)
2
m=[12, 'hi', 2.3, 500, 'new val']
m[1][0]
'h'
###############################################################################

>>> 
>>> t=52,23,'abc'
>>> type(t)
<class 'tuple'>
>>> lent(t)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    lent(t)
NameError: name 'lent' is not defined. Did you mean: 'len'?
>>> len(t)
3
>>> t.index('abc')
2
>>> t[0]
52
>>> t[0:2]
(52, 23)
>>> t[0]=42
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    t[0]=42
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> k=(12,52,85,(4,'abc',5.5),100)
>>> type(k)
<class 'tuple'>
>>> k[3]
(4, 'abc', 5.5)
>>> k[3][1]
'abc'
>>> k[3][1][1]
'b'
>>> s={1,2,1,2,3,4,4}
>>> type(s)
<class 'set'>
>>> print(s)
{1, 2, 3, 4}
>>> s2={5,6,7,8}
>>> s.intersection(s2)
set()
>>> s2={3,5,4,6}
>>> s.intersection(s2)
{3, 4}
>>> s.union(s2)
{1, 2, 3, 4, 5, 6}
>>> s.add(100)
>>> s
{1, 2, 3, 100, 4}
