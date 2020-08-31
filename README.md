# Real Time Stock Price Prediction
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


![GitHub](https://img.shields.io/github/license/nityansuman/warren)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/nityansuman/warren)
![GitHub repo size](https://img.shields.io/github/repo-size/nityansuman/warren)
![GitHub language count](https://img.shields.io/github/languages/count/nityansuman/warren)

![Maintenance](https://img.shields.io/maintenance/yes/2020)
![GitHub last commit](https://img.shields.io/github/last-commit/nityansuman/warren)

Stock market prediction is the act of trying to determine the future value of a company stock or other financial instrument traded on an exchange. The successful prediction of a stock's future price could yield significant profit. The efficient-market hypothesis suggests that stock prices reflect all currently available information and any price changes that are not based on newly revealed information thus are inherently unpredictable. Others disagree and those with this viewpoint possess myriad methods and technologies which purportedly allow them to gain future price information.
Here we make use of Facebook's Time Series forcasting algorithm Prophet to predict stock market price of US based companies in real teim using multi-variate, single step forecasting strategy.

![Header](src/static/images/header.png)

## Install Pre-requisites and Run

```
# Download/clone the project from github
$ git clone https://github.com/nityansuman/stock-price-prediction-app.git

# Create a project environment with Anaconda
$ conda create --name envname python
$ conda activate envname

# Install and set-up required packages
$ pip install -r REQUIREMENTS.txt

# Navigate to the root folder
$ cd stock-price-prediction-app/

# Run
$ python runserver.py
```

## Model Validation Analysis (30-day Validation Period)

### Facebook (Stock: FB) Validation
![FB_validation](src/static/images/fb_forecast_30_day_validation.png)


### Microsoft (Stock: MSFT) Validation
![FB_validation](src/static/images/msft_forecast_30day_validation.png)

### Google (Stock: GOOGL) Validation
![FB_validation](src/static/images/googl_forecast_30day_validation.png)

## Important Links

* [Git](https://git-scm.com/)
* [Python](https://python.org/)
* [Github](https://github.com/)
* [Flask](http://flask.pocoo.org/)
* [Web Development](https://w3schoo.com/)
* [Anaconda Python Distribution](https://conda.io)
* [Prophet](https://facebook.github.io/prophet/)
* [Time Series Forecasting](https://machinelearningmastery.com/time-series-forecasting/)
* [How to install anaconda python distribution ?](https://docs.anaconda.com/anaconda/install/)

Drop me a mail or connect with me on [Linkedin](https://linkedin.com/in/kumar-nityan-suman/) .

If you like the work I do, show your appreciation by 'FORK', 'STAR' and 'SHARE'.