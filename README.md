## Real Time Stock Price Prediction 
A web based product using machine learning models to predict future stock values based on the historical values.

## Forecasting Model:  
FB Prophet

[How to install anaconda ?](https://docs.anaconda.com/anaconda/install/)

## Steps to run the code:
### First thing first - clone the project
```
$ git clone https://github.com/nityansuman/Stock-Market-Prediction.git
```
### Create a project environment (Anaconda Env Recommended)
```
$ conda create --name myenv # Assuming Anaconda is installed, See above
```
### Get into the newly created virtual conda environment
```
$ source activate myenv
```
### Setup dependencies
```
$ pip install -r REQUIREMENTS.txt
```
### Run
```
$ cd Stock-Market-Prediction/stock_price_prediction/
$ python prophet.py # Open the website on the indicated port
```

In homepage, when the company ticker symbol is given, it fetches real time data using yahoo finance api.   
Once in a while, an error comes in retrieving data from yahoo finance as they check for captcha to make sure no automated system is using their data.  
In that case, just go back to the homepage and try again. 

The forecasting model tries to learn from the entire time period, predicting the data at each step using the previous data and learning from it. This helps in predicting the anamolies over the years.