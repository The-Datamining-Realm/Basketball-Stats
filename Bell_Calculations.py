from sklearn.linear_model import LinearRegression
from scipy.stats import norm
import pandas 
import statistics
import csv

TEAM_ABBR = ['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
             'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']

with open("CalculationResults/bell_results.csv", 'w', newline='') as outfile:
    csvwriter = csv.writer(outfile)
    csvwriter.writerow(['Team','Bell','Actual','Error'])
    results=[]
    error = 0
    for i in range(5):
        errorseason=0
        filepath = 'grandTeamLogs/'+ str(15+i) +'/ALL-TEAMS.csv'
        dataframe = pandas.read_csv(filepath)
        for k in range(len(TEAM_ABBR)):
            games = dataframe[dataframe['abbr'].str.contains(TEAM_ABBR[k])]
            games = games[:82]#only use the first 82 games of each teams season
            win_percent = "{:.1f}".format(100 * int(games.iloc[len(games.index)-1]["wins"]) /(int(games.iloc[len(games.index)-1]["wins"]) + int(games.iloc[len(games.index)-1]["losses"])))#calculates true win %

            point_diff_per_game = (games['pts'] - games['opp_pts']).values.tolist()# Makes a list of (pts for - pts allowed) for each game
            total_pts = games.sum(axis=0)['pts']# sum of all points scored by said team in this season
            total_allowed = games.sum(axis=0)['opp_pts']# sum of all points allowed by said team in this season
            avg_pts = int(games.mean(axis=0)['pts'])# average points per game for said team in this season

            res = "{:.1f}".format(100 * norm(loc= 0, scale=(avg_pts)).cdf((total_pts - total_allowed) / (statistics.stdev(point_diff_per_game)))) #Using the variables above, calcuate expected win rate

            results.append([TEAM_ABBR[k], str(res), str(win_percent), str("{:.3}".format(float(res)-float(win_percent))) ])# build rows to put into outfile
            error+= abs(float(res)-float(win_percent))#first step in error calculation
            errorseason += abs(float(res)-float(win_percent))
        print("average error in 20"+str(15+i)+": "+ str("{:.1f}".format((errorseason/len(TEAM_ABBR))))  + "%")
    print( "total average error: "+ str("{:.1f}".format((error/len(results)))) +"%")# second step in error calculation and print said error calc

    csvwriter.writerows(results)# write to csv file

