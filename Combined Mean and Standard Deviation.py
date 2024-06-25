#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Program to find combined Mean and combined Standard Deviation
import math
dt=int(input("Enter the number of datasets: "))
nt=0
xt=0
sigt=0
d=[]
n=[]
x=[]
sd=[]
for i in range(dt):
    n.append(int(input(f'Enter the elemets of {i+1} dataset: ')))
    x.append(int(input(f'Enter the {i+1} Mean: ')))
    sd.append(int(input(f'Enter the {i+1} Standard Deviation: ')))
    nt=nt+n[i]
    xt=xt+n[i]*x[i]
xt=float(xt/nt)
for j in range(dt):
    d.append(x[j]-xt)
    sigt=sigt+n[j]*(sd[j]**2+d[j]**2)
sigt=float(sigt/nt)
sdt=float(sigt**0.5)
print("The combined Mean is ",xt,"and combined Standard Deviation is ",sdt)


# # 
