#!/usr/bin/env python
# coding: utf-8

# In[ ]:


---HOMEWORK 3----

#Name: Ayşegül
#Surname: Hülagü
#mail: hulaguaysegul@gmail.com


# In[123]:


def prime_numbers(lower,upper):
        
    
    for i in range(lower,upper+1):
            for num in range(2,i):
                if(i%num)==0:
                    break
            else:
                print (i)
            


# In[124]:


prime_numbers(2,100)

