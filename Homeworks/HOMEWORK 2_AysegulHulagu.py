#!/usr/bin/env python
# coding: utf-8

# In[22]:


UserName=input("Please enter your username: ")
Password=input("Please enter your password: ")

for i in range(3):
    
    if UserName== "aysegul" and Password!= "deneme123":

        print("Invalid password")
        Password=input("Please re-enter your password: ")
    
        if Password== "deneme123":
            print("Connection is successful")
            break
       
        else:
            print("If you forgot the password,please change it: ")

    elif UserName=="aysegul" and Password=="deneme123":

             print("Connection is successful")
             break
    
    elif Password=="deneme123" and UserName!="aysegul":
            print("User name is wrong")
            UserName=input("Please re-enter your password")
            
            if UserName== "aysegul":
                print("Connection is successful")
                break
            
            else:
                print("If you forgot the username,please change it:")
            
    


# In[23]:


#-------EXTRA-------------


# In[31]:


user1= {"username": "aysegul","password":"deneme123"}

type(user1)


# In[35]:


#get username and password

kullanici_adi=input("Please enter your username: ")
sifre=input("Please enter your password: ")

for i in range(3):
    
    if kullanici_adi== user1["username"] and sifre!= user1["password"]:

        print("Invalid password")
        sifre=input("Please re-enter your password: ")
    
        if sifre== user1["password"]:
            print("Connection is successful")
            break
       
        else:
            print("If you forgot the password,please change it: ")

    elif kullanici_adi==user1["username"] and sifre==user1["password"]:

             print("Connection is successful")
             break
    
    elif sifre==user1["password"] and kullanici_adi!=user1["username"]:
            print("User name is wrong")
            kullanici_adi=input("Please re-enter your password")
            
            if kullanici_adi== user1["username"]:
                print("Connection is successful")
                break
            
            else:
                print("If you forgot the username,please change it:")
            

