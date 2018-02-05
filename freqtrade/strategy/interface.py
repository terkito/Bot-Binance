"""
IStrategy interface
This module defines the interface to apply for strategies
"""

from abc import ABC, abstractmethod
from pandas import DataFrame


class IStrategy(ABC):
    """
    Interface for freqtrade strategies
    Defines the mandatory structure must follow any custom strategies

    Attributes you can use:
        minimal_roi -> Dict: Minimal ROI designed for the strategy
        stoploss -> float: optimal stoploss designed for the strategy
        ticker_interval -> int: value of the ticker interval to use for the strategy
    """

    @abstractmethod
    def populate_indicators(self, dataframe: DataFrame, pair: str) -> DataFrame:
        """
        Populate indicators that will be used in the Buy and Sell strategy
        :param dataframe: Raw data from the exchange and parsed by parse_ticker_dataframe()
        :param pair: the pair that was is concerned by the dataframe
        :return: a Dataframe with all mandatory indicators for the strategies
        """

    @abstractmethod
    def populate_buy_trend(self, dataframe: DataFrame, pair: str) -> DataFrame:
        """
        Based on TA indicators, populates the buy signal for the given dataframe
        :param dataframe: DataFrame
        :param pair: the pair that was is concerned by the dataframe
        :return: DataFrame with buy column
        :return:
        """

    @abstractmethod
    def populate_sell_trend(self, dataframe: DataFrame, pair: str) -> DataFrame:
        """
        Based on TA indicators, populates the sell signal for the given dataframe
        :param dataframe: DataFrame
        :param pair: the pair that was is concerned by the dataframe
        :return: DataFrame with buy column
        """

    @abstractmethod
    def did_bought(self, pair: str):
        """
        we are notified that a given pair was bought
        :param pair: the pair that was is concerned by the dataframe
        """

    @abstractmethod
    def did_sold(self, pair: str):
        """
        we are notified that a given pair was sold
        :param pair: the pair that was is concerned by the dataframe
        """

    @abstractmethod
    def did_cancel_buy(self, pair: str):
        """
        we are notified that a given buy for a pair was cancelled
        :param pair: the pair that was is concerned by the dataframe
        """

    @abstractmethod
    def did_cancel_sell(self, pair: str):
        """
        we are notified that a given sell for a pair was cancelled
        :param pair: the pair that was is concerned by the dataframe
        """
