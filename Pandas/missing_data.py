# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(nikhil2117)s
"""

import pandas as pd
#import numpy as np

data  = {'names':["Rahul","Tanisha","Vijay","Hitesh","Priyanka"],'HR':[42,61,77,97,58],'MM':[48,59,53,62,90],'Stats':[96,88,90,86,79]}
df = pd.DataFrame(data,index=data['names'])
df.set_index('names',inplace=True)
df.drop('names',axis=1,inplace=True)
df
df.describe()
df.shape
df.dtypes
df
df.mean()
df.mean(axis=0)
df=df.reindex(['Arunabh',"Rahul",'Rakhi',"Tanisha",'Shreya',"Vijay",'Beenu',"Hitesh","Priyanka"])
df
df['HR'].mean()
df.isnull()
df.isna()
df.notnull()
df['HR'].isnull().sum()
df['MM'].isnull().sum()
df['Stats'].isnull().sum()

df.fillna(0)
df.replace(0,method='pad')
df.replace(0,method='backfill')
df.MM.sum()
df.fillna(method='pad')
df.dropna()
df.mean(axis=1)
df['HR'].mean()
meanMM= df['MM'].mean()
meanMM
df.fillna(meanMM,inplace=False)
df
df.mean()


#missing values implementation in the dataframe