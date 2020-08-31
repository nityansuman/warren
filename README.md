# Real Time Stock Price Prediction

Stock market prediction is the act of trying to determine the future value of a company stock or other financial instrument traded on an exchange. The successful prediction of a stock's future price could yield significant profit. The efficient-market hypothesis suggests that stock prices reflect all currently available information and any price changes that are not based on newly revealed information thus are inherently unpredictable. Others disagree and those with this viewpoint possess myriad methods and technologies which purportedly allow them to gain future price information.
Here we make use of Facebook's Time Series forcasting algorithm Prophet to predict stock market price of US based companies.

![Header](src/static/images/header.png)


## Install Prerequisites and Run

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

* [How to install anaconda python distribution ?](https://docs.anaconda.com/anaconda/install/)
* [Prophet](https://facebook.github.io/prophet/)
* [Time Series Forecasting](https://machinelearningmastery.com/time-series-forecasting/)
* [Natural Language Processing](https://nltk.org/book/)
* [Git](https://git-scm.com/)
* [Github](https://github.com/)
* [Flask](http://flask.pocoo.org/)
* [Web Development](https://w3schoo.com/)
* [Python](https://python.org/)
* [Anaconda Python Distribution](https://conda.io)

Drop me a mail or connect with me on [Linkedin](https://linkedin.com/in/kumar-nityan-suman/) .

If you like the work I do, show your appreciation by 'FORK', 'STAR' and 'SHARE'.