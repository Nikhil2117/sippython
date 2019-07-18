# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(nikhil2117)s
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x=np.linspace(0,10,100)
x
np.sin(x)
plt.plot(x,np.sin(x))
plt.xlim(-1,15)
plt.ylim(-1.5,1.5)
plt.plot(x,np.sin(x),color="orange")
#plt.show()
#%%%
x= np.arange(0,10)
x
y = x^2
#labelling the Axes and title
#run these 4 lines together 
plt.title("Graph Drawing")
plt.xlabel("Time")
plt.ylabel("Distance")
plt.plot(x,y,color="red")



plt.plot(x,np.sin(x))
plt.axis([-1,11,-2,2])

#multipe curve,singe line label
plt.plot(x,np.cos(x),label= "X Curve")
plt.plot(x,np.tan(x),label= "Y Curve")
plt.title("Sin and Cos curve")
plt.ylabel("Nikhil")
plt.xlabel("Chaudhary")
plt.legend()
x

plt.plot(x,np.sin(x))
plt.axis("tight")

plt.plot(x,np.sin(x))
plt.axis("equal")


x=np.linspace(0,10,1000)
ax=plt.axes()
ax.plot(x,np.sin(x),color="black")
ax.set(xlim=(0,10),ylim=(-2,2),xlabel="Xlabel",Ylabel="Ylabel",title="chal nikal")
#%%%%

df = pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
df
df.plot(kind="box",grid=True,notch=True)



plt.boxplot(df)
'''
Box plot
line plot
histogram
bar graph
scatter
'''