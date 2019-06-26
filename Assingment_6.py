# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(nikhil2117)s
"""

#Case Study on mtcars dataset in Python	download data
#Download data
import pandas as pd
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars = dataset_mtcars.data

#structure

#summary
df = mtcars
df.head()

#print first / last few rows
df.head()
df.tail()
#print number of rows
df.shape[0]

#number of columns
df.shape[1]
#print names of columns
df.columns
#Filter Rows
#cars with cyl=8
df[df['cyl']==8]
#cars with mpg <= 27
df[df['mpg'] <= 27]
#rows match auto tx

#First Row
df[:1]
#last Row
df[-1:]
# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
df.iloc[[0,3,6,24], [0,5,6]]
# first 5 rows and 5th, 6th, 7th columns of data frame
df.iloc[:5,[4,5,6]]
#rows between 25 and 3rd last
df[26:-3]
df.iloc[[1],[1]]
#alternative rows and alternative column
for i in range(0,df.shape[0],2):
    print(df.iloc[i])
#find row with Mazda RX4 Wag and columns cyl, am
df[["cyl","am"]][df.index == "Mazda RX4 Wag"]
#find rows between Merc 280 and Volvo 142E  and columns cyl, am
mtcars.loc['Merc 280':'Volvo 142E',['cyl','am']]
# mpg > 23 or wt < 2
mtcars[(mtcars.mpg > 23) & (mtcars.wt < 2)]
#using lambda for above
mtcars.loc[lambda x: x['mpg'] > 23].loc[lambda x: x['wt'] < 2]

#with or condition
df[(df["mpg"]>23) | (df["wt"]<2)]
#find unique rows of cyl, am, gear
mtcars.loc[:,['cyl','am', 'gear']].drop_duplicates()
#create new columns: first make a copy of mtcars to mtcars2
dd = mtcars
#keeps other cols and divide displacement by 61
dd.disp = df.disp/61
dd
# multiple mpg * 1.5 and save as original column
dd.mpg= df["mpg"]*1.5
dd
