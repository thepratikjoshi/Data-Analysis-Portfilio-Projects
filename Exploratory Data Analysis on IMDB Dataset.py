#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis on IMDB Dataset.

# This notebook is dedicated to exploratory data analysis of IMDB dataset. Below you can find the movie data between 2006 and 2016. I've tried to answer the questions that comes across my mind as a Movie lover.

# ![IMDb_Header_Page.jpg](attachment:IMDb_Header_Page.jpg)

# Importing Data and Required Libraries for the Analysis.

# In[81]:


#Importing Libraries 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[80]:


#Extracting the data from a IMDB data file.

df = pd.read_csv('F:\IMDB-Movie-Data.csv')


# In[4]:


# Looking the Data.
df.head()


# In[5]:


df.shape


# In[6]:


print(('Number of Rows',df.shape[0]))
print(("Number of Columns",df.shape[1]))


# In[7]:


df.info()


# Now, Checking If there are any Missing/Null Values.

# In[8]:


print('Any Missing Values?' , df.isnull().values.any())


# In[9]:


df.isnull().sum()


# In[83]:


#plotting heatmap to check the locations of the missing values. 
sns.heatmap(df.isnull())


# In[84]:


#missing values in Percentge.

per_missing = df.isnull().sum()*100/len(df)
per_missing


# In[12]:


# Dropping the Null vales.
df.dropna(axis=0,inplace = True)


# In[13]:


df.shape


# Checking whether there are any Duplicate Values or Not

# In[14]:


dup_data = df.duplicated().any()


# In[15]:


print('Any duplicate values?',dup_data)


# There are No Duplicate values in the Dataset.

# In[20]:


df.describe(include = 'all')


# In[21]:


df.columns


# # Highest  Avg. Voting per Year

# In[25]:


df.groupby('Year')['Votes'].mean().sort_values(ascending=False)


# In[27]:


sns.barplot(x='Year',y='Votes',data=df)
plt.title("Avg.votes per year")
plt.show()


# Graph shows Year '2012' have Maximum Number of  Average Voting as compared to other Years. 

# # Highest  Avg. Revenue per Year

# In[28]:


df.groupby('Year')['Revenue (Millions)'].mean().sort_values(ascending=False)


# In[29]:


sns.barplot(x='Year',y='Revenue (Millions)',data=df)
plt.title("Avg. Revenue per year")
plt.show()


# Graph shows Year '2009' have Maximum Average Revenue as compared to other Years. 

# # Top 10 Lengthy Movies

# In[32]:


top10_runtime = df.nlargest(10,'Runtime (Minutes)')[['Title', 'Runtime (Minutes)']].set_index('Title')
top10_runtime


# In[33]:


sns.barplot(x='Runtime (Minutes)',y = top10_runtime.index, data = top10_runtime)
plt.title('Top 10 Lengthy Movies')


# It shows "The Hateful Eight" is the longest movie.

# # Number of Movies produced per Year

# In[34]:


df['Year'].value_counts()


# In[35]:


sns.countplot(x='Year',data=df)
plt.title('Number of Movies per Year')
plt.show()


# In 2016, Most number of movies are Produced.

# # Top 10 Highest Rated Movies according to it's IMDB Rating

# In[36]:


top10_rating = df.nlargest(10,'Rating')[['Title', 'Rating','Director']].set_index('Title')
top10_rating


# In[37]:


sns.barplot(x='Rating', y= top10_rating.index,data=top10_rating, hue='Director',dodge=False)
plt.title('Top Rated Movies')
plt.legend(bbox_to_anchor=(1.05,1),loc=2)


# This represents "The Dark Knight" is the Top Rated Movie and its directed by Christopher Nolan.

# # Most Popular Movies according to Revenue.

# In[38]:


top10_rev = df.nlargest(10,'Revenue (Millions)')[['Title','Revenue (Millions)']].set_index('Title')
top10_rev


# In[41]:


sns.barplot(x='Revenue (Millions)',y=top10_rev.index, data = top10_rev)
plt.title('Most Popular Movies according to Revenue')


# The Movie named "Star Wars: Episode VII - The Force Awakens" is the Most popular Movie.

# # Checking whether Ratings affect the Revenue of the Movies?

# In[42]:


sns.scatterplot(x='Rating', y='Revenue (Millions)', data=df)


# Scatter plot shows Top Rated Movies generated the High Revenue. hence Rating of the Movies affect the Revenue.

# # Classifying movies based on ratings (Excellent,Good, Average and Poor)

# In[60]:


def rating(rating):
    if rating>= 8.0:
        return "Excellent"
    elif rating>=6.0:
        return "Good"
    elif rating>=4.0:
        return "Average"
    else:
        return "Poor"


# In[61]:


df['rating categ'] = df['Rating'].apply(rating)


# In[62]:


df.head()


# In[63]:


df['rating categ'].value_counts()


# In[64]:


sns.countplot(x='rating categ',data=df)
plt.title('Movies as per Rating Category')
plt.show()


# # Total Number of Movies per Genre

# In[65]:


df['Genre']


# In[67]:


#find unique value from genre

list1=[]
for value in df['Genre']:
    list1.append(value.split(','))
    
list1


# In[69]:


one_d =[]
for item in list1:
    for item1 in item:
        one_d.append(item1)

one_d


# In[70]:


uni_list = []


# In[72]:


for item in one_d:
    if item not in uni_list:
        uni_list.append(item)
        
uni_list


# In[73]:


len(uni_list)


# There are 20 Unique Genres.

# # Total Number of Movies Per Genres are as follows:

# In[77]:


from collections import Counter
Counter(one_d)

