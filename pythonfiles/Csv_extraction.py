import csv

#Enum
PTS=3
OPP_PTS=4
WINS=5
LOSSES=6

#Lists
include_cols = [PTS, OPP_PTS, WINS, LOSSES] 
important_information = []

with open('team_logs/2020-Raptors.csv', newline='') as csvFile:
    gamereader = csv.reader(csvFile,delimiter=',')
    for row in gamereader:
        important_information.append( list(row[i] for i in include_cols))

    important_information.remove(['pts', 'opp_pts', 'wins', 'losses'])
    print(important_information)