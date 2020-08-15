# Copyright 2020 The `Kumar Nityan Suman` (https://github.com/nityansuman/). All Rights Reserved.
#
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#  Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
# ==============================================================================

# Import packages
import os
import datetime
import pandas_datareader.data as web


def yahoo_stocks(symbol, start, end):
    return web.DataReader(symbol, 'yahoo', start, end)

def get_historical_stock_price(stock):
    print ("Getting historical stock prices for stock ", stock)
    #get 7 year stock data for Apple
    startDate = datetime.datetime(2010, 1, 4)
    #date = datetime.datetime.now().date()
    #endDate = pd.to_datetime(date)
    endDate = datetime.datetime(2017, 11, 28)
    stockData = yahoo_stocks(stock, startDate, endDate)
    return stockData