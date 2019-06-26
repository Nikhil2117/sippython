# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(nikhil2117)s
"""

teamA = {'Rohit', 'Shikhar','Virat', 'Rahul'}
teamB = {'Dhoni', 'Kedar', 'Bhuvneshwar', 'Bumrah','Rohit','Rahul'}
type(teamA)

teamC= teamA.union(teamB)
print(teamC)
teamA.remove('Rohit')
teamC.pop()

teamC
teamD = ['India', 'Australia','Pakistan', 'England','Bangladesh','SA','New Zealand']

for i in range(0,len(teamD),2):
    print(teamA[i],end="    ")
    
for i in [0,4]:
    print(teamA[i],end="    ")


def printhello(name='Student'):
    print("Hello  "+name)
 
printhello()

y = "kaam kr na be"
def printHello3(name='Student'):
    print("Hello \t" + name)

printHello3()  #without value
printHello3('Dhiraj')
x=1
if x == 1: 
    print(x)
else:
    print("x not equal to 1")
    
x2 = lambda a, b, c : a + b + c
x2(1,2,3)

def func1(n):   return lambda a : a + n
func2 = func1(2)
func2(11)
