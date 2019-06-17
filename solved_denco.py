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

dg = df.groupby('custname').size(1)

