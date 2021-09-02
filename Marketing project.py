#!/usr/bin/env python
# coding: utf-8

# # Answers of the test file, sheet 1

# <font color="blue">Importing necessary libraries for analysis

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# <font color="blue">Reading the test file

# In[2]:


df=pd.read_excel(r'C:\Users\Carnival\Downloads\Data_Specialist_Test (9).xlsx', header=11)


# <font color="blue">Exploring the file's information

# In[3]:


df.info()


# <font color="blue">Printing the first five rows

# In[4]:


df.head()


# <font color="blue">Deletion of the first column

# In[5]:


del df["Unnamed: 0"]


# <font color='blue'>Checking the data after deletion

# In[6]:


df.head(30)


# <font color='blue'>Checking if there are duplicate data

# In[7]:


df.duplicated()


# <font color='blue'>Key figures to explore and analyse the data

# In[8]:


fig, axes = plt.subplots(6,1, figsize=(16, 13))
fig.suptitle('Indices for assessment', fontsize=20)
sns.set_theme(style="darkgrid")

sns.barplot(ax=axes[0],x='Campaign', y="IR", data=df, color='red')
axes[0].axhline(np.median(df['IR']), ls='--', color='black')

sns.barplot(ax=axes[1],x='Campaign', y="CTR ", data=df, color='brown')
axes[1].axhline(np.median(df['CTR ']), ls='--', color='black')

sns.barplot(ax=axes[2],x='Campaign', y="Installs", data=df, color='blue')
axes[2].axhline(np.median(df['Installs']), ls='--', color='black')


sns.barplot(ax=axes[3],x='Campaign', y="Cost / Install", data=df, color='green')
axes[3].axhline(np.median(df["Cost / Install"]), ls='--', color='black')


sns.barplot(ax=axes[4],x='Campaign', y="Clicks", data=df, color='purple')
axes[4].axhline(np.median(df["Clicks"]), ls='--', color='black')


sns.barplot(ax=axes[5],x='Campaign', y="Impressions", data=df, color='orange')
axes[5].axhline(np.median(df["Impressions"]), ls='--', color='black')
axes[5].set_yscale("log")


# **1.a) Which campaign is performing the best? Based on which criteria are you making such conclusions?** 
# ><font color="red"> *C1 is the best performing campaign because it has the highest IR which means that it has the lowest number of clicks that lead to an installation. Hence, it is the most effective campaign.*
#     
# <font color="black">**1.b) How would you suggest to optimise these campaigns or what changes would you recommend? Which campaign would you allocate more resources to?**
#     
# ><font color="red">*To optimise these campaigns, the number of clicks and impressions have to increase by enhancing the quality of the advertisement. Basically, most of the campaigns has high IR. Thus, if the clicks are getting better, the installation will increase.*
#     
# ><font color="red">*I would allocate more resources to C23 because it has high CTR, but low installations. In short, this campaign is promising because many people click on it, with some modifications it can be more downloadable.*
#     
# <font color="black">**1.c) What other conclusion can you make from the data?**
# ><font color="red"> *Almost half of the campaigns got got impressions lower the median value which is the center point of al values.*
#     
# ><font color="red"> *Quite barely, all campaigns which got above average impressions are clickable and their number of clicks are above average*

# **2. Make a simple graph and indicate in title what you want to highlight?**
# ><font color="red">*The figure below*

# In[9]:


fig, ax = plt.subplots(1,2,figsize=(15,4))
fig.suptitle('Important metrics for assessing the campaigns', fontsize=20)
sns.set_theme()

sns.barplot(ax=ax[0],x='Campaign', y="IR", data=df, color='red');
ax[0].axhline(np.mean(df['IR']), ls='--', lw=3, color='blue');
ax[0].tick_params(axis='x', rotation=90)
ax[0].text(1,0.7,"Campaign 1  has the highest IR")

sns.barplot(ax=ax[1],x='Campaign', y="CTR ", data=df, color='brown');
ax[1].axhline(np.mean(df['CTR ']), ls='--', lw=3, color='blue');
ax[1].tick_params(axis='x', rotation=90)
ax[1].text(8,0.15,"Campaign 23  has the highest CTR");


# **3. What question would you ask your manager about this data set or this task?**
# ><font color='red'>*I would ask the manager about the platofrms he used for the advertisement campaigns, the sales revenue for each campaign and the data resources; are the data sources trustworthy? and whose perspective am I considering?*
