#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os


# In[2]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os
import math

# In[2]:


team_code = ['TOR','NYK','BOS','BRK','PHI','CLE','IND','DET','CHI','MIL','MIA','ATL','CHO','WAS','ORL','OKC','POR','UTA','DEN','MIN','GSW','LAC','SAC','PHO','LAL','SAS','DAL','MEM','HOU','NOP']
team_prediction = [0 for i in range(0,30)]
team_result = [0 for i in range(0,30)]
year_deviation = [0 for i in range(0,6)]
residual_variance = [0 for i in range(0,6)]
year_stDev = [0 for i in range(0,6)]
sum_of_deviations = 0
count = 0
os.chdir('../grandTeamLogs')
path = "yearGraphs"
try:
    if not os.path.exists(path):
        os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)
else:
    print ("Successfully created the directory %s " % path)
def pythagorean_expectation(scored, allowed):
    return round(scored**13.91/(allowed**13.91+scored**13.91),4)
for x in range(15,21):
    os.chdir(str(x))
    for code in team_code:
        df = pd.read_csv('20'+ str(x) + '-' + code + '.csv')
        pts_scored = sum(df.pts)
        pts_allowed = sum(df.opp_pts)
        result = pythagorean_expectation(pts_scored, pts_allowed)
        team_prediction[team_code.index(code)] = result
        if df['wins'].iloc[-1] != df['wins'].max():
            team_result[team_code.index(code)] = round(((df['wins'].iloc[-1]+df['wins'].max())/df.shape[0]),4)
        else:
            team_result[team_code.index(code)] = round((df['wins'].iloc[-1]/df.shape[0]),4)
    true_winning_mean = round(sum(team_result) / len(team_code),4)
    for team in team_prediction:
        sum_of_deviations += (team - true_winning_mean)**2
    year_deviation[count] = round(sum_of_deviations,4)
    count += 1
    sum_of_deviations = 0
    os.chdir('../')
    
for sum in year_deviation:
    residual_variance[year_deviation.index(sum)] = round(sum / len(team_code),6)
    year_stDev[year_deviation.index(sum)] = round(math.sqrt(sum / len(team_code)),6)
    
f = open("resultPE.txt","a")
f.write('Sum of Deviations:\n')
f.writelines("%s\n" % deviation for deviation in year_deviation)
f.write('Residual Variance:\n')
f.writelines("%s\n" % variance for variance in residual_variance)
f.write('Standard Deviation:\n')
f.writelines("%s\n" % std for std in year_stDev)
f.close()


# In[ ]:




