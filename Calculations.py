from sklearn.linear_model import LinearRegression
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model
from mpl_toolkits.mplot3d import Axes3D

EXPONENTS1 = 13.91
EXPONENTS2 = 16.50
# Daryl Morley used 13.91 as an exponent, John Holinger used 16.5.
TEAM_ABBR = ['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 'LAL',
             'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC', 'SAS', 'TOR', 'UTA', 'WAS']


def pythagorean_expectation1(points_for, points_against):
    return points_for**EXPONENTS1 / (points_for**EXPONENTS1 + points_against**EXPONENTS1)


def pythagorean_expectation2(points_for, points_against):
    return points_for**EXPONENTS2 / (points_for**EXPONENTS2 + points_against**EXPONENTS2)


def averageError(actual, predicted):
    totalError = 0.0
    for i in range(len(actual)):
        totalError += abs(actual[i] - predicted[i])
    return totalError / float(len(actual))


def formatData(filename):
    count = 0
    gamesCount = 1
    pts, opp_pts, wins, loses = 0, 0, 0, 0
    teamList = []
    temp = []
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


def plot_linear_regression(X_train, y_train):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(np.array(X_train)[:, 0], np.array(X_train)[:, 1],
               np.array(y_train), marker='.', color='red')
    ax.set_xlabel("Points for")
    ax.set_ylabel("Points against")
    ax.set_zlabel("win%")

    coefs = predictor.coef_
    intercept = predictor.intercept_
    xs = np.tile(np.arange(7500, 9500), (2000, 1))
    ys = np.tile(np.arange(7500, 9500), (2000, 1)).T
    zs = xs*coefs[0]+ys*coefs[1]+intercept
    print(
        "\nEquation: y = {:.2f} + ({:.12f})x1 + ({:.12f})x2".format(intercept, coefs[0], coefs[1]))
    print("\nThe coefficent of the equation:")
    print(predictor.coef_)

    ax.plot_surface(xs, ys, zs, alpha=0.5)
    plt.show()


train_input = list()
train_output = list()
actual_results = list()
pythagorean_expectation1_results = list()
pythagorean_expectation2_results = list()
linear_regression_results = list()

# train input and output for the linear regression predictor
for i in range(4):
    filepath = 'grandTeamLogs/' + str(15+i) + '/ALL-TEAMS.csv'
    retData = formatData(filepath)
    for row in retData:
        train_input.append([int(row[1]), int(row[2])])
        train_output.append(float(row[5]))

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input, y=train_output)
print(predictor.score(X=train_input, y=train_output))
print(predictor.get_params())

results = list()
teamData = formatData('grandTeamLogs/19/ALL-TEAMS.csv')
teamCount = 0

# Input the points for and points against to the model
for row in teamData:
    x = [[int(row[1]), int(row[2])]]
    outcome = predictor.predict(X=x)

    py_expectation1 = pythagorean_expectation1(
        int(row[1]), int(row[2]))
    py_expectation2 = pythagorean_expectation2(
        int(row[1]), int(row[2]))
    print()
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

    actual_results.append(float(row[5]))
    pythagorean_expectation1_results.append(float(py_expectation1))
    pythagorean_expectation2_results.append(float(py_expectation2))
    linear_regression_results.append(float(outcome))

    results.append(
        [TEAM_ABBR[teamCount], "{:.3f}".format(float(py_expectation1)), "{:.3f}".format(float(py_expectation2)), "{:.3f}".format(float(outcome)), row[5]])
    teamCount += 1

pythagorean_error = list()
linear_regression_error = list()

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

plot_linear_regression(train_input, train_output)

print("\naverage error of pythagorean expectation with exp=13.91 in 2018-2019: {:.3f}\n".format(
    averageError(actual_results, pythagorean_expectation1_results)))
print("\naverage error of pythagorean expectation with exp=16.50 in 2018-2019: {:.3f}\n".format(
    averageError(actual_results, pythagorean_expectation2_results)))
print("\naverage error of linear regression in 2018-2019: {:.3f}\n".format(
    averageError(actual_results, linear_regression_results)))
