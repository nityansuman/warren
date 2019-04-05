## Real Time Stock Price Prediction 

A web based product using machine learning models to predict future stock values based on the historical values.  

## Machine learning models used:  
FB Prophet

## Technologies used:
Python for backend  
Flask framework for integration of frontend and backend  
JavaScript frame work with CSS and HTML for front end  
Dygraphs for plotting  

## Steps to run the code:  
1. create a virtual environment with python3
	$virtualenv -p /usr/local/bin/python3 Dependencies  
2. Activate the virtual environment  
	$source Dependencies/bin/activate  
3. Install dependencies numpy, scipy, requests, pyyaml, tensorflow, keras  
	$pip install -r requirements.txt  
4. Run "Stock Market Prediction/prophet.py" -- this starts the http server using python flask  
5. Open the port on browser and use the site.  

## Site available at: http://13.57.46.92:5000/ 

In homepage, when the company ticker symbol is given, it fetches real time data using yahoo finance api.   
Once in a while, an error comes in retrieving data from yahoo finance as they check for captcha to make sure no automated system is using their data.  
In that case, just go back to the homepage and try again. 

The machine learning model tries to for the entire time period, predicting the data at each step using the previous data and learning from it. This helps in predicting the anamolies over the years.  

In the graph below, the blue line was the prediction based on previous data at every point. And green line is the original closing stock values. In the site, the graph is interactive, drag to zoom into particular period. Double-click to zoom out.

You can also get company information and finance news in the second page.
