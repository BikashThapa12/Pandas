#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


dict1 = {
    
    "name":['bikash', 'harry', 'rohan'],
    "marks":[13, 15, 60],
    "city":['kathmandu', 'pokhara', 'dailekh']
}


# In[3]:


df = pd.DataFrame(dict1)


# In[4]:


df


# In[5]:


df.to_csv('friends.csv') #export csv from python


# In[6]:


df.to_csv('friends.csv', index=False)


# In[7]:


df.head(2)


# In[8]:


df.tail(2)


# In[9]:


df.describe()


# In[10]:


# read csv file 
# Bikash = pd.read_csv('filename')


# In[11]:


dict1['marks']


# In[12]:


dict1['marks'][0]


# In[13]:


dict1['marks'][0] = 50


# In[14]:


dict1


# In[15]:


#dict1.index = ['first', 'seconnd', 'third']
#harry.index


# # Series and Dataframe

# In[16]:


newdf = pd.DataFrame(np.random.rand(334, 5), index = np.arange(334))


# In[17]:


newdf


# In[18]:


newdf.head()


# In[19]:


newdf.describe()


# In[20]:


newdf.dtypes


# In[21]:


newdf[0][0] = "Bikash"


# In[22]:


newdf


# In[23]:


newdf.dtypes


# In[24]:


newdf.index


# In[25]:


newdf.columns


# # Change newdf into Numpy array

# In[26]:


newdf.to_numpy()


# In[27]:


newdf.T # newdf will transfrom rows into column and column into rows


# In[28]:


newdf.head()


# In[29]:


newdf.sort_index(axis = 0, ascending = False) #sorting in rows, axis = 0, reprents rows


# In[30]:


newdf.sort_index(axis = 1, ascending = False) # sort in columns axis = 1 reprensts column


# In[31]:


newdf.head()


# In[32]:


newdf[0] #series


# In[33]:


type(newdf[0]) #Data frame id made out of combination of series


# In[34]:


newdf2 = newdf.copy()  #copying dataframes #newdf2 is a view


# In[35]:


newdf2[0][0] = 9810


# In[39]:


newdf2 = newdf.copy()


# In[40]:


newdf2[0][0] = 98105


# In[41]:


newdf2


# # Use of loc function

# In[42]:


newdf.loc[0, 0] = 654


# In[43]:


newdf.head(2)


# In[44]:


newdf.columns = list("ABCDE")


# In[45]:


newdf


# In[47]:


newdf.head(2)


# In[52]:


newdf.loc[0, 'A'] = 6757


# In[53]:


newdf


# In[54]:


newdf.drop(0, axis=1)


# In[55]:


newdf.loc[[1,2], ['C', 'D']]


# In[57]:


newdf.loc[:, ['C', 'D']]


# In[58]:


newdf.loc[[1,2], :]


# In[59]:


newdf.drop(0, axis=1)


# In[60]:


newdf.loc[(newdf['A']<0.3), & (newdf['C']>0.1)]     #complex queries


# # Use of Ilock

# In[63]:


newdf.head(2)


# In[65]:


newdf.iloc[0,4]   #if we want to start count from 0 # If we want to start count from name


# In[70]:


newdf.iloc[[0,1], [1,2]]


# In[71]:


newdf.head(3)


# In[72]:


newdf.drop(0)


# In[78]:


# newdf.drop(['A', 'D'], axis = 1, inplace = True)


# In[79]:


newdf.head(3)


# In[80]:


newdf.reset_index()


# In[82]:


newdf.reset_index(drop = True, inplace = True)  #we drooped index Column


# In[83]:


newdf


# In[86]:


newdf.head(3)


# In[87]:


newdf['B'] = None


# In[88]:


newdf


# In[89]:


newdf['B'].isnull()


# In[91]:


newdf.shape


# In[93]:


newdf.info


# In[94]:


# newdf['name'].value_counts(dropna = False)


# In[ ]:




