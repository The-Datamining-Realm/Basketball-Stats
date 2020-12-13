from sklearn.linear_model import LinearRegression
from scipy.stats import norm
import pandas 
import statistics
import csv

TEAM_ABBR = ['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
             'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

with open("CalculationResults/bell_results.csv", 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(['Team','Bell','Actual'])
    results=[]
    error = 0;
    for i in range(4):

        filepath = 'grandTeamLogs/'+ str(15+i) +'/ALL-TEAMS.csv'
        dataframe = pandas.read_csv(filepath)
        
        for k in range(len(TEAM_ABBR)):
            games = dataframe[dataframe['abbr'].str.contains(TEAM_ABBR[k])]
            games = games[:82]#only use the first 83 games of each teams season
            win_percent = "{:.3f}".format(int(games.iloc[len(games.index)-1]["wins"]) /(int(games.iloc[len(games.index)-1]["wins"]) + int(games.iloc[len(games.index)-1]["losses"]) ))
            diff = (games['pts'] - games['opp_pts']).values.tolist()
            avg_pts = games.sum(axis=0)['pts']
            avg_allowed = games.sum(axis=0)['opp_pts']

            res = "{:.3f}".format(norm(scale=abs(avg_pts - avg_allowed)).cdf((avg_pts - avg_allowed) / (statistics.stdev(diff)))) #I improvised the scale number
            results.append([TEAM_ABBR[k], str(res), str(win_percent)])
            error+= abs(float(res)-float(win_percent))

    print( "average error: "+ str("{:.3f}".format(error/len(results))))
    csvwriter.writerows(results)

