#1.1) Running instructions in Interactive interpreter and a Python Scrip
#Interactive interpreter
>>> a=10
>>> print(a)
10
>>> type(a)
<class 'int'>
>>> a=15
>>> b=24
>>> c=a+b
>>> print(c)
39
>>> s='hello'
>>> type(s)
<class 'str'>
>>> len(s)
5
>>> 
#python script to reverse a given number
n=int(input('enter the number'))
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
print('reversed number=',rev)
#output
enter the number123456
reversed number= 654321
