# Copyright 2020 `Kumar Nityan Suman` (https://github.com/nityansuman/). All Rights Reserved.
#
#                     GNU GENERAL PUBLIC LICENSE
#                        Version 3, 29 June 2007
#  Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
#  Everyone is permitted to copy and distribute verbatim copies
#  of this license document, but changing it is not allowed.
# ==============================================================================

# Import packages
import datetime
import pandas as pd
import yfinance as yf
import fbprophet as prophet


class Dataset:
	def build_dataset(self):
		# Set date range
		start_date = datetime.datetime(2010, 1, 1).date()
		end_date = datetime.datetime.now().date()
		
		# Create historical datatset from the past decade
		try:
			self.dataset = self.socket.history(start=start_date, end=end_date, interval="1d").reset_index()
			self.dataset.drop(columns=["Dividends", "Stock Splits", "Volume"], inplace=True)
			self.add_forecast_date()
		except Exception as e:
			print("Exception raised at: `utils.Dataset.build()", e)
			return False
		else:
			return True
	
	def add_forecast_date(self):
		# Add placeholder for forecast
		present_date = self.dataset.Date.max()
		day_number = pd.to_datetime(present_date).isoweekday()
		if day_number in [5, 6]:
		    self.forecast_date = present_date + datetime.timedelta(days=(7-day_number) + 1)
		else:
		    self.forecast_date = present_date + datetime.timedelta(days=1)
		print("Present date:", present_date)
		print("Valid Forecast Date:", self.forecast_date)
		test_row = pd.DataFrame([[self.forecast_date, 0.0, 0.0, 0.0, 0.0]], columns=self.dataset.columns)
		self.dataset = pd.concat([self.dataset, test_row])


class FeatureEngineering(Dataset):	
	def create_features(self):
		status = self.build_dataset()
		if status:
			self.create_lag_fetaures()
			self.impute_missing_values()
			self.dataset.drop(columns=["Open", "High", "Low"], inplace=True)
			print(self.dataset.tail(3))
			return True
		else:
			raise Exception("Dataset creation failed!")
	
	def create_lag_fetaures(self):
		for i in range(1, 7):
		    self.dataset[f"Close_lag_{i}"] = self.dataset.Close.shift(periods=i, axis=0)
		    self.dataset[f"Open_lag_{i}"] = self.dataset.Open.shift(periods=i, axis=0)
		    self.dataset[f"High_lag_{i}"] = self.dataset.High.shift(periods=i, axis=0)
		    self.dataset[f"Low_lag_{i}"] = self.dataset.Low.shift(periods=i, axis=0)
		return True
	
	def impute_missing_values(self):
		self.dataset.fillna(0, inplace=True)
		self.info["min_date"] = self.dataset.Date.min().date()
		self.info["max_date"] = self.dataset.Date.max().date() - datetime.timedelta(days=1)
		return True


class MasterProphet(FeatureEngineering):
	def __init__(self, ticker):
		self.ticker = ticker
		self.socket = yf.Ticker(self.ticker)
		self.info = {
			"sector": self.socket.info["sector"],
			"summary": self.socket.info["longBusinessSummary"],
			"country": self.socket.info["country"],
			"website": self.socket.info["website"],
			"employees": self.socket.info["fullTimeEmployees"]
		}
	
	def build_model(self):
		additonal_features = [col for col in self.dataset.columns if "lag" in col]
		try:
			self.model = prophet.Prophet(yearly_seasonality=True, weekly_seasonality=True, seasonality_mode="additive")
			for name in additonal_features:
				self.model.add_regressor(name)
		except Exception as e:
			print("Exception raised at: `utilities.Prophet.build()`", e)
			return False
		else:
			return True
	
	def train_and_forecast(self):
		self.model.fit(df=self.dataset.iloc[:-1, :].rename(columns={"Date": "ds", "Close":"y"}))
		return self.model.predict(self.dataset.iloc[-1:][[col for col in self.dataset if col != "Close"]].rename(columns={"Date": "ds"}))
	
	def forecast(self):
		self.create_features()
		self.build_model()
		return self.train_and_forecast()