#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World!")


# In[2]:


print(3+9)


# In[4]:


import math
num=math.sqrt(25)
print(num)


# In[5]:


a=1
b=3
c=6
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)


# In[6]:


import cmath
a=4
c=3
b=1
d= (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)
print('The solution is',sol1,sol2)


# In[7]:


a=3
b=4
a,b=b,a
print('The number a:',a,'\n','The number b:',b)


# In[8]:


import random
print(random.randint(0,100))


# In[10]:


kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
print(miles)


# In[11]:


celsius = 37.5
fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)


# In[12]:


print("Python", end=" ")
print("is easy to learn.")


# In[ ]:




