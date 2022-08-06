# https://github.com/man-c/pycoingecko
from pycoingecko import CoinGeckoAPI
from datetime import datetime
# https://pandas.pydata.org/docs/getting_started/install.html#installing-from-pypi
import pandas as pd
import time
import json

cg = CoinGeckoAPI()

print('\n Starting price script...')

# Set start date and convert to unix timestamp
# Entered desired date below with yr, mo, day, hr, min.
startdate = datetime(2022, 7, 1, 0, 0)
# print(startdate)
startdate = datetime.timestamp(startdate)
# print('startdate timestamp= ', startdate)
startdate = str(startdate)
print('startdate string= ', startdate)

# Set end date and convert to unix timestamp
# Entered desired date below with yr, mo, day, hr, min.
enddate =  datetime(2022, 8, 1, 0, 0)
# print(enddate)
enddate = datetime.timestamp(enddate)
# print('end date timestamp= ', enddate)
enddate = str(enddate)
print('end date string= ', enddate)

print('\n getting data from coingecko...')
# Import price data from coingecko. 
# TWAP data feed. Takes inputs for token, reference currency, and timeframe.
#f= open('output.json')
#data = json.load(f)
data = cg.get_coin_ohlc_by_id(id='yam-2', vs_currency='usd', days= 30)

# 30 day average price data feed. Takes inputs for token, reference currency, and a specific timeframe. 
# Timeframe to be determined with 'startdate' and 'enddate' parameters above
data2 = cg.get_coin_market_chart_range_by_id(id='yam-2', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)

print('\n received data from coingecko. calculating prices...')

#-------------------------------------------

# option 1. True twap for last 30 days using candle data. Coingecko data gets worse after 30days
# create dataframe and format columns
df = pd.DataFrame(data, columns = ["date", "open", "high", "low", "close"])
# print('\n twap data frame df: \n \n', df)

#convert date from unix to date-time so it isn't read in mean calcs.
df['date'] = pd.to_datetime(df['date'], unit='ms')
# print('\n twap data frame df with readable date: \n \n',df)

# Calculate the mean of each row
df['av_row'] = df.mean(axis=1, numeric_only=True)
# print(df)

# Calculate the TWAP by taking the mean of the means just found
twap = df['av_row'].mean()
print('\n last 30 day TWAP value is: ', twap)

#------------------------------------------

# Option 2. Average price over timeframe specified at start.
# print(data2)
dfrange = pd.DataFrame(data2)
# print('\n \n raw data= \n \n', dfrange)

# remove un-needed data
cleanedrange = dfrange.drop(['market_caps', 'total_volumes'], axis='columns')
# print('\n \n unnecessary columns dropped from dataset= \n \n', cleanedrange.columns)

#clean up data by splitting list into separate dataframe
split_range = pd.DataFrame(cleanedrange['prices'].tolist(), columns = ['date', 'price'])
# print('\n \n clean up dataset with 2 columns, date and price= \n \n ', split_range)

#convert date from unix to date-time so it isn't read in mean calcs.
split_range['date'] = pd.to_datetime(split_range['date'], unit='ms')
# print('\n \n make date human readable= \n \n', split_range)

# Calculate the average value by taking the mean of the price column
averageprice = split_range['price'].mean()
print('\n 30 day average value is: ', averageprice)


