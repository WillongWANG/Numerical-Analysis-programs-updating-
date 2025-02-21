#!/usr/bin/env python
# coding: utf-8

# In[19]:


import numpy as np

x=np.array([1,2,3,4,5,6,7,8]) #输入x向量,个数应为2的幂


def fft(x):
   w=complex(np.cos(-2*np.pi/x.shape[0]),np.sin(-2*np.pi/x.shape[0]))
   if x.shape[0]==1:
        return x
   else:
    a=np.zeros(0)
    for i in range(0,x.shape[0],2):
        a=np.append(a,[x[i]])
    u=fft(a)
    a=np.zeros(0)
    for i in range(1,x.shape[0],2):
        a=np.append(a,[x[i]])
    v=fft(a)
    
    y=np.zeros(0)
    for i in range(0,x.shape[0]//2):
        y=np.append(y,[u[i]+w**i*v[i]])
    for i in range(x.shape[0]//2,x.shape[0]):
        y=np.append(y,[u[i-x.shape[0]//2]+w**i*v[i-x.shape[0]//2]])
        
    return y


fft(x)


# In[20]:


np.fft.fft(a)






