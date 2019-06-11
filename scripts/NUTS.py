#%% [markdown]
# # Nomenclature of territorial units for statistics (NUTS)

#%%
# import libraries
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',500) # set up display area to show dataframe
pd.options.display.max_rows # prevent truncation of text strings in columns
pd.set_option('display.max_colwidth',-1)

#%%
# read csv files with NUTS data
nuts=pd.read_csv('data/NUTS/NUTS_AT_2016.csv')
nuts.dtypes # return columns and their datatypes

#%% [markdown]
# ## North Sea region

#%%
# filter for the North Sea region (BE, DE, DK, FR, NL, NO, SE, UK)
nuts=nuts.drop(nuts[~((nuts.CNTR_CODE=='BE')|(nuts.CNTR_CODE=='DE')|(nuts.CNTR_CODE=='DK')|(nuts.CNTR_CODE=='FR')|(nuts.CNTR_CODE=='NL')|(nuts.CNTR_CODE=='NO')|(nuts.CNTR_CODE=='SE')|(nuts.CNTR_CODE=='UK'))].index)

#%%
# sort values by NUTS_ID
nuts=nuts.sort_values(by=['NUTS_ID'])

#%%
# countries (NUTS 0) - code has two characters
nuts0=nuts.loc[nuts['NUTS_ID'].str.len()==2].copy()
nuts0

#%%
# number of NUTS 0 territories
len(nuts0)

#%%
# NUTS 1 - code has three characters
nuts1=nuts.loc[nuts['NUTS_ID'].str.len()==3].copy()

#%%
# NUTS 2 - code has four characters
nuts2=nuts.loc[nuts['NUTS_ID'].str.len()==4].copy()

#%%
# NUTS 3 - code has five characters
nuts3=nuts.loc[nuts['NUTS_ID'].str.len()==5].copy()

#%% [markdown]
# ## North Sea region - by country

#%% [markdown]
# ### Belgium

#%%
# filter for BE
be=nuts.loc[nuts['CNTR_CODE']=='BE'].copy()

#%%
# NUTS 1
be_nuts1=be.loc[nuts['NUTS_ID'].str.len()==3].copy()
be_nuts1

#%%
# number of NUTS 1 territories
len(be_nuts1)

#%%
# NUTS 2
be_nuts2=be.loc[nuts['NUTS_ID'].str.len()==4].copy()
be_nuts2

#%%
# number of NUTS 2 territories
len(be_nuts2)

#%%
# NUTS 3
be_nuts3=be.loc[nuts['NUTS_ID'].str.len()==5].copy()
be_nuts3

#%%
# number of NUTS 3 territories
len(be_nuts3)

#%% [markdown]
# ### Germany

#%%
# filter for DE
de=nuts.loc[nuts['CNTR_CODE']=='DE'].copy()

#%%
# NUTS 1
de_nuts1=de.loc[nuts['NUTS_ID'].str.len()==3].copy()
de_nuts1

#%%
# number of NUTS 1 territories
len(de_nuts1)

#%%
# NUTS 2
de_nuts2=de.loc[nuts['NUTS_ID'].str.len()==4].copy()
de_nuts2

#%%
# number of NUTS 2 territories
len(de_nuts2)

#%%
# NUTS 3
de_nuts3=de.loc[nuts['NUTS_ID'].str.len()==5].copy()
de_nuts3

#%%
# number of NUTS 3 territories
len(de_nuts3)

#%% [markdown]
# ### Denmark

#%%
# filter for DK
dk=nuts.loc[nuts['CNTR_CODE']=='DK'].copy()

#%%
# NUTS 1
dk_nuts1=dk.loc[nuts['NUTS_ID'].str.len()==3].copy()
dk_nuts1

#%%
# number of NUTS 1 territories
len(dk_nuts1)

#%%
# NUTS 2
dk_nuts2=dk.loc[nuts['NUTS_ID'].str.len()==4].copy()
dk_nuts2

#%%
# number of NUTS 2 territories
len(dk_nuts2)

#%%
# NUTS 3
dk_nuts3=dk.loc[nuts['NUTS_ID'].str.len()==5].copy()
dk_nuts3

#%%
# number of NUTS 3 territories
len(dk_nuts3)

#%% [markdown]
# ### France

#%%
# filter for FR
fr=nuts.loc[nuts['CNTR_CODE']=='FR'].copy()

#%%
# NUTS 1
fr_nuts1=fr.loc[nuts['NUTS_ID'].str.len()==3].copy()
fr_nuts1

