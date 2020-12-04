#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


# In[2]:


# Test url
url = 'https://www.basketball-reference.com/teams/TOR/2020_games.html'
page = requests.get(url)
page


# In[4]:


# Mine and print raw data
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


# In[11]:


# Get the necessary columns
stats = ['date_game','opp_name','game_result','pts','opp_pts','wins','losses','game_streak']
stats_list = [[td.getText() for td in soup.findAll('td', {'data-stat': stat})] for stat in stats]


# In[20]:


# Tranpose data and organize it using DataFrame
df = pd.DataFrame(stats_list).T


# In[21]:


# Rename columns
df.columns = stats[:]


# In[25]:


df.to_csv('2020-Raptors.csv', index = False)


# In[ ]:




