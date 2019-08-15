<!-- 
- [Data](#Data)
  - [Folder navigation](#Folder-navigation)
  - [Generation and demand data](#Generation-and-demand-data)
  - [Market data](#Market-data)
  - [Meteorological data](#Meteorological-data)
  - [Other data](#Other-data)
  - [Terms of use](#Terms-of-use)
 -->


# Data

All input and output data can be found in the [data](https://www.dropbox.com/sh/vjo4gkfk6dlye6h/AAAQNltY7-Y4N9SQYjGZDHY5a?dl=0) folder on Dropbox. Licenses and terms of the input data used can be found in their corresponding folders within the folder.


## Folder navigation

* ENTSO-E 
  * generation and load data for each bidding zone in the North Sea region, grouped by country
* Meteo - meteorological data, grouped by country
* Market - market data for the North Sea region
* NUTS - territorial units
* output - output or modified data from this project


## Generation and demand data

Generation and demand data for each bidding zone are downloaded from the [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/). The following descriptions of the data are from ENTSO-E Transparency Platform's [Knowledge Base](https://transparency.entsoe.eu/content/static_content/Static%20content/knowledge%20base/knowledge%20base.html).

#### [Actual Generation per Production Type](https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show)

- Actual aggregated net generation output (MW) per market time unit and per production type
- Published no later than one hour after the operational period
- Computed as the average of all available instantaneous net generation output values on each market time unit
- If unknown, it is estimated 
- The actual generation of small-scale units might be estimated if no real-time measurement devices exist

#### [Production and Generation Units](https://transparency.entsoe.eu/generation/r2/productionAndGenerationUnits/show)

The knowledge base did not provide any information about this data.

Based on available information, the data describes the production and generation units, including their code, name, validity dates, status (commissioned, decommissioned or cancelled), type (e.g., fossil gas, wind offshore), location, installed capacity (MW) and voltage. 

<!-- The data on [Installed Capacity Per Production Unit](https://transparency.entsoe.eu/generation/r2/installedCapacityPerProductionUnit/show) includes only power plants with an installed generation capacity equalling to or exceeding 100 MW. This is assumed to also apply for the Production and Generating Units data. -->

The codes for production unit types in the downloaded data (cross-referenced with the tables rendered on the transparency platform):

- B01: Biomass
- B02: Fossil brown coal / lignite
- B03: Fossil coal-derived gas
- B04: Fossil gas
- B05: Fossil hard coal
- B06: Fossil oil
- B07: Fossil oil shale
- B08: Fossil peat 
- B09: Geothermal
- B10: Hydro pumped storage
- B11: Hydro run-of-river and poundage
- B12: Hydro water reservoir
- B13: Marine
- B14: Nuclear
- B15: Other renewable
- B16: Solar
- B17: Waste
- B18: Wind offshore
- B19: Wind onshore
- B20: Other

#### [Installed Capacity Per Production Unit](https://transparency.entsoe.eu/generation/r2/installedCapacityPerProductionUnit/show)

Information about production units (existing and planned) with an installed generation capacity equalling to or exceeding 100 MW. The information shall contain:

- the unit name
- the installed net generation capacity (MW)
- the location
- the voltage connection levels
- the bidding zone
- the control area
- the production type
- the commissioning date (when available)
- the decommissioning date (when available)

<!-- Note: The definitions of the commissioning and decommissioning date are out of scope for TSOs and, in order to ensure qualitative data publications, it shall be drafted by NRAs in coordination with primary owners of the data taking into account the ongoing discussions. -->

The information shall be published annually for the three following years no later than one week before the beginning of the first year to which the data refers. Information should refer to January 1st of each year for the 3 following years.

#### [Installed Capacity per Production Type](https://transparency.entsoe.eu/generation/r2/installedGenerationCapacityAggregation/show)

The sum of installed net generation capacity (MW) per control area for all existing production units equalling to or exceeding 1 MW installed generation capacity, per production type. The information shall be published annually no later than one week before the end of the previous year. The installed net generation capacity refers to to the generation capacity which is effectively installed on January 1st of the following year.

**Incomplete data**: 

- Data for Sweden is unavailable at the bidding zone level for 2018 and 2019 (last checked on 15/08/2019)

#### [Total Load - Day Ahead / Actual](https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show)

- Actual total load per bidding zone per market time unit
- The total load is defined as equal to the sum of power generated by plants on both TSO/DSO networks, from which is deduced:
  - the balance (export-import) of exchanges on interconnections between neighbouring bidding zones
  - the power absorbed by energy storage resources
- The information is published no later than one hour after the end of the operating period
- Calculated using the average of real-time load values per bidding zone per market time unit
- Actual total Load (including losses without stored energy) = Net Generation – Exports + Imports – Absorbed Energy
- Net generation is preferred, but gross generation could be used where it is available with the better precision
- TSOs should decide gross or net generation will be used but the net/gross characteristic should be consistent per bidding zone
- Absorbed energy is also provided as separate information with the aggregated generation output of the hydro pumped storage
- The physical flow on the tie line is measured as agreed by neighbouring TSOs or bidding zones, where applicable

## Market data

[Nord Pool](https://www.nordpoolgroup.com/historical-market-data/)

* [Membership list - Nord Pool](https://www.nordpoolgroup.com/trading/join-our-markets/membership/)
* [Terms and conditions for use](https://www.nordpoolgroup.com/About-us/Terms-and-conditions-for-use/)

[EPEX Spot](https://www.epexspot.com/en/extras/download-center/market_data)

* [EPEX SPOT Exchange Members](https://www.epexspot.com/en/membership/list_of_members)


## Meteorological data 

#### Belgium

[The Royal Meteorological Institute of Belgium](https://opendata.meteo.be/)

#### Germany

[Deutscher Wetterdienst](https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html)

* [CDC (Climate Data Center) portal](https://cdc.dwd.de/portal/)
* [CDC OpenData](https://opendata.dwd.de/climate_environment/CDC/)
* Data set descriptions
  * [Hourly station observations of air temperature at 2 m above ground in °C for Germany](https://cdc.dwd.de/sdi/pid/TT_TU_MN009/DESCRIPTION_TT_TU_MN009_en.pdf)
  * [Hourly station observations of relative humidity in % for Germany](https://cdc.dwd.de/sdi/pid/RF_TU_MN009/DESCRIPTION_RF_TU_MN009_en.pdf)
  * [Hourly station observations of precipitation amount in mm for Germany](https://cdc.dwd.de/sdi/pid/R1_MN008/DESCRIPTION_R1_MN008_en.pdf)
  * [Hourly station observations of form of precipitation (WR code) for Germany](https://cdc.dwd.de/sdi/pid/WRTR_MN008/DESCRIPTION_WRTR_MN008_en.pdf)
  * [Hourly station observations of index whether precipitation has fallen for Germany](https://cdc.dwd.de/sdi/pid/RS_IND_MN008/DESCRIPTION_RS_IND_MN008_en.pdf)
  * [Hourly mean of station observations of wind speed ca. 10 m above ground in m/s for Germany](https://cdc.dwd.de/sdi/pid/F_MN003/DESCRIPTION_F_MN003_en.pdf)
  * [Hourly mean of station observations of wind direction at ca. 10 m above ground in degree for Germany](https://cdc.dwd.de/sdi/pid/D_MN003/DESCRIPTION_D_MN003_en.pdf)
  * [Hourly station observations of air pressure at station level in hpa for Germany](https://cdc.dwd.de/sdi/pid/P0_MN008/DESCRIPTION_P0_MN008_en.pdf)
  * [Hourly station observations of air pressure at mean sea level in hpa for Germany](https://cdc.dwd.de/sdi/pid/P_MN008/DESCRIPTION_P_MN008_en.pdf)
  * [Hourly station observations of cloud coverage in eighths for Germany](https://cdc.dwd.de/sdi/pid/N_MN008/DESCRIPTION_N_MN008_en.pdf)
* [Hourly wind data](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/wind/)

#### Denmark

[Danish Meteorological Institute](http://research.dmi.dk/data/)

#### France

[Météo-France](https://donneespubliques.meteofrance.fr/)

#### Netherlands

[Royal Netherlands Meteorological Institute](https://data.knmi.nl/datasets)

#### Norway

[Norwegian Meteorological Institute](https://www.met.no/en/free-meteorological-data)

#### Sweden

[Swedish Meteorological and Hydrological Institute](https://www.smhi.se/en/services/professional-services/data-and-statistics)

#### United Kingdom

[Met Office](https://www.metoffice.gov.uk/datapoint)


## Other data

[NUTS (Nomenclature of territorial units for statistics)](https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts)


## Terms of use

#### Deutscher Wetterdienst

* [Terms of use for data on the CDC ftp server](https://opendata.dwd.de/climate_environment/CDC/Terms_of_use.pdf)

#### ENTSO-E Transparency Platform

* [GENERAL TERMS AND CONDITIONS FOR THE USE OF THE ENTSO-E TRANSPARENCY PLATFORM](https://docstore.entsoe.eu/Documents/MC%20documents/Transparency%20Platform/ENTSOE_Transparency_Terms_Conditions.pdf)
* [LIST OF DATA AVAILABLE FOR FREE RE-USE](https://docstore.entsoe.eu/Documents/MC%20documents/Transparency%20Platform/List_of_Data_available_for_reuse.pdf)