#%%
# drop entries corresponding to "RUP FR - RÉGIONS ULTRAPÉRIPHÉRIQUES FRANÇAISES" (FRY) - French Overseas Territories
fr=fr[~fr.NUTS_ID.str.contains("FRY")]
nuts=nuts[~nuts.NUTS_ID.str.contains("FRY")]
nuts2=nuts2[~nuts2.NUTS_ID.str.contains("FRY")]
nuts3=nuts3[~nuts3.NUTS_ID.str.contains("FRY")]
fr_nuts1=fr_nuts1[~fr_nuts1.NUTS_ID.str.contains("FRY")]

#%%
# number of NUTS 1 territories
len(fr_nuts1)

#%%
# NUTS 2
fr_nuts2=fr.loc[nuts['NUTS_ID'].str.len()==4].copy()
fr_nuts2

#%%
# number of NUTS 2 territories
len(fr_nuts2)

#%%
# NUTS 3
fr_nuts3=fr.loc[nuts['NUTS_ID'].str.len()==5].copy()
fr_nuts3

#%%
# number of NUTS 3 territories
len(fr_nuts3)

#%% [markdown]
# ### Netherlands

#%%
# filter for NL
nl=nuts.loc[nuts['CNTR_CODE']=='NL'].copy()

#%%
# NUTS 1
nl_nuts1=nl.loc[nuts['NUTS_ID'].str.len()==3].copy()
nl_nuts1

#%%
# number of NUTS 1 territories
len(nl_nuts1)

#%%
# NUTS 2
nl_nuts2=nl.loc[nuts['NUTS_ID'].str.len()==4].copy()
nl_nuts2

#%%
# number of NUTS 2 territories
len(nl_nuts2)

#%%
# NUTS 3
nl_nuts3=nl.loc[nuts['NUTS_ID'].str.len()==5].copy()
nl_nuts3

#%%
# number of NUTS 3 territories
len(nl_nuts3)

#%% [markdown]
# ### Norway

#%%
# filter for NO
no=nuts.loc[nuts['CNTR_CODE']=='NO'].copy()

#%%
# NUTS 1
no_nuts1=no.loc[nuts['NUTS_ID'].str.len()==3].copy()
no_nuts1

#%%
# number of NUTS 1 territories
len(no_nuts1)

#%%
# NUTS 2
no_nuts2=no.loc[nuts['NUTS_ID'].str.len()==4].copy()
no_nuts2

#%%
# number of NUTS 2 territories
len(no_nuts2)

#%%
# NUTS 3
no_nuts3=no.loc[nuts['NUTS_ID'].str.len()==5].copy()
no_nuts3

#%%
# number of NUTS 3 territories
len(no_nuts3)

#%% [markdown]
# ### Sweden

#%%
# filter for SE
se=nuts.loc[nuts['CNTR_CODE']=='SE'].copy()

#%%
# NUTS 1
se_nuts1=se.loc[nuts['NUTS_ID'].str.len()==3].copy()
se_nuts1

#%%
# number of NUTS 1 territories
len(se_nuts1)

#%%
# NUTS 2
se_nuts2=se.loc[nuts['NUTS_ID'].str.len()==4].copy()
se_nuts2

#%%
# number of NUTS 2 territories
len(se_nuts2)

#%%
# NUTS 3
se_nuts3=se.loc[nuts['NUTS_ID'].str.len()==5].copy()
se_nuts3

#%%
# number of NUTS 3 territories
len(se_nuts3)

#%% [markdown]
# ### United Kingdom

#%%
# filter for UK
uk=nuts.loc[nuts['CNTR_CODE']=='UK'].copy()

#%%
# NUTS 1
uk_nuts1=uk.loc[nuts['NUTS_ID'].str.len()==3].copy()
uk_nuts1

#%%
# number of NUTS 1 territories
len(uk_nuts1)

#%%
# NUTS 2
uk_nuts2=uk.loc[nuts['NUTS_ID'].str.len()==4].copy()
uk_nuts2

#%%
# number of NUTS 2 territories
len(uk_nuts2)

#%%
# NUTS 3
uk_nuts3=uk.loc[nuts['NUTS_ID'].str.len()==5].copy()
uk_nuts3

#%%
# number of NUTS 3 territories
len(uk_nuts3)

#%% [markdown]
# ## Save North Sea NUTS data as csv file

#%%
# cp1252 encoding used for latin characters
nuts.to_csv('data/output/NUTS_NS_2016.csv',index=None,encoding="cp1252")

#%% [markdown]
# ## Number of NUTS 1, 2 and 3 territories in the North Sea region (excluding French Overseas Territories)

#%%
# number of NUTS 1 territories
len(nuts1)

#%%
# number of NUTS 2 territories
len(nuts2)

#%%
# number of NUTS 3 territories
len(nuts3)