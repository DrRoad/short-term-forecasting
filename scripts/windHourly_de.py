#%%
# import libraries
import pandas as pd
import os, errno
import urllib.request, requests
import glob, zipfile, io
from datetime import datetime, timedelta

#%%
yr = pd.to_datetime(datetime.now().year, format='%Y') # current year; translates to YYYY-01-01 00:00:00

#%%
# define start and end dates (must be within the same year)
start = 2019010100
end = 2019060123

#%%
# convert times to datetime
start = pd.to_datetime(start, format='%Y%m%d%H')
end = pd.to_datetime(end, format='%Y%m%d%H')

#%% 
# hourly wind data repo url
repourl = 'https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/wind/'

#%% 
# read fixed width formatted text file with list of weather stations in DE
# first, extract list of column names (separated by space(s))
if start < yr or end < yr:
  cols_stn = pd.read_csv(str(repourl)+'historical/FF_Stundenwerte_Beschreibung_Stationen.txt', sep=r'\s+', nrows=1).columns.tolist()
else:
  cols_stn = pd.read_csv(str(repourl)+'recent/FF_Stundenwerte_Beschreibung_Stationen.txt', sep=r'\s+', nrows=1).columns.tolist()

#%%
# then, extract the data, skipping first two rows and assigning column names
# encoding used due to presence of accented latin characters (e.g., ü)
if start < yr or end < yr:
  df_stn = pd.read_fwf(str(repourl)+'historical/FF_Stundenwerte_Beschreibung_Stationen.txt', encoding='ISO-8859-1', skiprows=2, names=cols_stn)
else:
  df_stn = pd.read_fwf(str(repourl)+'recent/FF_Stundenwerte_Beschreibung_Stationen.txt', encoding='ISO-8859-1', skiprows=2, names=cols_stn)

#%%
# tanslate column titles to English
df_stn = df_stn.set_axis(['station_id', 'start_date', 'end_date', 'station_height', 'latitude', 'longitude', 'station_name', 'state'], axis='columns', inplace=False)

#%%
# convert dtypes for start_date and end_date to datetime
df_stn['start_date'] = pd.to_datetime(df_stn['start_date'], format='%Y%m%d')
df_stn['end_date'] = pd.to_datetime(df_stn['end_date'], format='%Y%m%d')

#%%
# filter stations with data between start and end dates
df_stn = df_stn.drop(df_stn[(df_stn.start_date>start)|(df_stn.end_date<end)].index)

#%%
# list of states
states = df_stn['state'].unique()
for state in states:
  # create directories to store files for each state if it does not exist
  path = 'data/met/de/wind_hourly/'+str(state).replace(' ', '')
  try:
      os.makedirs(path)
  except OSError as exception:
      if exception.errno != errno.EEXIST:
          raise
      else:
          print ('\nBE CAREFUL! Directory %s already exists.' % path)

  # list of station ids in the state
  df_state = df_stn.loc[df_stn['state']==str(state)]
  station_ids = df_state['station_id'].tolist()
  start_dates = df_state['start_date'].tolist()
  end_dates = df_state['end_date'].tolist()
  stations = list(zip(station_ids, start_dates, end_dates))

  # download and extract data 
  for stn, sd, ed in stations:
    stn = str(stn).zfill(5) # add leading zeros to station ids if less than 5 digits
    dest = str(path)+'/'+str(stn) # file download directory
    if start < yr or end < yr:
      sd_str = sd.strftime('%Y%m%d')
      ed_str = ed.strftime('%Y%m%d')
      if ed_str >= yr.strftime('%Y%m%d'):
        ed_str = (yr - timedelta(days=1)).strftime('%Y%m%d')
      url = str(repourl)+'historical/stundenwerte_FF_'+str(stn)+'_'+str(sd_str)+'_'+str(ed_str)+'_hist.zip' # zip file url for historical data
    else:
      url = str(repourl)+'recent/stundenwerte_FF_'+str(stn)+'_akt.zip' # zip file url for recent data
    
    # download contents of zip file into directory
    try:
      r = requests.get(url)
      z = zipfile.ZipFile(io.BytesIO(r.content))
      z.extractall(dest)
    except zipfile.BadZipFile: # exception if no zip file exists
      print ('No data exists for station '+str(stn)+' in '+str(state))

    # read weather data for station 
    for file in glob.glob(str(dest)+'/produkt*.txt'):
      df_station = pd.read_csv(file, sep=';')

      # tanslate column titles to English
      df_station = df_station.set_axis(['station_id', 'timestamp_end', 'QLoNC', 'mean_wind_speed', 'mean_wind_direction', 'end_of_record'], axis='columns', inplace=False)

      # convert to datetime
      df_station['timestamp_end'] = pd.to_datetime(df_station['timestamp_end'], format='%Y%m%d%H')

      # filter date range for first half of 2019
      df_station = df_station.drop(df_station[(df_station.timestamp_end<start)|(df_station.timestamp_end>end)].index)

      # set end timestamps as index 
      df_station.set_index(['timestamp_end'], inplace=True)
      df_station.to_csv(str(dest)+'/wind_hourly_'+str(stn)+'.csv')
