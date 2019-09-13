# Code sample for accessing Transparency Platform restful API
# Source: https://transparency.entsoe.eu/content/static_content/Static%20content/web%20api/Guide.html#_code_samples
# Install  packages  pip and requests on Python 2 or Python 3
# Download Link to Pip  https://pip.pypa.io/en/latest/installing/#do-i-need-to-install-pip
# Package “request” by executing command “pip install requests”
# Sample Code will be as simple as below:
# **********************
#%%
import requests
url = "https://transparency.entsoe.eu/api?securityToken=TOKEN&documentType=A44&in_Domain=10Y1001A1001A63L&out_Domain=10Y1001A1001A63L&periodStart=201809242300&periodEnd=201809302300"
response = requests.get(url)
data = response.text
print(data)
# **********************


#%%
