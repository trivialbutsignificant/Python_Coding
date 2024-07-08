#!/usr/bin/env python
# coding: utf-8

# In[11]:


#Finding significant digits
n=input("Enter the number: ")
l=len(n)
j=0
k=0
for i in range(l):
    if n[i]=='.':
        j=1
    if n[i]=='0' or n[i]=='.':
        k+=1
if n[0]=='0' and l==1:
    print("There are",0,"significant digits.")
elif k==l and n[0]=='0' and n[1]=='.':
    print("There are",0,"significant digits.")
elif n[0]=='0' and n[1]=='.':
    for i in range(2,l):
        if n[i]!='0':
            break
    print("There are",l-i,"significant digits.")
elif n[0]!='0' and j!=0 :
    print("There are",l-1,"significant digits.")
elif n[0]!='0' and j==0:
    for i in range(l):
        if n[l-i-1]!='0':
            break
    print("There are",l-i,"significant digits.") 
else:
    print("Number is invalid!")


# In[ ]:




