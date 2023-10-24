#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df=pd.read_csv(r'C:\Users\hindu\Downloads\Amazon Sale Report.csv')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


#drop unrelated/blank column
df.drop(['New','PendingS'],axis=1,inplace=True)


# In[8]:


#Checking null value
pd.isnull(df)


# In[9]:


#Total no of null values
pd.isnull(df).sum()


# In[10]:


#drop null value
df.dropna(inplace=True)


# In[11]:


df.shape


# In[12]:


#change data type
df['ship-postal-code']=df['ship-postal-code'].astype('int')


# In[13]:


#checking whether the data type is change or not
df['ship-postal-code'].dtype


# In[14]:


df['Date']=pd.to_datetime(df['Date'])


# In[15]:


#rename column
df.rename(columns={'Qty':'Quantity'})


# In[16]:


#describe() method returns description of the dataframe
df.describe()


# In[17]:


df.describe(include=object)


# In[18]:


#use describe() for specific column
df[['Qty','Amount']].describe()


# # Exploratory Data Analysis

# # Size

# In[19]:


ax=sns.countplot(x='Size',data=df)


# In[20]:


ax=sns.countplot(x='Size',data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# Note -From above graph you can see that most of people buys M Size

# # Group By

# The groupby() function in pandas is used to group data based on one or morecolumn in the Dataframe

# In[21]:


df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)


# In[22]:


S_Qty=df.groupby(['Size'],as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)
sns.barplot(x='Size',y='Qty',data=S_Qty)


# # Courier Status

# In[23]:


sns.countplot(data=df,x='Courier Status',hue='Status')


# In[24]:


plt.figure(figsize=(10,5))
sns.countplot(data=df,x='Courier Status',hue='Status')
plt.show()


# In[25]:


#histogram
df['Size'].hist()


# In[28]:


df['Category']=df['Category'].astype(str)
column_data=df['Category']
plt.figure(figsize=(10,5))
plt.hist(column_data,bins=30,edgecolor='Black')
plt.show()


#  Note:From above graph you can see that most of the buyer buy T-shirt

# In[32]:


#checking B2B Data by using pie chart
B2B_Check=df['B2B'].value_counts()

#plot the pie chart
plt.pie(B2B_Check,labels=B2B_Check.index,autopct='%1.1f%%')
plt.show()


# Note:From above chart we can see maximum i.e. 99.2% of buyers are retailers and 0.8% are B2B buyers

# In[38]:


#Prepare data for scatter plot
x_data=df['Category']
y_data=df['Size']

#Plot the scatter plot
plt.scatter(x_data,y_data)
plt.x_label('Category')
plt.y_label('Size')
plt.title('Scatter Plot')
plt.show()


# In[43]:


#Plot count of cities by State
plt.figure(figsize=(12,6))
sns.countplot(data=df,x='ship-state')
plt.xlabel('ship-date')
plt.ylabel('count')
plt.title('Distribution Of State')
plt.xticks(rotation=90)
plt.show()


# Note:From above graph we can see that most of the buyers are Maharashtra State

# # Conclusion

# The data analysis reveals that the business has a significant customer based in Maharashtra State, mainly serves retailers,fullfill orders through Amazon,experiences high demand for T-Shirts and sees M Size as most preffered choice among buyers.

# In[ ]:




