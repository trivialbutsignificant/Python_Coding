#!/usr/bin/env python
# coding: utf-8

# In[21]:


#Program to plot Ogive
import numpy as np
import matplotlib.pyplot as plt
data=str(input("Enter the data values: ")).split(', ')
classInterval =str(input("Enter the class intervals: ")).split(', ')

# calculating frequency and class interval
values, base = np.histogram(data, bins=classInterval)
 
# calculating cumulative sum
cumsum = np.cumsum(values)
 
# plotting  the ogive graph
plt.plot(base[1:], cumsum, color='red', marker='o', linestyle='-')
 
# formatting
plt.title('Ogive Graph')
plt.xlabel('Marks in End-Term')
plt.ylabel('Cumulative Frequency')


# In[ ]:





# In[ ]:




