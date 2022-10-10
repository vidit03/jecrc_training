Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d1={'name':['akash','akshat','sunny'],'age':[25,20,22],}
type(d1)
<class 'dict'>
len(del)
SyntaxError: invalid syntax
len(d1)
2
d1[0]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    d1[0]
KeyError: 0
d1['name']
['akash', 'akshat', 'sunny']
d1['age']
[25, 20, 22]
d1
{'name': ['akash', 'akshat', 'sunny'], 'age': [25, 20, 22]}
d1.keys()
dict_keys(['name', 'age'])
d1.values()
dict_values([['akash', 'akshat', 'sunny'], [25, 20, 22]])
d1.items()
dict_items([('name', ['akash', 'akshat', 'sunny']), ('age', [25, 20, 22])])
d1['ph_no']=[647889,748993329,784387477]
d1
{'name': ['akash', 'akshat', 'sunny'], 'age': [25, 20, 22], 'ph_no': [647889, 748993329, 784387477]}
d1['name'][0]
'akash'
d1['name'][0][::-1]
'hsaka'
d1['name'][0]=['pasha']
print(d1)
{'name': [['pasha'], 'akshat', 'sunny'], 'age': [25, 20, 22], 'ph_no': [647889, 748993329, 784387477]}
d1['name'][0]='pasha'
d1
{'name': ['pasha', 'akshat', 'sunny'], 'age': [25, 20, 22], 'ph_no': [647889, 748993329, 784387477]}
del d1['ph_on']
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    del d1['ph_on']
KeyError: 'ph_on'
del d1['ph_no']
d1
{'name': ['pasha', 'akshat', 'sunny'], 'age': [25, 20, 22]}
d1.get('email')
d1.get('name')
['pasha', 'akshat', 'sunny']
a=20
b='ml'
print(a,b)
20 ml
print(a,b,sep='          ')
20          ml
print(a,b,sep='@')
20@ml

=========== RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py ===========
20####ML
a=input('Enter your name:')
Enter your name:pasha
a
'pasha'

========= RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py =========
20####ML
enetr the 1st number:-2
enter the 2nd number:-3
5

========= RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py =========
20####ML
enetr the 1st number:-1
enter the 2nd number:-2
3
enter the age:-12
a gift

========= RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py =========
20####ML
enetr the 1st number:-1
enter the 2nd number:-2
3
enter the age:-20
A GIFT
a task

========= RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py =========
20####ML
enetr the 1st number:-1
enter the 2nd number:-2
3
enter the age:-20
A GIFT
a task

========= RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py =========
20####ML
enetr the 1st number:-1
enter the 2nd number:-2
3
enter the age:-40
koi gift nahi hai

========= RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py =========
20####ML
enetr the 1st number:-1
enter the 2nd number:-2
3
enter the age:-14
a gift
>>> 
========= RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py =========
20####ML
enetr the 1st number:-1
enter the 2nd number:-1
2
enter the age:-2
a gift
what day is today:-saturday
Traceback (most recent call last):
  File "C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py", line 21, in <module>
    today = int(input('what day is today:-'))
ValueError: invalid literal for int() with base 10: 'saturday'
>>> 
========= RESTART: C:/Users/vidit/OneDrive/Desktop/ML-training/day 1/prog1.py =========
enter the 1st number:-2
enter the 2nd number:-3
enter the 3rd number:-1
b is the greatest
