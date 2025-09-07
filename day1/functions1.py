def calculate_sma(prices=[], window=1):
    """
    Calculate the Simple Moving Average (SMA) for the final window from the list of prices.

    Args:
        prices (list of float): List of historical prices.
        window (int): The number of periods to use for calculating the moving average.

    Returns:
        list of float: A list containing the SMA values. The length of the sreturned list will be len(prices) - window + 1.

    Raises:
        ValueError: If window is less than 1 or greater than the length of prices.
    """

    if len(prices) < window:
        print("ValueError: the length of the list of prices is less than the window size")
    return sum(prices[-window:]) / window

prices = [10, 11, 12, 13, 14, 15, 16.5, 17.5]
print(calculate_sma(prices, 5))
print(calculate_sma.__doc__)

def sum_prices(*prices):
    return sum(prices)

print(sum_prices(10, 20, 30))


def desc_trade(**kwargs):
    for key in kwargs:
        print(f'{key} --> {kwargs[key]}')

desc_trade(symbol='AAPL', result='profit')