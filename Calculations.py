from sklearn.linear_model import LinearRegression
import csv
import os

EXPONENTS1 = 13.91
EXPONENTS2 = 16.50
# Daryl Morley used 13.91 as an exponent, John Holinger used 16.5.
TEAM_ABBR = ['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
             'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']


def pythagorean_expectation1(points_for, points_against):
    return points_for**EXPONENTS1 / (points_for**EXPONENTS1 + points_against**EXPONENTS1)


def pythagorean_expectation2(points_for, points_against):
    return points_for**EXPONENTS2 / (points_for**EXPONENTS2 + points_against**EXPONENTS2)


def formatData(filename):
    count = 0
    gamesCount = 1
    pts, opp_pts, wins, loses = 0, 0, 0, 0
    teamList = []
    temp = []
    cnt = 0
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if count == 30:
                break
            if row[0] == TEAM_ABBR[count]:
                if gamesCount < 82:
                    gamesCount += 1
                    pts += int(row[1])
                    opp_pts += int(row[2])
                    wins = int(row[3])
                    loses = int(row[4])
                elif gamesCount == 82:
                    temp.append(TEAM_ABBR[count])
                    temp.append(str(pts + int(row[1])))
                    temp.append(str(opp_pts + int(row[2])))
                    wins = int(row[3])
                    loses = int(row[4])
                    temp.append(str(wins))
                    temp.append(str(loses))
                    temp.append("{:.3f}".format(
                        float(row[3]) / float(gamesCount)))
                    teamList.append(temp)
                    gamesCount = 1
                    count += 1
                    pts, opp_pts, wins, loses = 0, 0, 0, 0
                    temp = []
    count = 0
    return teamList


train_input = list()
train_output = list()

for i in range(4):
    filepath = 'grandTeamLogs/' + str(15+i) + '/ALL-TEAMS.csv'
    retData = formatData(filepath)
    for row in retData:
        train_input.append([int(row[1]), int(row[2])])
        train_output.append(float(row[5]))

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input, y=train_output)

results = list()
teamData = formatData('grandTeamLogs/19/ALL-TEAMS.csv')
teamCount = 0


for row in teamData:
    print()
    py_expectation1 = pythagorean_expectation1(
        int(row[1]), int(row[2]))
    py_expectation2 = pythagorean_expectation2(
        int(row[1]), int(row[2]))
    x = [[int(row[1]), int(row[2])]]
    outcome = predictor.predict(X=x)

    print('The winning percentage of {} is: {}'.format(
        row[0], str(row[5])))
    print('The pythagorean expectation with exp=13.91 predicted the win% = ' +
          str(py_expectation1))
    diff1 = round(float(py_expectation1), 3) - float(row[5])
    if diff1 > 0.0:
        print(
            'The pythagorean expectation predicted {:.3f} above the actual win%!'.format(abs(diff1)))
    elif diff1 < 0:
        print(
            'The pythagorean expectation predicted {:.3f} below the actual win%!'.format(abs(diff1)))
    else:
        print('The pythagorean expectation predicted the correct actual win%!')

    print('The pythagorean expectation with exp=16.50 predicted the win% = ' +
          str(py_expectation2))
    diff2 = round(float(py_expectation2), 3) - float(row[5])
    if diff2 > 0.0:
        print(
            'The pythagorean expectation predicted {:.3f} above the actual win%!'.format(abs(diff2)))
    elif diff2 < 0:
        print(
            'The pythagorean expectation predicted {:.3f} below the actual win%!'.format(abs(diff2)))
    else:
        print('The pythagorean expectation predicted the correct actual win%!')

    print('The linear regression model predicted the win% = ' + str(float(outcome)))
    diff3 = round(float(outcome), 3) - float(row[5])
    if diff3 > 0.0:
        print(
            'The linear regression model predicted {:.3f} above the actual win%!'.format(abs(diff3)))
    elif diff3 < 0:
        print(
            'The linear regression model predicted {:.3f} below the actual win%!'.format(abs(diff3)))
    else:
        print('The linear regression model predicted the correct actual win%!')

    results.append(
        [TEAM_ABBR[teamCount], "{:.3f}".format(float(py_expectation1)), "{:.3f}".format(float(py_expectation2)), "{:.3f}".format(float(outcome)), row[5]])
    teamCount += 1

# pythagorean_error = list()
# linear_regression_error = list()

# for i in range(len(actual_results)):
#     pythagorean_error.append(abs(actual_results[i] - pythagorean_results[i]))
#     linear_regression_error.append(
#         abs(actual_results[i] - linear_regression_results[i]))

# pythagorean_average_error = sum(pythagorean_error) / len(pythagorean_error)
# linear_regression_average_error = sum(
#     linear_regression_error) / len(linear_regression_error)

# print()
# print('The average error in the pythagorean expectation is ' +
#       str(pythagorean_average_error*100) + ' percent')
# print('The average error in the linear regression prediction is ' + str(linear_regression_average_error*100)
#       + ' percent')

# print('The linear regression prediction is ' + str(100 - (linear_regression_average_error/pythagorean_average_error*100))
#       + ' percent more accurate')

with open('CalculationResults/result18-19.csv', 'w', newline='') as newCsvFile:
    csvwriter = csv.writer(newCsvFile, delimiter=',')
    csvwriter.writerow(['Team', 'pyth13.91', 'pyth16.50', 'linearReg', 'win%'])
    csvwriter.writerows(results)
