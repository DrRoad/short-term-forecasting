#%%
# import libraries
import pandas as pd
import os, errno
import requests, glob, zipfile, io
from datetime import datetime, timedelta

#%%
# define start and end dates of data (must be from the same year)
start = 2019010100 # year, month, day, hour
end = 2019060123

#%%
# current year; translates to YYYY-01-01 00:00:00
yr = pd.to_datetime(datetime.now().year, format='%Y') 

#%%
# convert times to datetime
start = pd.to_datetime(start, format='%Y%m%d%H')
end = pd.to_datetime(end, format='%Y%m%d%H')

#%% 
# hourly solar data repo url
repourl = 'https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/solar/'

#%% 
# read fixed width formatted text file with list of weather stations in DE
# first, extract list of column names (separated by space(s))
cols_stn = pd.read_csv(str(repourl)+'ST_Stundenwerte_Beschreibung_Stationen.txt', sep=r'\s+', nrows=1).columns.tolist() 

#%%
# then, extract the data, skipping first two rows and assigning column names
# encoding used due to presence of accented latin characters (e.g., ü)
df_stn = pd.read_fwf(str(repourl)+'ST_Stundenwerte_Beschreibung_Stationen.txt', encoding='ISO-8859-1', skiprows=2, names=cols_stn)

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
  # create directories to store files for each state if they do not exist
  path = 'data/met/de/solar_hourly/'+str(state).replace(' ', '')
  try:
      os.makedirs(path)
  except OSError as exception:
      if exception.errno != errno.EEXIST:
          raise
      else:
          print ('\nBE CAREFUL! Directory %s already exists.' % path)

  # list of station ids in the state
  df_state = df_stn.loc[df_stn['state']==str(state)]
  stations = df_state['station_id'].tolist()

  # download and extract data 
  for stn in stations:
    stn = str(stn).zfill(5) # add leading zeros to station ids if less than 5 digits
    dest = str(path)+'/'+str(stn) # file download directory
    url = str(repourl)+'stundenwerte_ST_'+str(stn)+'_row.zip' # zip file url
    
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
      df_station = df_station.set_axis(['station_id', 'timestamp_end', 'QLoNC', 'longwave_downward_radiation', 'diffuse_radiation', 'incoming_radiation', 'sunshine_duration', 'zenith_angle', 'end_of_interval', 'end_of_record'], axis='columns', inplace=False)

      # convert to datetime
      df_station['timestamp_end'] = pd.to_datetime(df_station['timestamp_end'], format='%Y%m%d%H')

      # filter for date range
      df_station = df_station.drop(df_station[(df_station.timestamp_end<start)|(df_station.timestamp_end>end)].index)

      # set end timestamps as index 
      df_station.set_index(['timestamp_end'], inplace=True)
      df_station.to_csv(str(dest)+'/solar_hourly_'+str(stn)+'.csv')
