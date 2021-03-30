import yahoo_fin.stock_info as yf
import pandas as pd
from datetime import date, timedelta

start_date = 	01/02/2019
end_date = 03/29/2021

ticker_list_dataframe = pd.read_csv('S&P500-Symbols.csv') ###pulls up list of S&P 500 stocks storeed in CSV file
ticker_list = df["Symbol"].tolist()### sets Ticer_List to be the whole symbol colume of the S&P500-Symbols.csv file

for ticker in ticker_list:
  try:
        stock_csv_file_name = str(ticker) + '.csv'
        stock_data = yf.get_data(ticker , start_date = start_date, end_date = end_date, index_as_date = False)
        stock_data.to_csv(stock_csv_file_name)
  except (AssertionError, ValueError, KeyError):
         print('ERROR' + ticker)
         continue      
