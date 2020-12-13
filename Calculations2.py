from sklearn.linear_model import LinearRegression
from scipy.stats import norm
import pandas 
import statistics

TEAM_ABBR = ['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
             'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']


for i in range(4):

    filepath = 'grandTeamLogs/'+ str(15+i) +'/ALL-TEAMS.csv'
    dataframe = pandas.read_csv(filepath)
    for k in range(len(TEAM_ABBR)):
        games = dataframe[dataframe['abbr'].str.contains(TEAM_ABBR[k])]

        diff = (games['pts'] - games['opp_pts']).values.tolist()
        avg_pts = games.sum(axis=0)['pts']
        avg_allowed = games.sum(axis=0)['opp_pts']

        res = norm(scale=abs(avg_pts - avg_allowed)).cdf((avg_pts - avg_allowed) / (statistics.stdev(diff))) #I improvised the scale number
        print(res)

