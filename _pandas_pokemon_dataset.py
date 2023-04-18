#!/usr/bin/env python
# coding: utf-8

# # Loading data into pandas

# In[2]:


import pandas as pd

df = pd.read_csv('E:/Self Learning/Python/Pandas_pokemon dataset/Pokemon.csv')


# In[3]:


df.head()


# In[4]:


##Read the Headers
print(df.columns)


# In[5]:


##Read each column
print(df['Name'])


# In[6]:


#Read each row
print(df.head(4))


# In[7]:


#Read each row with iloc
print(df.iloc[1:4])


# In[8]:


#Read each row with spesific position[row,col]
print(df.iloc[2,2])


# In[9]:


#row iteration with for loop

for index, row in df.iterrows():
    print(row)


# In[10]:


#finding specific data from dataframe (same as filtering in excel)

df.loc[df['Type 1']== "Fire"]


# # Sorting/describing Data
# 
# 
# 

# In[11]:


#describe data or overview

df.describe()


# In[12]:


#sort values

df.sort_values(['Type 1', 'HP'], ascending=[1,0])


# # Making changes to data

# In[13]:


df.head(10)


# In[14]:


df['Total'] = (df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed'])


# In[15]:


df.head()


# In[16]:


df.drop(columns= ['Total'])


# In[17]:


df['Total'] = df.iloc[:,4:10].sum(axis=1)


# In[18]:


df.head()


# In[19]:


#rearrange the columns

cols = list(df.columns)
df = df[cols[0:4] + cols[5:13] + [cols[4]]]


# In[20]:


df.head()


# # Exporting data to desired format

# In[24]:


#export to csv 
#df.to_csv('modified_pokemon.csv', index=False)

#exports to xlsx
#df.to_excel('modified_pokemon.XLSX', index =False)

#exports to text
#df.to_csv('modified.txt', index=False, sep='\t')


# # Filtering Data

# In[26]:


#filter data using "AND"
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]


# In[29]:


#filter data using "AND"
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]


# In[36]:


#filter data using "OR"
new_df= df.loc[(df['Type 1'] == 'Grass') | (df['Type 2'] == 'Poison')]

#reset index
new_df.reset_index(drop=True, inplace = True)


# In[39]:


# filter using string in characters

df.loc[df['Name'].str.contains('Mega')]


# In[40]:


# filter using ~ which means filter the data which doesnt match
df.loc[~df['Name'].str.contains('Mega')]


# In[46]:


#filter string data adding regex function

import re

#df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)]

df.loc[df['Name'].str.contains('pi[a-z]*', flags=re.I, regex = True)]


# # Conditinal Changes

# In[64]:


#CHANGE FIELD BASED ON CONDITION
df.loc[df['Type 1']== 'Flamer', 'Type 1'] = 'Fire'

# change other field based on first field condition
df.loc[df['Type 1']== 'Fire', 'Legendary']= True

#Change other column fields based on greater than or less than condition
df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = 'TEST VALUE'

#change multiple column fields
df.loc[df['Total']> 500, ['Generation', 'Legendary']] = ['test1', 'test2']

df


# # Aggregate Statistics(Group by) 

# In[65]:


df = pd.read_csv('E:/Self Learning/Python/Pandas_pokemon dataset/Pokemon.csv')


# In[67]:


#use group by with mean and sort vaules in descending order

#df.groupby(['Type 1']).mean().sort_values('Defense', ascending=False)

df.groupby(['Type 1']).mean().sort_values('Attack', ascending=False)


# In[71]:


#mean
#df.groupby(['Type 1']).mean()

#sum
#df.groupby(['Type 1']).sum()

#count
df.groupby(['Type 1']).count()


# In[75]:


#create new colum and use number of count, add this count to "count" column

df['count']= 1

df.groupby(['Type 1']).count()['count']


# In[76]:


#two columns in Group by

df.groupby(['Type 1', 'Type 2']).count()['count']


# # Working with large amounts of data

# In[88]:


# instead loading all data in pandas, just load few chucks from the dataset

New_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('E:/Self Learning/Python/Pandas_pokemon dataset/Pokemon.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()
    
    new_df = pd.concat([new_df, results])


# In[89]:


new_df


# In[ ]:





# In[ ]:




