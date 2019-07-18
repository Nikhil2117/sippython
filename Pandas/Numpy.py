# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(nikhil2117)s
"""
import numpy as np
np.linspace(10,15,9)

q= np.linspace(0,10,5)
np.round(q,2)
#fill 10 positions with empty values 0
xe=np.empty(10)  #almost 0
xe
#identity array
np.eye(4)  #identity matrix 
#all zeros
np.zeros([10,2])#zeroes values
#all ones
np.ones([12,5])
#all with particular value
np.full((3,4),["Nik"])
np.full((3,4), np.pi)


#changing shape
np.array([1,2,3,4])
np.array([1,2,3,4,5,6]).reshape(2,3)
x=np.array([1,2,3,4,5,6]).reshape(2,3)
x
y=x[:,np.newaxis]
y
y.shape
z=x[np.newaxis,:]
z
z.shape


x=np.array([1,2,3,4,5,6])
y=np.array([7,8,9])
x,y
np.concatenate([x,y]).tolist()
x = np.concatenate([x,np.zeros(5)])
x
xa = np.concatenate([x,np.zeros(3*4-x.size)])
xa



x=np.array([1,2,3])
y=np.array([4,5,6])
x,y
np.concatenate([x,y])
x=np.arange(6).reshape(2,3)
x
y=np.arange(10,16).reshape(2,3)
y
np.concatenate([x,y], axis=0)
np.concatenate([x,y], axis=1)
#vertical and horizontal stack
np.vstack([x,y])#row bind
np.hstack([x,y])#column bind


#split : break the array at particular position
x=np.arange(10,19)
x1,x2,x3 = np.split(x,[3,5])  #3rd, 5th : 3 subarrays
x1,x2,x3
x1,x2,x3 = np.split(x,3)  #3rd, 5th : 3 subarrays
x1,x2,x3
#split in multi dim array
y=x.reshape([3,3])
y
#upper and lower
upper, lower = np.vsplit(y,[2])
upper  #first 2 rows
lower # last row
#left and right : hsplit line : 1st col
left, right = np.hsplit(y,[2])
left
right

x=np.arange(5)
x
#using functions of np
np.add(x,5)  #add 5 to values
np.multiply(x,10)  #multiply values by 10

y=np.empty(5)
y  #almost zero
np.multiply(x,5, out=y )
y  #multiply x by 5 and save it in y





x=np.random.randint(10,100, size=(3,6))
x 
x.shape  #shape - 3 rows, 6 columns
np.shape(x)
np.size(x)   #how many values
x.sum()  #sum of the values
np.sum(x)
x.mean()  #mean of values
x.sum(axis=0)  #sum of the values : columns  : 6 columns
x.sum(axis=1)  # sum of row values : 3 rows 
x

x.min()
x.min(axis=1) #min in each row
x.max(axis=0) #min in each col
x
np.median(x)  #median values in full dataset
np.max(x)  #max
x.max()  #will not work, as it is multi
max([1,2,3])  #this will work
np.min(x) #min
x.min()
x.T
x.T.T
np.arange(1,13).reshape(3,4)
np.arange(1,13).reshape(3,4,order = "F")



x=np.random.randint(10,100, size=20)
x

np.equal(x, 49) #all values equal to 48
np.greater(x, 40) #values greater than 40
np.sum(np.greater(x,40))  #how many values > 40
sum(np.greater(x,40))
np.less(x, 50)  #values < 50
np.greater_equal(x, 40)  #values >= 40
x < 40 #another way T/ F
np.sum(x < 40)  #how many values < 40
x
np.sum(x < 40, axis=0)  #in each col, values < 40

x=np.random.randint(10, size=(3,4))
x
np.all(x > 4)
np.any(x > 4)
np.sum(x > 1)
np.sum(x > 3, axis=1)
np.sum(x > 3, axis=0)
np.sum( (x> 3) & (x < 7), axis=0)
np.sum( ~((x> 3) & (x < 7)), axis=0)


#sort
#%%
x = np.random.randint(100,size=50)
x
np.sort(x)
np.argsort(x)#return the index position of the sorted array

x = np.random.randint(10,size=15)
x
np.partition(x, [3])  #sorted till three numbers
np.partition(x, 4)  #sort till 4th numbers


x = np.array([30,49,50,60,49])
np.sum(np.equal(x,49))


np.sort(x)[::-1]
x[np.argsort(-x)]#descendiing sort in numpy!!!!

'''dual conditions
vice versa eqn.
'''