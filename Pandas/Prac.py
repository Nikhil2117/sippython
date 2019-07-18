# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(nikhil2117)s
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('E:\pyWork\pyProjects\sippython\data\\titanic_project.csv')
df.head()
df.shape
df.columns
pd.set_option('display.max_columns',15)
df.head()
df.info()
#Treating_with_NaN_in_the_Cabin

#z = df['cabin_number'].notna().sum()
#Filling NaN values with 0 in Cabin Number
df['cabin_number'].fillna(0,inplace=True)

#converting cabins into numerical values

df['CN'] = np.nan
df
df.head()
dollarizer = lambda x: (x[1:-1])
df.Cabin = df.Cabin.apply(dollarizer)

df['Cabin']
df['CN'] = df['Cabin']/df['Cabin']
#converting_sex into Numerical
df['Sex'].replace('male',0,inplace=True)
df['Sex']= df['Sex'].replace('female',1)
x = df[['Fare','Age','Sex','cabin_number','Pclass']]
x
x.isna().sum()
mode_age = df['Age'].mode()  
mode_age=int(mode_age)
x['Age'].fillna(mode_age,inplace = True)
x['cabin_number'].fillna(0,inplace = True)
y = df['Survived']


x = x.values
y = y.values

from sklearn.model_selection import train_test_split 

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.2, random_state = 0)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(random_state = 0)

model.fit(x_train, y_train)

model.score(x_test,y_test)

y_pred = model.predict(x_test)
y_pred.shape
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
cm

import statsmodels.api as sm
model = sm.OLS(y_train,x_train)
results = model.fit()
results.summary()



import sklearn.metrics as metrics
# calculate the fpr and tpr for all thresholds of the classification
probs = model.predict(x_test)
xxx= pd.DataFrame(probs)
preds = xxx
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)

# method I: plt

plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()