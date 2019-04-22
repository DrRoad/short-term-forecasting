#%%
# import libraries
import pandas as pd

#%% 
# read fixed width formatted text file with list of weather stations in DE
# encoding used due to presence of accented characters (e.g., ü)
# first, extract list of column names (separated by space(s))
cols_stn=pd.read_csv('DATA/Meteo/DE/wind_hourly/FF_Stundenwerte_Beschreibung_Stationen.txt',sep=r"\s+",nrows=1).columns.tolist()
# then, extract the data, skipping first two rows and assigning column names
df_stn=pd.read_fwf('DATA/Meteo/DE/wind_hourly/FF_Stundenwerte_Beschreibung_Stationen.txt',encoding="ISO-8859-1",skiprows=2,names=cols_stn)
df_stn 

#%%
