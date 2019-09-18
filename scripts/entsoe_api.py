#%% 
# # Extracting data from ENTSO-E Transparency Platform's Restful API
# https://github.com/EnergieID/entsoe-py

#%%
# import libraries
from entsoe import EntsoePandasClient
import pandas as pd

#%%
# import security token saved in a separate file (login.py)
import login

#%%
# use security token to access the api through the entsoe pandas client
client = EntsoePandasClient(api_key=login.token)

#%%
# define attributes for the data to be extracted
# timestamps for the first half of 2019
start = pd.Timestamp('20190101', tz='Europe/Brussels') 
end = pd.Timestamp('20190601', tz='Europe/Brussels')

#%%
# list of bidding zones in the North Sea region
bz_ns = ['BE', 'DE-LU', 'DK-1', 'DK-2', # Belgium, Germany + Luxembourg, Denmark 
          'FR', 'GB', 'IE-SEM', 'NL', # France, United Kingdom (Great Britain + (Northern) Ireland), Netherlands
          'NO-1', 'NO-2', 'NO-3', 'NO-4', 'NO-5', # Norway
          'SE-1', 'SE-2', 'SE-3', 'SE-4'] # Sweden

#%%
# extracting data for each bidding zone in a loop
for country_code in bz_ns:
  # create a pandas dataframe for the generation data with the above attributes
  ts_gen = client.query_generation(country_code, start=start, end=end, psr_type=None, lookup_bzones=True)
  # save as csv 
  ts_gen.to_csv('data/entsoe_api/generation_'+str(country_code)+'.csv')
