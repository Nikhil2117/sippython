# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(nikhil2117)s
"""

import pandas as pd
import numpy as np

df = pd.read_csv('data/denco.csv')
pd.set_option('display.max_columns',15)

#most_loyal_customers 
##by pandas way
df.custname.value_counts()#value_count is used to return the  most frequently-occurring element.
df.custname.value_counts().sort_values(ascending=False).head(5)

#by numpy
df.groupby('custname').size().sort_values(ascending=False).head(5)


#customers with most revenue
df.groupby('custname')['revenue'].sum().sort_values(ascending= False).head()
#sir's way

df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue', ascending=False).head(5)
#these are top parts which give max revenue 
df.groupby('partnum')['revenue'].sum().sort_values(ascending= False).head()
#sir's Way
df[['partnum','revenue']].groupby('partnum').sum().sort_values(by='revenue', ascending=False).head(5)

#these are top parts which give max margins
#if total sales has to be considered
dd= df.groupby('partnum')['margin'].sum().sort_values(ascending= False).head()
#sir's Way
df[['partnum','margin']].groupby('partnum').sum().sort_values(by='margin', ascending=False).head(5)

df.groupby('partnum').size().sort_values(ascending=False).head()

dg = df[['revenue','region']].groupby('region').sum()
type(dg)
type(dd)
