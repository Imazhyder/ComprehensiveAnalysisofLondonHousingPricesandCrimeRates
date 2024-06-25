#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


data = pd.read_csv(r"C:\Users\hp\Desktop\London Housing Dataset.csv")


# In[4]:


data


# In[5]:


# df.count
# df.isnull().sum()


# In[6]:


data.count()


# In[7]:


data.isnull()


# In[8]:


data.isnull().sum()


# In[9]:


# import seaborn as sns
# import matplotlib.pyplot as plt
# sns.heatmap(df.isnull())
# plt.show()


# In[11]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[13]:


sns.heatmap(data.isnull())
plt.show()


# In[14]:


#data.dtypes
#data.date = pd.to_datetime(data.date)


# In[15]:


data.head()


# In[16]:


data.dtypes


# In[17]:


data.date = pd.to_datetime(data.date)


# In[18]:


data.dtypes


# In[19]:


#Add a new column "year" in the dataset, which contains years only.


# In[20]:


data['year'] = data.date.dt.year


# In[21]:


data


# In[22]:


#Add a new column "month" as 2nd column in the dataset, which contains months only.


# In[23]:


data.insert(1, 'month', data.date.dt.month)


# In[24]:


data.head()


# In[25]:


#Remove the columns "year" and "month" from the dataset


# In[28]:


data.drop(['year', 'month'] , axis = 1, inplace = True)


# In[29]:


data


# In[30]:


#Show all the records where 'No. of Crimes' is 0. And, how many such records are there?


# In[34]:


data[data.no_of_crimes == 0]


# In[35]:


len(data[data.no_of_crimes == 0])


# In[36]:


#What is the maximum & minimum "average_price" per year in England?


# In[37]:


data['year'] = data.date.dt.year


# In[38]:


data.head()


# In[39]:


df1 = data[data.area == 'england']
df1


# In[40]:


#Using the groupby function


# In[43]:


df1.groupby('year').average_price.max()


# In[44]:


df1.groupby('year').average_price.min()


# In[45]:


df1.groupby('year').average_price.mean()


# In[47]:


#What is the Maximum & Minimum No. of Crimes recorded per year?
#Using the groupby function


# In[52]:


data.groupby('area').no_of_crimes.max().sort_values(ascending = False)


# In[54]:


data.groupby('area').no_of_crimes.min().sort_values(ascending = True)


# In[55]:


#Show the total count of records of England area, where average price is less than 100,000


# In[66]:


df1[df1.average_price < 100000]


# In[67]:


df1[df1.average_price < 100000].area.value_counts()


# In[ ]:




