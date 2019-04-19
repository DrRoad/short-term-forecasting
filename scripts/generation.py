#%%
# import libraries
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

#%%
# plot styles
plt.style.use(['Solarize_Light2']) # customising plot styles
# customise facecolor of figures
plt.rcParams['figure.facecolor']='#FDF6E3' # inline output
plt.rcParams['savefig.facecolor']='#FDF6E3' # pdf

#%%
# read generation csv data file for NL and save as dataframe
gen_nl=pd.read_csv('DATA/ENTSO-E/NL/NL/Actual Generation per Production Type_201801010000-201901010000.csv')

#%%
# print data types of each column in dataframe
gen_nl.dtypes

#%%
# split time in MTU to extract the start and end timestamps (and remove "(CET)") using the '-' delimiter
gen_nl['Timestamp - Start']=[x.split('-')[0].replace('','') for x in gen_nl['MTU']]
gen_nl['Timestamp - End']=[x.split('-')[1].replace(' (CET)','') for x in gen_nl['MTU']]

#%%
# convert timestamps to datetime dtype
gen_nl['Timestamp - Start']=pd.to_datetime(gen_nl['Timestamp - Start'])
gen_nl['Timestamp - End']=pd.to_datetime(gen_nl['Timestamp - End'])

#%% 
# drop unwanted columns - area and MTU
gen_nl=gen_nl.drop(columns=['Area','MTU'])

#%%
# set timestamps as index
gen_nl.set_index(['Timestamp - Start','Timestamp - End'],inplace=True)