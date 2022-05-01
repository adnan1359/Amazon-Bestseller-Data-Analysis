#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


# In[2]:


df = pd.read_csv("bestsellers.csv")
df


# In[3]:


df.head(10)


# In[4]:


df.tail(10)


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.isnull().sum()


# ## Number of Fiction Books

# In[9]:


df.loc[df['Genre'] == 'Fiction']


# In[10]:


fiction_count = df.loc[df['Genre'] == 'Fiction']["Genre"].count()
fiction_count


# - Name           312
# - Author         312
# - User Rating    312
# - Reviews        312
# - Price          312
# - Year           312
# - Genre          312
# - dtype: int64
# 

# ## Number of Non-Fiction Books

# In[11]:


df.loc[df['Genre'] == "Non Fiction"]


# In[12]:


nonFiction_count = df.loc[df["Genre"] == "Non Fiction"]["Genre"].count()
nonFiction_count


# ## Distribution of fiction and Non Fiction Books

# In[13]:


plt.figure(figsize=(10, 5))

explode = (0.07, 0)
colors = ("orange", "red")

plt.title("Distribution of Fiction and Non-Fiction Books")

plt.pie([fiction_count, nonFiction_count], labels = ["Fiction", "Non_fiction"], explode = explode, colors = colors, shadow = True, autopct='%1.2f%%')

plt.legend(loc = 4)

plt.show()


# ## Authors with most books published

# In[14]:


df['Author'].mode()


# In[15]:


author_dict = dict(df['Author'].value_counts())
author_dict


# In[16]:


author = list(author_dict.keys())[:6]
count = list(author_dict.values())[:6]


# In[17]:


plt.bar(author, count, width = 0.8, color = "seagreen")

plt.title("Authors with most books published")

plt.xlabel("Authors")
plt.ylabel("Books Published")

plt.xticks(rotation = 90)

plt.show()


# ## Author with most Fiction Books

# In[18]:


df.loc[df["Genre"] == "Fiction"]


# In[19]:


my_dict = dict(df.loc[df["Genre"] == "Fiction"]["Author"].value_counts())
my_dict


# In[20]:


author = list(my_dict.keys())[:6]
count = list(my_dict.values())[:6]


# In[21]:


plt.figure(figsize=(10, 5))

plt.title("Top Five Authors with most Non-Fiction Books")

plt.xlabel("Author Name")
plt.ylabel("Number of books published")

plt.bar(author, count)
plt.show()


# ## Authors with most Non-Fiction Books

# In[22]:


dict(df.loc[df["Genre"] == "Non Fiction"]["Author"].value_counts())


# In[23]:


my_dict = dict(df.loc[df["Genre"] == "Non Fiction"]["Author"].value_counts())
my_dict


# In[24]:


books = list(my_dict.keys())[:6]
count = list(my_dict.values())[:6]


# In[25]:


plt.figure(figsize=(10, 5))

plt.title("Top Five Authors with most Non-Fiction Books")

plt.xlabel("Author Name")
plt.ylabel("Number of books published")

plt.xticks(rotation = 90)

plt.bar(books, count, color = "seagreen")
plt.show()


# ## Most reviewed books

# In[26]:


most_reviewed = dict(zip(df["Name"], df["Reviews"]))

sorted_book_reviews = sorted(most_reviewed.items(), key = lambda x : x[1], reverse = True)
dict(sorted_book_reviews)


# ## Author with highest User Ratings

# In[27]:


unique_author_list = df["Author"].unique()


# In[28]:


mean_auth_review = {}

for auth in unique_author_list:
    mean_auth_review[auth] = df.loc[df["Author"] == auth]["User Rating"].mean()
    
sort_mean_auth_review = sorted(mean_auth_review.items(), key = lambda x : x[1], reverse = True)
dict(sort_mean_auth_review)


# ### Questions from dataset

#  - Number of Fiction Books
#  - Number of Non-Fiction Books
#  - Top 10 Best Reviewed Books
#  - Author with most books published
#  - Author with most Fiction Books
#  - Author with most Non-Fiction Books
#  - Top 5 most high-rated authors

# ## Insights from dataset

# - There are 312 Fiction Books 
# - There are 388 Non- Fiction Books
# - Check Cell[25]
# - "Gary Chapman" and "Jeff Kinney" have the most books published ( 14 each )
# - "Jeff Kinney" ( 14 ) and "Suzanne Collins" ( 12 ) have the most Fiction books published
# - "Gary Chapman" ( 14 ) and "American Psychological Association" ( 11 ) have the most Non-Fiction books published
# - Sherri Duskey Rinker', 'Rush Limbaugh', 'Patrick Thorpe', 'Eric Carle', 'Alice Schertle' are top high-rated authors with ratings ( 4.9 )

# In[ ]:





# In[ ]:




