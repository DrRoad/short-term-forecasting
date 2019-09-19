#%%
# import libraries
import pandas as pd
import os, errno
import urllib.request
import requests, zipfile, io

#%% 
# weather data from meteorological service
# read fixed width formatted text file with list of weather stations in DE
# first, extract list of column names (separated by space(s))
cols_stn = pd.read_csv('https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/solar/ST_Stundenwerte_Beschreibung_Stationen.txt', sep=r"\s+", nrows=1).columns.tolist()

#%%
# then, extract the data, skipping first two rows and assigning column names
# encoding used due to presence of accented latin characters (e.g., ü)
df_stn = pd.read_fwf('https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/solar/ST_Stundenwerte_Beschreibung_Stationen.txt', encoding="ISO-8859-1", skiprows=2, names=cols_stn)

#%%
# tanslate column titles to English
df_stn = df_stn.set_axis(['station_id', 'start_date', 'end_date', 'station_height', 'latitude', 'longitude', 'station_name', 'state'], axis='columns', inplace=False)

#%%
# filter stations with data between 2018-01-01 and 2018-12-31
df_stn = df_stn.drop(df_stn[(df_stn.start_date>20190101)|(df_stn.end_date<20190601)].index)

#%%
# convert dtypes for start_date and end_date to datetime
df_stn['start_date'] = pd.to_datetime(df_stn['start_date'], format="%Y%m%d")
df_stn['end_date'] = pd.to_datetime(df_stn['end_date'], format="%Y%m%d")

#%%
# list of states
states = df_stn['state'].unique()
for state in states:
  # create directories to store files for each state if it does not exist
  path = "data/met/de/solar_hourly/"+str(state).replace(" ", "")
  try:
      os.makedirs(path)
  except OSError as exception:
      if exception.errno != errno.EEXIST:
          raise
      else:
          print ("\nBE CAREFUL! Directory %s already exists." % path)
  # list of station ids in the state
  df_state = df_stn.loc[df_stn['state']==str(state)]
  stations = df_state['station_id'].tolist()

#%%
  # download and extract data 
  for station in stations:
    station = str(station).zfill(5) # add leading zeros to station ids if less than 5 digits
    url = "https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/solar/stundenwerte_ST_"+str(station)+"_row.zip" # zip file url
    dest = "data/met/de/solar_hourly/"+str(state).replace(" ", "")+"/"+str(station) # file download directory

    # download contents of zip file into directory
    try:
      r = requests.get(url)
      z = zipfile.ZipFile(io.BytesIO(r.content))
      z.extractall(dest)
    except zipfile.BadZipFile: # exception if no zip file exists
      print ("No data exists for station "+str(station)+" in "+str(state))
