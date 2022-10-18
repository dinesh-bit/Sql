#!/usr/bin/env python
# coding: utf-8

# **List**

# Mutable, Sequential data

# In[1]:


a=[1,2,3,'dog','cat',True]
a


# In[2]:


len(a) #length of the list


# In[3]:


a.append(4)
a   #adding new element to the list


# In[4]:


len(a)


# In[5]:


a.insert(-1,'mice')
a  #inserting element with their position


# In[6]:


a[4]


# In[7]:


a[1:5]#range of values


# In[8]:


a[-1]


# In[9]:


a


# In[10]:


a.pop() #removes the last element


# In[48]:


a


# In[30]:


a.index('mice') #returns the index of the element


# In[12]:


for i in a:
    print(i)


# In[9]:


b=['bat','ant','zoo','cat']
# b.sort()
# b
c=sorted(b)  #Returns the sorted values in the new list
c    


# In[13]:


d='- '.join(b)
print(d)


# In[15]:


h=d.split('-')
print(h)


# In[16]:


h[1]


# In[17]:


h[1]='leo' #Muttable


# In[18]:


print(h)


# **Tuple**

# immutable

# In[19]:


zoo=('lion','tiger','fox','hippo')
zoo


# In[20]:


zoo[1]


# In[59]:


zoo[:-1]


# In[ ]:


# zoo.pop()     #immutable
# zoo.append()
# zoo.remove()
# zoo[1]='cub'


# In[56]:


for i in zoo:
    print(i)


# **Dictionary**

# key value pairs, key is unique id, value is data

# In[23]:


emp={'id':325,'Name':'Ethan','Post':'intern','Skill':['adaptive','team_player']}
emp


# In[99]:


emp['Skill']


# In[103]:


emp.get('Skill')


# In[104]:


print(emp.get('exp'))


# In[106]:


print(emp.get('exp','NAN'))


# In[111]:


emp['mail']='asd@mail.com' #adding new key
emp


# In[28]:


emp['Name']='loki'  #replacing value
emp


# In[113]:


emp.update({'id':345,'Name':'joy'})
emp


# In[29]:


del emp['id']


# In[30]:


emp


# In[128]:


len(emp)


# In[129]:


emp.keys()


# In[130]:


emp.values()


# In[131]:


emp.items()


# In[134]:


for i,k in emp.items():
    print(i,k) 


# **Sets**

# unordered collection of value, No duplicates

# In[72]:


zoo={'lion','tiger','fox','hippo'}
zoo


# In[73]:


zoo={'lion','tiger','fox','hippo','fox'} #Don't allow Duplicates
zoo


# In[32]:


print('tiger' in zoo)


# In[90]:


pet={'hippo','dog','pig','lion'}
pet


# In[84]:


zoo.intersection(pet)  #Common values


# In[86]:


zoo.difference(pet)  #Different values


# In[89]:


zoo.union(pet)  #Combine all values


# In[92]:


for i in pet:
    print(i)


# In[1]:


p={1,2,3,4}
p.add(6)
p

