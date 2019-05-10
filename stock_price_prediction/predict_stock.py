""" 
@Author: kumar.nityan.suman
@Date: 2019-05-11 01:32:09
"""


# Load packages
import os
import sys
import requests
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Define file to store downloaded historical data
FILE_NAME = "historical.csv"


def get_historical(quote):
    """Download historical data for the given company from google finance.
    
    Arguments:
        quote {String} -- A string representing the company quote (name-symbol).
    
    Returns:
        Bool -- Returns True on download.
    """
    url = "http://www.google.com/finance/historical?q=NSE%3A" + quote + "&output=csv"
    r = requests.get(url, stream=True)
    if r.status_code != 400:
        with open(FILE_NAME, mode="wb") as f:
            for chunk in r:
                f.write(chunk)
        return True

def stock_prediction():
    """Load historical data from the csv file.
    
    Returns:
        String -- Denoting the movement of the price.
    """
    dataset = list()
    with open(FILE_NAME) as f:
        for n, line in enumerate(f):
            if n != 0:
                str = line.split(",")[1]
                if str != "-":
                    dataset.append(float(line.split(",")[1]))
    
    dataset = np.array(dataset)

    # Create dataset matrix (X=t and Y=t+1)
    def create_dataset(dataset):
        dataX = [dataset[n+1] for n in range(len(dataset)-2)]
        return np.array(dataX), dataset[2:]
        
    trainX, trainY = create_dataset(dataset)

    # Create and fit Multilinear Perceptron model
    model = Sequential()
    model.add(Dense(8, input_dim=1, activation="relu"))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error", optimizer="adam")
    model.fit(trainX, trainY, nb_epoch=200, batch_size=2, verbose=2)

    # Our prediction for tomorrow
    prediction = model.predict(np.array([dataset[0]]))
    result = "The price will move from %s to %s" % (dataset[0], prediction[0][0])
    return result

# Ask user for a stock quote
stock_quote = input("Enter a stock quote (e.j: AAPL, FB, GOOGL): ").upper()

# Check if we got the historical data
if not get_historical(stock_quote):
    print ("Google returned a 404, please re-run the script and enter a valid stock quote.")
    sys.exit()

# We have our file so we create the neural net and get the prediction
print(stock_prediction())

# We are done so we delete the csv file
os.remove(FILE_NAME)