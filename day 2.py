Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 'python'
b = 10
id(a)
2051406149360
id(b)
2051369468432
a='Machine learning'
print(a)
Machine learning
print(b)
10
print(a,b)
Machine learning 10
a='python'
b='10'
a*b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'str'
print(ab)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(ab)
NameError: name 'ab' is not defined. Did you mean: 'a'?
print(a,b)
python 10
import keyword
keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
len(keyword.kwlist)
35
a 1='python'
SyntaxError: invalid syntax
a_1='python'
print(a_1)
python
_ = 'python'
print(_)
python
"python"
'python'
a=20
b=30
a,b,c=20,30,40
print(a)
20
print(b)
30
print(c)
40
x=y=z=100
print(x)
100
print()z
SyntaxError: invalid syntax
print(z)
100

 







































1+2
3
1*2
2
1%2
1
1/2
0.5
1//2
0
1**2
1
2<3
True
2>3
False
2>=2
True
2<=3
True
2!=3
True
2==4
False
a=20
a+=50
print(a)
70
1<2 and 1>0
True
1<2 or 1>2
True
1<2 not 1>2
SyntaxError: invalid syntax
1>2 not 1>3
SyntaxError: invalid syntax
not 2
False
not 1
False
not not 1
True
1 in 2
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    1 in 2
TypeError: argument of type 'int' is not iterable
1 in
SyntaxError: invalid syntax
1 in 100
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    1 in 100
TypeError: argument of type 'int' is not iterable
i is odd
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    i is odd
NameError: name 'i' is not defined. Did you mean: 'id'?
>>> 1 1 is 2
SyntaxError: invalid syntax
>>> a is 1
False
>>> a=5
>>> type(a)
<class 'int'>
>>> b=4.5
>>> type(b)
<class 'float'>
>>> c=2+3j
>>> type(c)
<class 'complex'>
>>> print(type(c))
<class 'complex'>
>>> a_1='silent please'
>>> type(a_1)
<class 'str'>
>>> my_list = [1,1.1,'hi']
>>> type(my_list)
<class 'list'>
>>> my_tuple = [1,1.1]
>>> type(my_tuple)
<class 'list'>
>>> my_set = {1,22,34}
>>> type(my_set)
<class 'set'>
>>> c= 3+4j
>>> c.real
3.0
>>> c.imag
4.0
>>> bool(45)
True
>>> bool(-11)
True
>>> bool(none)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    bool(none)
NameError: name 'none' is not defined. Did you mean: 'None'?
>>> bool(None)
False
>>> bool(())
False
