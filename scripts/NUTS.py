#%% [markdown]
# # NUTS (Nomenclature of territorial units for statistics)

#%%
# import libraries
import pandas as pd
pd.set_option('display.max_rows',500) # set up display area to show dataframe
pd.options.display.max_rows # prevent truncation of text strings in columns
pd.set_option('display.max_colwidth',-1)

#%%
# read csv files with NUTS data
nuts=pd.read_csv('data/NUTS/NUTS_AT_2016.csv')
nuts.dtypes # return columns and their datatypes

#%%
# filter for the North Sea region (BE, DE, DK, FR, NL, NO, SE, UK)
nuts=nuts.drop(nuts[~((nuts.CNTR_CODE=='BE')|(nuts.CNTR_CODE=='DE')|(nuts.CNTR_CODE=='DK')|(nuts.CNTR_CODE=='FR')|(nuts.CNTR_CODE=='NL')|(nuts.CNTR_CODE=='NO')|(nuts.CNTR_CODE=='SE')|(nuts.CNTR_CODE=='UK'))].index)

#%%
# sort values by NUTS_ID
nuts=nuts.sort_values(by=['NUTS_ID'])

#%% [markdown]
# ## By country

#%%
# countries
nuts0=nuts.loc[nuts['NUTS_ID'].str.len()==2]
nuts0

#%% [markdown]
# ### Belgium

#%%
be=nuts.loc[nuts['CNTR_CODE']=='BE']

#%%
# NUTS 1
be_nuts1=be.loc[nuts['NUTS_ID'].str.len()==3]
be_nuts1

#%%
# NUTS 2
be_nuts2=be.loc[nuts['NUTS_ID'].str.len()==4]
be_nuts2

#%%
# NUTS 3
be_nuts3=be.loc[nuts['NUTS_ID'].str.len()==5]
be_nuts3

#%% [markdown]
# ### Germany

#%%
de=nuts.loc[nuts['CNTR_CODE']=='DE']

#%%
# NUTS 1
de_nuts1=de.loc[nuts['NUTS_ID'].str.len()==3]
de_nuts1

#%%
# NUTS 2
de_nuts2=de.loc[nuts['NUTS_ID'].str.len()==4]
de_nuts2

#%%
# NUTS 3
de_nuts3=de.loc[nuts['NUTS_ID'].str.len()==5]
de_nuts3

#%% [markdown]
# ### Denmark

#%%
dk=nuts.loc[nuts['CNTR_CODE']=='DK']

#%%
# NUTS 1
dk_nuts1=dk.loc[nuts['NUTS_ID'].str.len()==3]
dk_nuts1

#%%
# NUTS 2
dk_nuts2=dk.loc[nuts['NUTS_ID'].str.len()==4]
dk_nuts2

#%%
# NUTS 3
dk_nuts3=dk.loc[nuts['NUTS_ID'].str.len()==5]
dk_nuts3

#%% [markdown]
# ### France

#%%
fr=nuts.loc[nuts['CNTR_CODE']=='FR']

#%%
# NUTS 1
fr_nuts1=fr.loc[nuts['NUTS_ID'].str.len()==3]
fr_nuts1

#%%
# NUTS 2
fr_nuts2=fr.loc[nuts['NUTS_ID'].str.len()==4]
fr_nuts2

#%%
# NUTS 3
fr_nuts3=fr.loc[nuts['NUTS_ID'].str.len()==5]
fr_nuts3

#%% [markdown]
# ### Netherlands

#%%
nl=nuts.loc[nuts['CNTR_CODE']=='NL']

#%%
# NUTS 1
nl_nuts1=nl.loc[nuts['NUTS_ID'].str.len()==3]
nl_nuts1

#%%
# NUTS 2
nl_nuts2=nl.loc[nuts['NUTS_ID'].str.len()==4]
nl_nuts2

#%%
# NUTS 3
nl_nuts3=nl.loc[nuts['NUTS_ID'].str.len()==5]
nl_nuts3

#%% [markdown]
# ### Norway

#%%
no=nuts.loc[nuts['CNTR_CODE']=='NO']

#%%
# NUTS 1
no_nuts1=no.loc[nuts['NUTS_ID'].str.len()==3]
no_nuts1

#%%
# NUTS 2
no_nuts2=no.loc[nuts['NUTS_ID'].str.len()==4]
no_nuts2

#%%
# NUTS 3
no_nuts3=no.loc[nuts['NUTS_ID'].str.len()==5]
no_nuts3

#%% [markdown]
# ### Sweden

#%%
se=nuts.loc[nuts['CNTR_CODE']=='SE']

#%%
# NUTS 1
se_nuts1=se.loc[nuts['NUTS_ID'].str.len()==3]
se_nuts1

#%%
# NUTS 2
se_nuts2=se.loc[nuts['NUTS_ID'].str.len()==4]
se_nuts2

#%%
# NUTS 3
se_nuts3=se.loc[nuts['NUTS_ID'].str.len()==5]
se_nuts3

#%% [markdown]
# ### United Kingdom

#%%
uk=nuts.loc[nuts['CNTR_CODE']=='UK']

#%%
# NUTS 1
uk_nuts1=uk.loc[nuts['NUTS_ID'].str.len()==3]
uk_nuts1

#%%
# NUTS 2
uk_nuts2=uk.loc[nuts['NUTS_ID'].str.len()==4]
uk_nuts2

#%%
# NUTS 3
uk_nuts3=uk.loc[nuts['NUTS_ID'].str.len()==5]
uk_nuts3

#%%
# save nuts to csv
# encoding used for latin characters
nuts.to_csv('data/NUTS/NUTS_NS_2016.csv',index=None,encoding="cp1252")

#%%
