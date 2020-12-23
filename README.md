# Basketball Data Mining and Analytics

This project aims to harvest basketball data from reputable sites, namely [Basketball Reference](https://www.basketball-reference.com/) in an attempt to mine interesting patterns in order to visualize and assess basketball game winning formula for the current era.

---

## Installation

Install [Python 3.8 with pip](https://docs.microsoft.com/en-us/windows/python/beginners)

NBA_api_test requires `pip install nba_api`

standard_api_test requires `pip install request`

libraries/packages required to run the calculations:
`pip install sklearn`
`pip install matplotlib`
`pip install mpl_toolkits`
`pip install numpy`
`pip install csv`

## Usage

#### grandTeamLogs

Contains all the raw NBA result data from [Basketball Reference](www.basketball-reference.com)

#### Training data

Contains processed NBA stat as csv to train our linear regression model

#### Run the calculations

To get the predicted results by all of our methods. Run the `calculations.py` file using this command line in terminal:

```bash
python3 calculation.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
