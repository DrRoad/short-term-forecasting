#%% [markdown]
# # Nomenclature of territorial units for statistics (NUTS) with market bidding zones

#%%
# import libraries
import pandas as pd
import numpy as np

#%%
# set jupyter notebook display options
pd.set_option('display.max_rows', 900) # set up display area to show dataframe
pd.options.display.max_rows # prevent truncation of text strings in columns
pd.set_option('display.max_colwidth', -1)

#%%
# read csv files with NUTS data
nuts = pd.read_csv('data/nuts/NUTS_NS_2016.csv', encoding="cp1252")

#%%
# sort values by NUTS_ID
nuts = nuts.sort_values(['NUTS_ID'])

#%%
# NUTS 3 - code has five characters
nuts3 = nuts.loc[nuts['NUTS_ID'].str.len()==5].copy()

#%% [markdown]
# ## Bidding areas

#%% [markdown]
# ### Belgium

#%%
nuts3.loc[nuts3['CNTR_CODE'].str.contains("BE"), 'BIDDING_ZONE'] = "BE"

#%% [markdown]
# ### Germany

#%%
nuts3.loc[nuts3['CNTR_CODE'].str.contains("DE"), 'BIDDING_ZONE'] = "DE-LU"

#%% [markdown]
# ### Denmark

#%%
# DK1 (western DK) - Syddanmark (DK03), Midtjylland (DK04), Nordjylland (DK05)
nuts3.loc[nuts3['NUTS_ID'].str.contains("DK03|DK04|DK05"), 'BIDDING_ZONE'] = "DK1"

#%%
# DK2 (eastern DK) - Sjælland (DK02), Hovedstaden (DK01)
nuts3.loc[nuts3['NUTS_ID'].str.contains("DK01|DK02"), 'BIDDING_ZONE'] = "DK2"

#%% [markdown]
# ### France

#%%
nuts3.loc[nuts3['CNTR_CODE'].str.contains("FR"), 'BIDDING_ZONE'] = "FR"

#%% [markdown]
# ### Netherlands

#%%
nuts3.loc[nuts3['CNTR_CODE'].str.contains("NL"), 'BIDDING_ZONE'] = "NL"

#%% [markdown]
# ### Norway

#%%
# NO1 - Oslo (Oslo, Akershus, Hedmark, Oppland, Østfold, Buskerud, Vestfold, Telemark)
nuts3.loc[nuts3['NUTS_ID'].str.contains("NO01|NO02|NO03"), 'BIDDING_ZONE'] = "NO1"

#%%
# NO2 - Kristiansand (Aust-Agder, Vest-Agder, Rogaland)
nuts3.loc[nuts3['NUTS_ID'].str.contains("NO04"), 'BIDDING_ZONE'] = "NO2"

#%%
# NO3 - Trondheim, Molde (Trøndelag, Sogn og Fjordane, Møre og Romsdal)
nuts3.loc[nuts3['NUTS_ID'].str.contains("NO052|NO053|NO06"), 'BIDDING_ZONE'] = "NO3"

#%%
# NO4 - Tromsø (Troms, Nordland, Finnmark)
nuts3.loc[nuts3['NUTS_ID'].str.contains("NO07"), 'BIDDING_ZONE'] = "NO4"

#%%
# NO5 - Bergen (Hordaland)
nuts3.loc[nuts3['NUTS_ID'].str.contains("NO051"), 'BIDDING_ZONE'] = "NO5"

#%% [markdown]
# ### Sweden

#%%
# SE1 - Luleå (BD: Norrbotten)
nuts3.loc[nuts3['NUTS_ID'].str.contains("SE332"), 'BIDDING_ZONE'] = "SE1"

#%%
# SE2 - Sundsvall (AC: Västerbotten, Z: Jämtland, Y: Västernorrland, X: Gävleborg)
nuts3.loc[nuts3['NUTS_ID'].str.contains("SE331|SE322|SE321|SE313"), 'BIDDING_ZONE'] = "SE2"

#%%
# SE3 - Stockholm (W: Dalarna, C: Uppsala, AB: Stockholm, U: Västmanland, D: Södermanland, T: Örebro, S: Värmland, O: Västra Götaland, F: Jönköping, E: Östergötland, I: Gotland)
nuts3.loc[nuts3['NUTS_ID'].str.contains("SE311|SE124|SE125|SE312|SE121|SE110|SE122|SE214|SE232|SE123|SE211"), 'BIDDING_ZONE'] = "SE3"

#%%
# SE4 - Malmö (N: Halland, G: Kronoberg, H: Kalmar, M: Skåne, K: Blekinge)
nuts3.loc[nuts3['NUTS_ID'].str.contains("SE213|SE231|SE212|SE224|SE221"), 'BIDDING_ZONE'] = "SE4"

#%% [markdown]
# ### United Kingdom

#%%
# GB - Great Britain
nuts3.loc[nuts3['NUTS_ID'].str.contains("UKC|UKD|UKE|UKF|UKG|UKH|UKI|UKJ|UKK|UKL|UKM"), 'BIDDING_ZONE'] = "GB"

#%%
# IE-SEM - Northern Ireland
nuts3.loc[nuts3['NUTS_ID'].str.contains("UKN"), 'BIDDING_ZONE'] = "IE-SEM"

#%% [markdown]
# ## Save North Sea NUTS 3 data with bidding zones as csv file

#%%
# cp1252 encoding used for latin characters
nuts3.to_csv('data/nuts/NUTS3_BIDDING.csv', index=None, encoding="cp1252")

#%%
nuts3 = nuts3.reset_index(drop=True) # reset index
# NUTS 3
nuts3
