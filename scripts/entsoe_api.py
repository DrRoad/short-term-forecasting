#%% [markdown]
# # Extracting data from ENTSO-E Transparency Platform's Restful API
# Source: https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_code_samples

#%%
# import libraries
import requests

#%%
# import security token saved in a separate file (login.py)
import login

#%%
# define attributes 
## Art. 16.1.b&c Aggregated generation per type
document_type = 'A75' # document type - actual generation per type
process_type = 'A16' # process type
period_start = '201809240000' # period start
period_end = '201809250000' # period end
bidding_zone = '10YBE----------2' # domain / area EIC code - Belgium (BE)

#%%
url = "https://transparency.entsoe.eu/api?securityToken="+str(login.token)+"&documentType="+str(document_type)+"&processType="+str(process_type)+"&periodStart="+str(period_start)+"&periodEnd="+str(period_end)+"&in_Domain="+str(bidding_zone)
response = requests.get(url)
data = response.text
print(data)


#%%
