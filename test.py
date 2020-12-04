from sklearn.linear_model import LinearRegression
import csv
import os

EXPONENTS1 = 13.91
EXPONENTS2 = 16.50
# Daryl Morley used 13.91 as an exponent, John Holinger used 16.5.


def pythagorean_expectation1(points_for, points_against):
    return points_for**EXPONENTS1 / (points_for**EXPONENTS1 + points_against**EXPONENTS1)


def pythagorean_expectation2(points_for, points_against):
    return points_for**EXPONENTS2 / (points_for**EXPONENTS2 + points_against**EXPONENTS2)


teams = list()
west = [6, 7, 9, 10, 12, 13, 14, 17, 18, 20, 23, 24, 25, 26, 28]
east = [0, 1, 2, 3, 4, 5, 8, 11, 15, 16, 19, 21, 22, 27, 29]
west_teams = list()
east_teams = list()
train_input = list()
train_output = list()

for file in os.listdir('Training Data'):
    if file.endswith('.csv'):
        rout = 'Training Data/' + file
        with open(rout, 'r') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if row[1] != 'GP':
                    train_input.append([int(row[5]), int(row[6])])
                    train_output.append(float(row[4]))

predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=train_input, y=train_output)

pythagorean_results1 = list()
pythagorean_results2 = list()
linear_regression_results = list()
actual_results = list()

with open('nba18-19.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    count = 0
    for row in reader:
        if row[1] != 'GP':
            # print()
            py_expectation1 = pythagorean_expectation1(
                int(row[5]), int(row[6]))
            py_expectation2 = pythagorean_expectation2(
                int(row[5]), int(row[6]))
            x = [[int(row[5]), int(row[6])]]
            outcome = predictor.predict(X=x)

            teams.append([count, str(row[0]), outcome])
            count += 1
            # print('The winning percentage of {} is: {}'.format(
            #     row[0], str(row[4])))
            # print('The pythagorean expectation with exp=13.91 is: ' +
            #       str(py_expectation1))
            # diff1 = float(py_expectation1) - float(row[4])
            # if diff1 > 0.0:
            #     print(
            #         'The pythagorean expectation predicted {:.3f} above the actual win%!'.format(abs(diff1)))
            # elif diff1 < 0:
            #     print(
            #         'The pythagorean expectation predicted {:.3f} below the actual win%!'.format(abs(diff1)))
            # else:
            #     print('The pythagorean expectation predicted the correct actual win%!')

            # print('The pythagorean expectation with exp=16.50 is: ' +
            #       str(py_expectation2))
            # diff2 = float(py_expectation2) - float(row[4])
            # if diff2 > 0.0:
            #     print(
            #         'The pythagorean expectation predicted {:.3f} above the actual win%!'.format(abs(diff2)))
            # elif diff2 < 0:
            #     print(
            #         'The pythagorean expectation predicted {:.3f} below the actual win%!'.format(abs(diff2)))
            # else:
            #     print('The pythagorean expectation predicted the correct actual win%!')

            # print('The linear regression model predicted: ' + str(outcome))
            # diff3 = float(outcome) - float(row[4])
            # if diff3 > 0.0:
            #     print(
            #         'The pythagorean expectation predicted {:.3f} above the actual win%!'.format(abs(diff3)))
            # elif diff3 < 0:
            #     print(
            #         'The pythagorean expectation predicted {:.3f} below the actual win%!'.format(abs(diff3)))
            # else:
            #     print('The pythagorean expectation predicted the correct actual win%!')

            # if abs(float(py_expectation) - float(row[4])) > abs(float(outcome) - float(row[4])):
            #     print('In this case, the linear regression model is more accurate')
            # elif abs(float(py_expectation) - float(row[4])) < abs(float(outcome) - float(row[4])):
            #     print('In this case, the pythagorean expectation is more accurate')
            # else:
            #     print('This is highly unlikely')

            pythagorean_results1.append(float(py_expectation1))
            pythagorean_results2.append(float(py_expectation2))
            linear_regression_results.append(float(outcome))
            actual_results.append(float(row[1]))

for team in teams:
    if team[0] in west:
        west_teams.append(team)
    else:
        east_teams.append(team)


def sort_criteria(obj):
    return float(obj[2])


west_teams.sort(reverse=True, key=sort_criteria)
east_teams.sort(reverse=True, key=sort_criteria)

print("West Teams:")
for team in west_teams:
    print(team[1])
print()
print("East Teams:")
for team in east_teams:
    print(team[1])
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
