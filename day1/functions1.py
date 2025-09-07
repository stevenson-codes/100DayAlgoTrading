def calculate_sma(price, window):
    """
    Calculate the Simple Moving Average (SMA) for the final window from the list of prices.

    Args:
        price (list of float): List of historical prices.
        window (int): The number of periods to use for calculating the moving average.

    Returns:
        list of float: A list containing the SMA values. The length of the sreturned list will be len(price) - window + 1.

    Raises:
        ValueError: If window is less than 1 or greater than the length of price.
    """

    if len(price) < window:
        print("ValueError: the length of the list of prices is less than the window size")
    sma = sum(price[-window]) / window

prices = (10, 11, 12, 13, 14, 15, 16.5, 17.5)
calculate_sma(prices, 5)