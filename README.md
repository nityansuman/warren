# Real Time Stock Price Prediction

![Header](stock_price_prediction/static/background.jpg)


## Steps to run the code:

+ Clone the project
```
$ git clone https://github.com/nityansuman/Stock-Market-Prediction.git
```

+ Create a project environment (Anaconda Env Recommended)
```
$ conda create --name myenv # Assuming Anaconda is installed, See above
$ source activate myenv
```

+ Setup dependencies
```
$ pip install -r REQUIREMENTS.txt
```

+ Start the server
```
$ cd Stock-Market-Prediction/stock_price_prediction/
$ python prophet.py
```

In homepage, when the company ticker symbol is given, it fetches real time data using yahoo finance api.   
Once in a while, an error comes in retrieving data from yahoo finance as they check for captcha to make sure no automated system is using their data. In that case, just go back to the homepage and try again.