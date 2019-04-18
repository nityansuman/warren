## Real Time Stock Price Prediction 
A web based product using machine learning models to predict future stock values based on the historical values.

## Forecasting Model:  
FB Prophet

[How to install anaconda ?](http://anaconda.org/)

## Steps to run the code:

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
$ python prophet.py # Open the website on the indicated port
```

**Site available at: http://13.57.46.92:5000/**

In homepage, when the company ticker symbol is given, it fetches real time data using yahoo finance api.   
Once in a while, an error comes in retrieving data from yahoo finance as they check for captcha to make sure no automated system is using their data.  
In that case, just go back to the homepage and try again. 

The forecasting model tries to learn from the entire time period, predicting the data at each step using the previous data and learning from it. This helps in predicting the anamolies over the years.