#%%
# import libraries
import pandas as pd

#%%
# # Weather data from meteorological service

#%% 
# read fixed width formatted text file with list of weather stations in DE
# first, extract list of column names (separated by space(s))
cols_stn = pd.read_csv('data/Meteo/DE/wind_hourly/FF_Stundenwerte_Beschreibung_Stationen.txt', sep = r"\s+", nrows = 1).columns.tolist()

#%%
# then, extract the data, skipping first two rows and assigning column names
# encoding used due to presence of accented latin characters (e.g., ü)
df_stn = pd.read_fwf('data/Meteo/DE/wind_hourly/FF_Stundenwerte_Beschreibung_Stationen.txt', encoding = "ISO-8859-1", skiprows = 2, names = cols_stn)
df_stn.dtypes # return data types of each column

#%%
# tanslate column titles to English
df_stn = df_stn.set_axis(['station_id', 'start_date', 'end_date', 'station_height', 'latitude', 'longitude', 'station_name', 'state'], axis = 'columns', inplace = False)

#%%
# filter stations with data between 2018-01-01 and 2018-12-31
df_stn = df_stn.drop(df_stn[(df_stn.start_date > 20180101) | (df_stn.end_date < 20181231)].index)
df_stn # return dataframe

#%%
# convert dtypes for start_date and end_date to datetime
df_stn['start_date'] = pd.to_datetime(df_stn['start_date'], format = "%Y%m%d")
df_stn['end_date'] = pd.to_datetime(df_stn['end_date'], format = "%Y%m%d")
df_stn # return dataframe

#%%
df_stn.dtypes # return data types of each column

#%%
# states with data available
df_stn.state.unique()

#%%
# filter for Schleswig-Holstein
df_sh = df_stn.loc[df_stn['state'] == 'Schleswig-Holstein']
df_sh

#%%
# list of station ids
df_sh['station_id'].tolist()

#%%
# read weather data for station 1200
df_1200 = pd.read_csv('data/Meteo/DE/wind_hourly/Schleswig-Holstein/stundenwerte_FF_01200_20071120_20181231_hist/produkt_ff_stunde_20071120_20181231_01200.txt', sep = ';')
df_1200 # return dataframe
 
#%%
# tanslate column titles to English
df_1200 = df_1200.set_axis(['station_id', 'timestamp_end', 'QLoNC', 'mean_wind_speed', 'mean_wind_direction', 'end_of_record'], axis = 'columns', inplace = False)

#%%
# filter date range for 2018
df_1200 = df_1200.drop(df_1200[(df_1200.timestamp_end < 2018010100) | (df_1200.timestamp_end > 2018123123)].index)
df_1200 # return dataframe

#%%
# convert to datetime
df_1200['timestamp_end'] = pd.to_datetime(df_1200['timestamp_end'], format = "%Y%m%d%H")

#%%
# set end timestamps as index 
df_1200.set_index(['timestamp_end'], inplace = True)
df_1200 # return dataframe

#%% [markdown]
# # Generation data from ENTSO-E Transparency Platform

#%%
# read data from csv
gen_de = pd.read_csv('data/ENTSO-E/DE/DE-AT-LU/Actual Generation per Production Type_201801010000-201901010000.csv')

#%%
# split time in MTU to extract the start and end timestamps (and remove "(CET)") using the '-' delimiter
gen_de['timestamp_start'] = [x.split('-')[0].replace('', '') for x in gen_de['MTU']]
gen_de['timestamp_end'] = [x.split('-')[1].replace(' (CET)', '') for x in gen_de['MTU']]

#%%
# convert timestamps to datetime dtype
gen_de['timestamp_start'] = pd.to_datetime(gen_de['timestamp_start'])
gen_de['timestamp_end'] = pd.to_datetime(gen_de['timestamp_end'])

#%%
# drop unnecessary columns - area and MTU
gen_de = gen_de.drop(columns = ['Area', 'MTU'])

#%%
# set timestamps as index
gen_de.set_index(['timestamp_start'], inplace = True)
gen_de # return dataframe

#%%
# keep only wind data
gen_de = gen_de[['Wind Offshore  - Actual Aggregated [MW]', 'Wind Onshore  - Actual Aggregated [MW]']]

#%%
# rename columns
gen_de = gen_de.set_axis(['wind_ofshore_MW', 'wind_onshore_MW'], axis = 'columns', inplace = False)

#%% [markdown]
# # Merge weather and generation data

#%%
gen_de = gen_de.join(df_1200, how = 'outer')
gen_de # return dataframe

#%%
# drop NaN rows to get hourly data
gen_de = gen_de.dropna()
gen_de

#%%
# drop unnecessary columns
gen_de = gen_de.drop(columns = ['end_of_record', 'QLoNC', 'station_id'])
gen_de
