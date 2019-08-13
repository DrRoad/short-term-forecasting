#%% [markdown]
# # Weather data from German meteorological service

#%%
# import libraries
import pandas as pd

#%%
# set jupyter notebook display options
pd.set_option('display.max_rows', 900) # set up display area to show dataframe
pd.options.display.max_rows # prevent truncation of text strings in columns
pd.set_option('display.max_colwidth', -1)

#%% [markdown]
# ## Solar data

#%%
# read fixed width formatted text file with list of weather stations in DE
# first, extract list of column names (separated by space(s))
cols_stn = pd.read_csv('data/Meteo/DE/solar_hourly/ST_Stundenwerte_Beschreibung_Stationen.txt', sep=r"\s+", nrows=1).columns.tolist()

#%%
# then, extract the data, skipping first two rows and assigning column names
# encoding used due to presence of accented latin characters (e.g., ü)
df_stn = pd.read_fwf('data/Meteo/DE/solar_hourly/ST_Stundenwerte_Beschreibung_Stationen.txt', encoding="ISO-8859-1", skiprows=2, names=cols_stn)
df_stn.dtypes # return data types of each column

#%%
# tanslate column titles to English
df_stn = df_stn.set_axis(['station_id', 'start_date', 'end_date', 'station_height', 'latitude', 'longitude', 'station_name', 'state'], axis='columns', inplace=False)

#%%
# filter stations with data between 2018-01-01 and 2018-12-31
df_stn = df_stn.drop(df_stn[(df_stn.start_date>20180101)|(df_stn.end_date<20181231)].index)

#%%
# convert dtypes for start_date and end_date to datetime
df_stn['start_date'] = pd.to_datetime(df_stn['start_date'], format="%Y%m%d")
df_stn['end_date'] = pd.to_datetime(df_stn['end_date'], format="%Y%m%d")

#%%
# sort data by state
df_stn = df_stn.sort_values(['state'])
df_stn = df_stn.reset_index(drop=True) # reset index
df_stn # return dataframe

#%%
# save as csv
# cp1252 encoding used for latin characters
df_stn.to_csv('data/output/DE_solar_stn_2018.csv', index=None, encoding="cp1252")

#%%
df_stn.dtypes # return data types of each column

#%%
# states with data available
df_stn.state.unique()
