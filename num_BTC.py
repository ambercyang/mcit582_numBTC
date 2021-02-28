#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[13]:


def num_BTC(b):
    # b is the block height
    N = 210000
    c = float(0)
    h = b/N


    for x in range(0, int(h)):
        for y in range (0,N):
            c = c + 50*0.5**x
          
    for z in range(0,b-int(h)*N):
        c = c + 50*0.5**int(h) 
        
    return c


# In[ ]:


num_BTC(500000000000)


# In[ ]:




