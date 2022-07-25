# Script to get cleaned up historical prices from coingecko.

# https://github.com/man-c/pycoingecko
from pycoingecko import CoinGeckoAPI
from datetime import datetime
import pandas as pd
import time
import json

cg = CoinGeckoAPI()

# Set start date and convert to unix timestamp
# Entered desired date below with yr, mo, day, hr, min.
startdate = datetime(2022, 7, 1, 0, 0)
print(startdate)
startdate = datetime.timestamp(startdate)
print('startdate timestamp= ', startdate)
startdate = str(startdate)
print('startdate string= ', startdate)

# Set end date and convert to unix timestamp
# Entered desired date below with yr, mo, day, hr, min.
enddate =  datetime(2022, 7, 2, 0, 0)
print(enddate)
enddate = datetime.timestamp(enddate)
print('end date timestamp= ', enddate)
enddate = str(enddate)
print('end date string= ', enddate)

# Call the coingecko API to get data for each asset. Delay is added to avoid the rate limit
# Timeframe to be determined with 'startdate' and 'enddate' parameters above
print('getting YAM price...')
yamdata = cg.get_coin_market_chart_range_by_id(id='yam-2', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting BTC price...')
btcdata = cg.get_coin_market_chart_range_by_id(id='bitcoin', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting ETH price...')
ethdata = cg.get_coin_market_chart_range_by_id(id='ethereum', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting stETH price...')
stethdata = cg.get_coin_market_chart_range_by_id(id='staked-ether', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting SUSHI price...')
sushidata = cg.get_coin_market_chart_range_by_id(id='sushi', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting xSUSHI price...')
xsushidata = cg.get_coin_market_chart_range_by_id(id='xsushi', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting UMA price...')
umadata = cg.get_coin_market_chart_range_by_id(id='uma', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting GTC price...')
gtcdata = cg.get_coin_market_chart_range_by_id(id='gitcoin', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting DPI price...')
dpidata = cg.get_coin_market_chart_range_by_id(id='defipulse-index', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting INDEX price...')
indexdata = cg.get_coin_market_chart_range_by_id(id='index-cooperative', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')
time.sleep(5)

print('getting MUST price...')
mustdata = cg.get_coin_market_chart_range_by_id(id='must', vs_currency='usd', from_timestamp= startdate, to_timestamp=enddate)
print('Got price, waiting to query next...')

print('retrieved all prices')


# --- YAM

yamdf = pd.DataFrame(yamdata)
#print('\n \n raw data= \n \n', yamdf)

# remove un-needed data
yamdf = yamdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', yamdf.columns)

#clean up data by splitting list into separate dataframe
yamdf = pd.DataFrame(yamdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', yamdf)

#convert date from unix to date-time so it isn't read in mean calcs.
yamdf['date'] = pd.to_datetime(yamdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', yamdf)

# Calculate the average value by taking the mean of the price column
YAMprice = yamdf['price'].mean()
print('\n YAM 1 day average value is: ', YAMprice)
YAM = ['YAM', YAMprice]
allPrices = [YAM]

# --- BTC

BTCdf = pd.DataFrame(btcdata)
#print('\n \n raw data= \n \n', BTCdf)

# remove un-needed data
BTCdf = BTCdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', BTCdf.columns)

#clean up data by splitting list into separate dataframe
BTCdf = pd.DataFrame(BTCdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', BTCdf)

#convert date from unix to date-time so it isn't read in mean calcs.
BTCdf['date'] = pd.to_datetime(BTCdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', BTCdf)

# Calculate the average value by taking the mean of the price column
BTCprice = BTCdf['price'].mean()
print('\n BTC 1 day average value is: ', BTCprice)
BTC = ['BTC', BTCprice]
allPrices.append(BTC)

# --- ETH

ETHdf = pd.DataFrame(ethdata)
#print('\n \n raw data= \n \n', ETHdf)

# remove un-needed data
ETHdf = ETHdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', ETHdf.columns)

#clean up data by splitting list into separate dataframe
ETHdf = pd.DataFrame(ETHdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', ETHdf)

#convert date from unix to date-time so it isn't read in mean calcs.
ETHdf['date'] = pd.to_datetime(ETHdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', ETHdf)

# Calculate the average value by taking the mean of the price column
ETHprice = ETHdf['price'].mean()
print('\n ETH 1 day average value is: ', ETHprice)
ETH = ['ETH', ETHprice]
allPrices.append(ETH)

# -- stETH

stETHdf = pd.DataFrame(stethdata)
#print('\n \n raw data= \n \n', stETHdf)

# remove un-needed data
stETHdf = stETHdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', stETHdf.columns)

#clean up data by splitting list into separate dataframe
stETHdf = pd.DataFrame(stETHdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', stETHdf)

#convert date from unix to date-time so it isn't read in mean calcs.
stETHdf['date'] = pd.to_datetime(stETHdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', stETHdf)

# Calculate the average value by taking the mean of the price column
stETHprice = stETHdf['price'].mean()
print('\n stETH 1 day average value is: ', stETHprice)
stETH = ['stETH', stETHprice]
allPrices.append(stETH)

# --- SUSHI

SUSHIdf = pd.DataFrame(sushidata)
#print('\n \n raw data= \n \n', SUSHIdf)

# remove un-needed data
SUSHIdf = SUSHIdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', SUSHIdf.columns)

#clean up data by splitting list into separate dataframe
SUSHIdf = pd.DataFrame(SUSHIdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', SUSHIdf)

#convert date from unix to date-time so it isn't read in mean calcs.
SUSHIdf['date'] = pd.to_datetime(SUSHIdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', SUSHIdf)

# Calculate the average value by taking the mean of the price column
SUSHIprice = SUSHIdf['price'].mean()
print('\n SUSHI 1 day average value is: ', SUSHIprice)
SUSHI = ['SUSHI', SUSHIprice]
allPrices.append(SUSHI)

# --- XSUSHI

XSUSHIdf = pd.DataFrame(xsushidata)
#print('\n \n raw data= \n \n', XSUSHIdf)

# remove un-needed data
XSUSHIdf = XSUSHIdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', XSUSHIdf.columns)

#clean up data by splitting list into separate dataframe
XSUSHIdf = pd.DataFrame(XSUSHIdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', XSUSHIdf)

#convert date from unix to date-time so it isn't read in mean calcs.
XSUSHIdf['date'] = pd.to_datetime(XSUSHIdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', XSUSHIdf)

# Calculate the average value by taking the mean of the price column
XSUSHIprice = XSUSHIdf['price'].mean()
print('\n xSUSHI 1 day average value is: ', XSUSHIprice)
XSUSHI = ['XSUSHI', XSUSHIprice]
allPrices.append(XSUSHI)

# --- UMA

UMAdf = pd.DataFrame(umadata)
#print('\n \n raw data= \n \n', UMAdf)

# remove un-needed data
UMAdf = UMAdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', UMAdf.columns)

#clean up data by splitting list into separate dataframe
UMAdf = pd.DataFrame(UMAdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', UMAdf)

#convert date from unix to date-time so it isn't read in mean calcs.
UMAdf['date'] = pd.to_datetime(UMAdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', UMAdf)

# Calculate the average value by taking the mean of the price column
UMAprice = UMAdf['price'].mean()
print('\n UMA 1 day average value is: ', UMAprice)
UMA = ['UMA', UMAprice]
allPrices.append(UMA)

# --- GTC

GTCdf = pd.DataFrame(gtcdata)
#print('\n \n raw data= \n \n', GTCdf)

# remove un-needed data
GTCdf = GTCdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', GTCdf.columns)

#clean up data by splitting list into separate dataframe
GTCdf = pd.DataFrame(GTCdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', GTCdf)

#convert date from unix to date-time so it isn't read in mean calcs.
GTCdf['date'] = pd.to_datetime(GTCdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', GTCdf)

# Calculate the average value by taking the mean of the price column
GTCprice = GTCdf['price'].mean()
print('\n GTC 1 day average value is: ', GTCprice)
GTC = ['GTC', GTCprice]
allPrices.append(GTC)

# --- DPI

DPIdf = pd.DataFrame(dpidata)
# print('\n \n raw data= \n \n', DPIdf)

# remove un-needed data
DPIdf = DPIdf.drop(['market_caps', 'total_volumes'], axis='columns')
# print('\n \n unnecessary columns dropped from dataset= \n \n', DPIdf.columns)

#clean up data by splitting list into separate dataframe
DPIdf = pd.DataFrame(DPIdf['prices'].tolist(), columns = ['date', 'price'])
# print('\n \n clean up dataset with 2 columns, date and price= \n \n ', DPIdf)

#convert date from unix to date-time so it isn't read in mean calcs.
DPIdf['date'] = pd.to_datetime(DPIdf['date'], unit='ms')
# print('\n \n make date human readable= \n \n', DPIdf)

# Calculate the average value by taking the mean of the price column
DPIprice = DPIdf['price'].mean()
print('\n DPI 1 day average value is: ', DPIprice)
DPI = ['DPI', DPIprice]
allPrices.append(DPI)

# --- INDEX

INDEXdf = pd.DataFrame(indexdata)
#print('\n \n raw data= \n \n', INDEXdf)

# remove un-needed data
INDEXdf = INDEXdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', INDEXdf.columns)

#clean up data by splitting list into separate dataframe
INDEXdf = pd.DataFrame(INDEXdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', INDEXdf)

#convert date from unix to date-time so it isn't read in mean calcs.
INDEXdf['date'] = pd.to_datetime(INDEXdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', INDEXdf)

# Calculate the average value by taking the mean of the price column
INDEXprice = INDEXdf['price'].mean()
print('\n INDEX 1 day average value is: ', INDEXprice)
INDEX = ['INDEX', INDEXprice]
allPrices.append(INDEX)

# --- MUST

MUSTdf = pd.DataFrame(mustdata)
#print('\n \n raw data= \n \n', MUSTdf)

# remove un-needed data
MUSTdf = MUSTdf.drop(['market_caps', 'total_volumes'], axis='columns')
#print('\n \n unnecessary columns dropped from dataset= \n \n', MUSTdf.columns)

#clean up data by splitting list into separate dataframe
MUSTdf = pd.DataFrame(MUSTdf['prices'].tolist(), columns = ['date', 'price'])
#print('\n \n clean up dataset with 2 columns, date and price= \n \n ', MUSTdf)

#convert date from unix to date-time so it isn't read in mean calcs.
MUSTdf['date'] = pd.to_datetime(MUSTdf['date'], unit='ms')
#print('\n \n make date human readable= \n \n', MUSTdf)

# Calculate the average value by taking the mean of the price column
MUSTprice = MUSTdf['price'].mean()
print('\n MUST 1 day average value is: ', MUSTprice)
MUST = ['MUST', MUSTprice]
allPrices.append(MUST)

#--- all prices
# print('\n all prices are: ', allPrices)
priceDF = pd.DataFrame(allPrices, columns = ['Asset', 'price'])
priceDF.to_json('./prices.json',orient='index')
print ('\n Asset prices: \n', priceDF)
