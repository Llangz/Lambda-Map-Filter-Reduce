#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Lambda functions are also called Anonymous function


# In[ ]:


#lambda, arguments: expression(only one), Lambda is used hwen we need a function for a short period of time


# In[1]:


for i in range(1,11):
    if i%2==0:
        print(i)


# In[ ]:


#Filter


# In[4]:


list(filter(lambda i:i%2==0, range(1,11)))


# In[5]:


tuple(filter(lambda i:i%2==0, range(1,11)))


# In[ ]:





# In[ ]:


#Reduce is used for computation of(add,multiply) items in a list/tuple. It reduces them to a single element


# In[6]:


import functools


# In[8]:


a = [1,3,5,7,9]
functools.reduce(lambda x,y: x + y, a)


# In[9]:


b = [2,4,6,8,0]
functools.reduce(lambda x, y: x * y, b)


# In[ ]:


#Map functions. Map(function, sequence)


# In[15]:


c = [1,2,3,4,5]
def square(x):
    return x*x
map(square, c)


# In[16]:


list(map(lambda x: x*x,c))


# In[17]:


d = [1,3,5,7,9]
e = [2,4,6,8,10]
list(map(lambda x, y: x*y, d, e))


# In[ ]:




