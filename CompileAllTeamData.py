import csv

#Enum
PTS=3
OPP_PTS=4
WINS=5
LOSSES=6
TEAM_ABBR=['ATL','BOS','BRK','CHI','CHO','CLE','DAL','DEN','DET','GSW','HOU','IND','LAC','LAL','MEM','MIA','MIL','MIN','NOP','NYK','OKC','ORL','PHI','PHO','POR','SAC','SAS','TOR','UTA','WAS']
YEARS=['15','16','17','18','19','20']
#Lists
fields=['abbr','pts','opp_pts','wins','losses']

include_cols = [PTS, OPP_PTS, WINS, LOSSES] 
for year in YEARS:
    new_rows = []
    for k in range(len(TEAM_ABBR)):

        with open('grandTeamLogs/'+year+'/20'+year+'-'+TEAM_ABBR[k]+'.csv', newline='') as csvFile:
            gamereader = csv.reader(csvFile,delimiter=',')
            next(gamereader, None)
            for row in gamereader:
                new_rows.append( (list(row[i] for i in include_cols))) #Adds team fields
                new_rows[len(new_rows)-1].insert(0,TEAM_ABBR[k]) #Adds team tag

    with open('grandTeamLogs/'+year+'/ALL-TEAMS.csv','w', newline='') as newCsvFile:
        csvwriter = csv.writer(newCsvFile, delimiter=',')
        csvwriter.writerow(fields)
        csvwriter.writerows(new_rows)
