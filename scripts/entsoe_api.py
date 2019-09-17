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
start = pd.Timestamp('20171201', tz='Europe/Brussels')
end = pd.Timestamp('20180101', tz='Europe/Brussels')
country_code = 'DK-1'  # bidding zone or domain

#%%
# create a pandas dataframe for the generation data with the above attributes
ts_gen = client.query_generation(country_code, start=start, end=end, psr_type=None, lookup_bzones=True) # lookup_bzones=True if using bidding zone instead of domain

#%%
