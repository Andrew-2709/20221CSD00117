#!/usr/bin/env python
# coding: utf-8

# In[1]:


li=[]
for i in range(1,100,5):
    li.append(int(input()))
print(li)
print(li[-3:])


# In[6]:


li=[]
n=int(input("Enter the no of elements needed: "))
k=int(input("Enter the Start: "))
for i in range(0,n):
      li.append(k)
      k=k+5
print(li)
print(li[-3:])
print(li[17:21:1])


# In[2]:


import numpy as np
arr=np.arange(100)
print(arr)


# In[8]:


print(type(arr))


# In[9]:


print(arr.shape)


# In[10]:


print(arr.ndim)


# In[11]:


print(arr.size)


# In[23]:


b=np.array([[1,2],[3,4]])
print(b)


# In[24]:


c=np.ones((3,3))
print(c)


# In[ ]:


b=np.array([[1,2,6],[3,4,7],[9,]])
print(b)


# In[26]:


n=np.zeros((3,3))
print(n)


# In[28]:


m=np.eye((3))
print(m)


# In[29]:


s=np.ones((4,3,2))
print(s)


# In[31]:


v=np.diag([1,2,3])
print(v)


# In[32]:


e=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(e)
z=np.diag(e)
print(z)


# In[33]:


y=np.linspace(5,10,5)
print(y)


# In[34]:


o=np.linspace(5,12,5)
print(o)


# In[37]:


u=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(u)
print(u[1,1])
print(u[2,2])


# In[47]:


w=np.arange(1,11)
w[4:10]=10
print(w)


# In[51]:


li=[1,2,3,4,5,6,7,8,9,10]
for i in range(4,10,1):
    li[i]=10
print(li)


# In[52]:


li=[1,2,3,4,5,6,7,8,9,10]
a=np.array(li)
a[5:]=10
print(a)

