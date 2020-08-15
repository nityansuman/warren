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
import csv
import pandas as pd
import numpy as np
from datetime import datetime
from fbprophet import Prophet
from itertools import zip_longest
from flask import request, redirect
from flask import render_template, request, session
from werkzeug.utils import secure_filename
from src import app
from src.utils import get_historical_stock_price


@app.route("/")
@app.route("/home")
def home():
    ''' Renders the home page '''
    session["date"] = datetime.now()
    return render_template(
        "index.html"
    )

@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route("/predict", methods=["POST", "GET"])
def predict():
    stock = request.form['ticker']
    df_whole = get_historical_stock_price(stock)

    df = df_whole.filter(['Close'])

    df['ds'] = df.index
    df['y'] = np.log(df['Close'])
    original_end = df['Close'][-1]

    model = Prophet()
    model.fit(df)

    num_days = 10
    future = model.make_future_dataframe(periods=num_days)
    forecast = model.predict(future)

    print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

    df.set_index('ds', inplace=True)
    forecast.set_index('ds', inplace=True)

    viz_df = df.join(forecast[['yhat', 'yhat_lower','yhat_upper']], how = 'outer')
    viz_df['yhat_scaled'] = np.exp(viz_df['yhat'])

    close_data = viz_df.Close
    forecasted_data = viz_df.yhat_scaled
    date = future['ds']
    forecast_start = forecasted_data[-num_days]

    d = [date, close_data, forecasted_data]
    export_data = zip_longest(*d, fillvalue = '')
    with open('src/database/corpus/numbers.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerow(("Date", "Actual", "Forecasted"))
        wr.writerows(export_data)
    myfile.close()

    return render_template(
        "output.html",
        original = round(original_end,2),
        forecast = round(forecast_start,2),
        stock_tinker = stock.upper()
        )