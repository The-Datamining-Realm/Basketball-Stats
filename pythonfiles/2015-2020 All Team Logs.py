#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os


# In[2]:


year = 15
team = 30
team_code = ['TOR','NYK','BOS','BRK','PHI','CLE','IND','DET','CHI','MIL','MIA','ATL','CHO','WAS','ORL','OKC','POR','UTA','DEN','MIN','GSW','LAC','SAC','PHO','LAL','SAS','DAL','MEM','HOU','NOP']
stats = ['date_game','opp_name','game_result','pts','opp_pts','wins','losses','game_streak']
linkhead = "https://www.basketball-reference.com/teams/"
linktail = "_games.html"

# Create 2d array for all teams during 2015-2020
url_list = [[0 for x in range(team)] for y in range(6)]

# Create a big folder called grandTeamLogs for smaller folders by years
path = "grandTeamLogs"
try:
    if not os.path.exists(path):
        os.mkdir(path)
        os.chdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
        
cwd = os.getcwd()

# Generate urls for all teams during that span
for i in range (0,6):
    path = str(year)
    try:
        if not os.path.exists(path):
            os.mkdir(path)
            os.chdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
    else:
        print ("Successfully created the directory %s " % path)
    for j in range (0, team):
        url_list[i][j] = linkhead + str(team_code[j]) + "/20" + str(year) + linktail
        page = requests.get(url_list[i][j])
        # If any generated link doesn't work, quit the generation process
        if page.status_code != 200:
            break
        else:
            soup = BeautifulSoup(page.content, 'html.parser')
            stats_list = [[td.getText() for td in soup.findAll('td', {'data-stat': stat})] for stat in stats]
            df = pd.DataFrame(stats_list).T
            df.columns = stats[:]
            df.to_csv('20' + str(year)+ '-' + team_code[j] + '.csv', index = False)
    year += 1
    os.chdir(cwd)


# In[ ]:




