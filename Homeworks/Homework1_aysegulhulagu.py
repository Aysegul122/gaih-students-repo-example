#!/usr/bin/env python
# coding: utf-8

# In[114]:


#--------QUESTION 1-------------

#creating list 

list1=[]

list1=list(range(1,8))

print(list1)
    


# In[115]:


#swapping the list

list1

length=len(list1)
print(length)

if len(list1) %2== 0:
    a=int(length/2)
    
    list1 = list1[a: ] + list1[ : a]

else:
    b=(length//2)
    
    list1 = list1[b+1: ] + list1[b:b+1] + list1[ : b]
    
print(list1)




# In[116]:


#--------QUESTION 2-------------


# In[180]:


number = int(input("Please enter a single digit integer number: "))


if number<0:
    print("Invalid number")
    number=int(input("Please enter postive number: "))
    number_stop=number+1
    for i in range(number_stop):
     if i %2==0:
      print(i)
    
else:
    number_stop=number+1
    for i in range(number_stop):
     if i %2==0:
      print(i)
    

