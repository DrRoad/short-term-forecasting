<!--  
- [Background](#background)
- [Regions](#regions)
  - [North Sea countries](#north-sea-countries)
    - [NUTS (Nomenclature of territorial units for statistics)](#nuts-nomenclature-of-territorial-units-for-statistics)
  - [Bidding zones](#bidding-zones)
    - [Definition](#definition)
    - [Bidding zones in the North Sea region](#bidding-zones-in-the-north-sea-region)
- [Data](#data)
  - [Data folder navigation](#data-folder-navigation)
  - [Met data](#met-data)
  - [Generation and demand data](#generation-and-demand-data)
  - [Market data](#market-data)
  - [Other data](#other-data)
- [Methodology](#methodology)
  - [Modelling framework](#modelling-framework)
- [References](#references)
-->

Welcome to the [short-term-forecasting](https://github.com/ENSYSTRA/short-term-forecasting) wiki! 

Short-term forecasting of electricity generation, demand and prices using machine learning.

Copyright (C)  2019  Nithiya Streethran.

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.3 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".

Images are licensed under the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license, where the image source has not been specified.

This work is part of Nithiya Streethran's research as Early-Stage Researcher (ESR) 9 of the [ENSYSTRA - ENergy SYStems in TRAnsition](https://ensystra.eu/) Innovative Training Network. ENSYSTRA is funded by the European Union's Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No: 765515.

# Background

The transition towards a future low-carbon economy is driven globally by the Paris Agreement [[par2015]](#par2015), which recognises the need for sustainable development worldwide to counter the threats of climate change. The European Union (EU) is committed to reduce greenhouse gas (GHG) emissions by 2050 to 80-90 % below 1990 levels [[ene2012]](#ene2012). As the energy industry is responsible for the highest share of anthropogenic GHG emissions, importance is placed on how changes in energy systems can help achieve these GHG emission reduction targets [[ene2012]](#ene2012). 

A number of opportunities exist for the decarbonisation of the energy industry. The International Renewable Energy Agency (IRENA), in their renewable energy roadmap study, has identified renewable energy as having the highest potential in reducing energy-related carbon dioxide (CO<sub>2</sub>) emissions globally, which is closely followed by energy efficiency and electrification with renewable energy [[glo0000]](#glo0000). In a 2018 political agreement, the EU member states agreed upon a target of at least 32 % of the demand being met with renewables by 2030, through national targets of the individual member states [[ren0000]](#ren0000). The electricity demand in the transport sector is also expected to increase due to expected petrol and diesel engine bans and subsequently the electrification of road transport [[wor2017]](#wor2017).

According to the EU reference scenario 2016 [[ene0000]](#ene0000), wind and solar energy resources are expected to generate a total of 35 % of EU's electricity by 2050. This is a significant increase (23 %) from 2015 levels.

Table: Characteristics of the main energy generation technologies, adapted from Erbach 2016 [[erb2016]](#erb2016) and Tidball, et al. 2010 [[tid2010]](#tid2010).

Type<sup>[[f1]](#f1)</sup> | Variable | Fuel type | Flexibility | Low carbon | CAPEX<sup>[[f2]](#f2)</sup> | OPEX<sup>[[f2]](#f2)</sup> | LCOE<sup>[[f2]](#f2)</sup>
---|---|---|---|---|---|---|---
Coal | no | fossil | medium | no | low | high | very low 
Natural gas | no | fossil | high | no | very low | very high | low 
Biomass | no | renewable | medium | yes<sup>[[f3]](#f3)</sup> | low | very high | very high
Nuclear | no | nuclear | low | zero-emission | medium | medium | medium
Hydro | no | renewable | very high | zero-emission | | |
Solar | yes | renewable | very low | zero-emission | very high | very low | very high
Wind | yes | renewable | very low | zero-emission | | | 
*Onshore wind* | | | | | high | very low | very low 
*Offshore wind* | | | | | very high | low | high 
Geothermal | no | renewable | high | zero-emission | high | medium | high

<a name="f1">[f1]</a> *Costs for natural gas, biomass, solar and geothermal are that of advanced combustion turbine, biomass gasification plant, utility-scale photovoltaic and hydrothermal plant respectively*

<a name="f2">[f2]</a> *CAPEX - capital costs; OPEX - operational expenditure (includes fuel and fixed O&M costs); LCOE - levelised cost of electricity*

<a name="f3">[f3]</a> *regrowth of biomass compensates emissions*

<!-- As this directive additionally requires member states to provide at least 10 % of their transport fuels with renewables by 2020, and some member states have announced plans to ban petrol and diesel engine vehicles [[wor2017]](#wor2017), [[gra2017]](#gra2017), the electricity demand in the transport sector is expected to increase due to the electrification of road transport. -->

<!-- Figure~\ref{fig:euref} shows the shares of different electricity generation sources in the EU from 2000 to 2050 according to the reference scenario 2016 \cite{noauthor_energy_nodate-11}. These generation sources have different variabilities, fuel types, flexibilities, costs and carbon emissions, as shown in Table~\ref{tab:gen}. Wind and solar energy, which are \gls{vre} resources, are expected to generate a total of 35\,\% of \gls{eu}'s electricity by 2050. This is a significant increase (23\,\%) from 2015 levels. Conversely, generation from nuclear and solids, which are not variable and provide base load generation, are expected to decrease significantly. Unlike conventional generators, \gls{vre} are intermittent as they are dependent on atmospheric conditions, such as wind speed and cloud cover, and they vary spatially (i.e., location-dependent) and temporally \cite{joskow_comparing_2011}. Therefore, \gls{vre} generation cannot be controlled to meet the demand patterns and needs of the energy system \cite{joskow_comparing_2011}, which is a challenge to electricity and energy system operators in general. -->

# Regions

## North Sea countries

As per the definition provided by the European MSP Platform [[nor2000]](#nor0000) and the CPMR North Sea Commission [[mem2015]](#mem2015), the North Sea region consists of eight countries: Belgium, Denmark, France, Germany, Netherlands, Norway, Sweden and United Kingdom.

### [NUTS (Nomenclature of territorial units for statistics)](https://ec.europa.eu/eurostat/web/nuts/background)

[See the Jupyter notebook](https://github.com/ENSYSTRA/short-term-forecasting/tree/master/jupyter-notebooks/NUTS.ipynb).

## Bidding zones

### Definition

According to [[bid2014]](#bid2014):

* The largest geographical area within which market participants are able to exchange energy without capacity allocation. 
* The majority of bidding zones in Europe are defined by national borders (e.g., France or the Netherlands).
* Some are larger than national borders (e.g., Austria, Germany and Luxembourg or the Single Electricity Market for the island of Ireland) 
* Some are smaller zones within individual countries (e.g., Italy, Norway or Sweden). 

### Bidding zones in the North Sea region

The bidding zones in the European electricity market are illustrated in the map below [[tre2017]](#tre2017).

![Bidding zones in the European electricity market. Source: [Polskie Sieci Elektroenergetyczne](http://raport.pse.pl/en/trends-and-market-context).](images/market-map.png "Bidding zones in the European electricity market. Source: Polskie Sieci Elektroenergetyczne.")

Table: Bidding zones in the North Sea region.

**Country** | **Market(s)** | **Zone(s)**
--- | --- | ---
Belgium (BE) | EPEX SPOT | BE
Germany (DE / GE) | EPEX SPOT | DE-AT-LU<sup>[[f4]](#f4)</sup>
Denmark (DK) | Nord Pool | DK1, DK2
France (FR) | EPEX SPOT | FR
Netherlands (NL) | EPEX SPOT | NL
Norway (NO) | Nord Pool | NO1, NO2, NO3, NO4, NO5
Sweden (SE / SW) | Nord Pool | SE1, SE2, SE3, SE4
United Kingdom (UK) | EPEX SPOT, Nord Pool | GB, I-SEM<sup>[[f4]](#f4)</sup>

<a name="f4">[f4]</a> *Austria (AT / AU); Luxembourg (LU); Great Britain (GB); Irish single electricity market (I-SEM), which includes Republic of Ireland (IE) and UK's Northern Ireland (NI)*

# Data

## [Data folder](https://drive.google.com/drive/folders/1_3Y30j_c-4iai0WuhcrysXHYdZ4F2AKB) navigation

* ENTSO-E 
  * generation and load data for each bidding zone in the North Sea region, grouped by country
* Meteo - meteorological data, grouped by country
* Market - market data for the North Sea region
* NUTS - territorial units
* output - output or modified data from this project

## Met data

#### [Deutscher Wetterdienst](https://www.dwd.de/EN/climate_environment/cdc/cdc_node.html)

* [CDC (Climate Data Center) portal](https://cdc.dwd.de/portal/)
* [CDC OpenData](https://opendata.dwd.de/climate_environment/CDC/)
* [Terms of use for data on the CDC ftp server](https://opendata.dwd.de/climate_environment/CDC/Terms_of_use.pdf)
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

#### [Royal Netherlands Meteorological Institute](https://data.knmi.nl/datasets)
  
#### [Met Office](https://www.metoffice.gov.uk/datapoint)

#### [Norwegian Meteorological Institute](https://www.met.no/en/free-meteorological-data)

#### [Swedish Meteorological and Hydrological Institute](https://www.smhi.se/en/services/professional-services/data-and-statistics)

#### [Danish Meteorological Institute](http://research.dmi.dk/data/)

#### [Météo-France](https://donneespubliques.meteofrance.fr/)

#### [The Royal Meteorological Institute of Belgium](https://opendata.meteo.be/)

## Generation and demand data

#### [ENTSO-E Transparency Platform](https://transparency.entsoe.eu/)

* [GENERAL TERMS AND CONDITIONS FOR THE USE OF THE ENTSO-E TRANSPARENCY PLATFORM](https://docstore.entsoe.eu/Documents/MC%20documents/Transparency%20Platform/ENTSOE_Transparency_Terms_Conditions.pdf)
* [LIST OF DATA AVAILABLE FOR FREE RE-USE](https://docstore.entsoe.eu/Documents/MC%20documents/Transparency%20Platform/List_of_Data_available_for_reuse.pdf)
* Downloaded data:
  * [Actual Generation per Production Type](https://transparency.entsoe.eu/generation/r2/actualGenerationPerProductionType/show)
  * [Total Load - Day Ahead / Actual](https://transparency.entsoe.eu/load-domain/r2/totalLoadR2/show)

## Market data

#### [Nord Pool](https://www.nordpoolgroup.com/historical-market-data/)

* [Membership list - Nord Pool](https://www.nordpoolgroup.com/trading/join-our-markets/membership/)
* [Terms and conditions for use](https://www.nordpoolgroup.com/About-us/Terms-and-conditions-for-use/)

#### [EPEX Spot](https://www.epexspot.com/en/extras/download-center/market_data)

* [EPEX SPOT Exchange Members](https://www.epexspot.com/en/membership/list_of_members)

## Other data

#### [NUTS (Nomenclature of territorial units for statistics)](https://ec.europa.eu/eurostat/web/gisco/geodata/reference-data/administrative-units-statistical-units/nuts)

# Methodology

## Modelling framework

![Modelling framework.](images/model_framework.jpg "Modelling framework.")

# References

<a name="bid2014">[bid2014]</a> ‘Bidding Zones Literature Review’. Ofgem, July 2014. <https://www.ofgem.gov.uk/sites/default/files/docs/2014/10/fta_bidding_zone_configuration_literature_review_1.pdf>.

<a name="ene0000">[ene0000]</a> ‘Energy Modelling - EU Reference Scenario 2016’. Accessed 1 November 2018. <https://data.europa.eu/euodp/data/dataset/energy-modelling>.

<a name="ene2012">[ene2012]</a> Energy roadmap 2050, 2012. Publications Office of the European Union, Luxembourg. <https://doi.org/10.2833/10759>.

<a name="erb2016">[erb2016]</a> Erbach, Gregor. ‘Understanding Electricity Markets in the EU’. Briefing. European Union, November 2016. <http://www.europarl.europa.eu/RegData/etudes/BRIE/2016/593519/EPRS_BRI(2016)593519_EN.pdf>.

<a name="glo0000">[glo0000]</a> ‘Global Energy Transformation: A Roadmap to 2050’. International Renewable Energy Agency. Accessed 14 November 2018. <http://www.irena.org/publications/2018/Apr/Global-Energy-Transition-A-Roadmap-to-2050>.

<a name="mem2015">[mem2015]</a> ‘Member Directory | Map -- CPMR North Sea Commission’, 21 October 2015. <https://cpmr-northsea.org/who-we-are/member-directory-map/>.

<a name="nor0000">[nor0000]</a> ‘North Sea | European MSP Platform’. Accessed 1 June 2018. <https://www.msp-platform.eu/sea-basins/north-sea-0>.

<a name="par2015">[par2015]</a> ‘Paris Agreement’. United Nations Framework Convention on Climate Change, 2015. <https://unfccc.int/process-and-meetings/the-paris-agreement/the-paris-agreement>.

<a name="ren0000">[ren0000]</a> ‘Renewable Energy - Energy - European Commission’. Energy. Accessed 12 October 2018. <https://ec.europa.eu/energy/en/topics/renewable-energy>.

<a name="tid2010">[tid2010]</a> Tidball, R, J Bluestein, N Rodriguez, S Knoke, ICF International, and J Macknick. ‘Cost and Performance Assumptions for Modeling Electricity Generation Technologies’. Subcontract Report. National Renewable Energy Laboratory, 2010. <https://www.nrel.gov/docs/fy11osti/48595.pdf>.

<a name="tre2017">[tre2017]</a> ‘Trends and Market Context’. PSE Impact Report. PSE, 2017. <http://raport.pse.pl/en/trends-and-market-context>.

<a name="wor2017">[wor2017]</a> ‘World Energy Outlook 2017’. Paris, France: International Energy Agency, 2017. <https://www.iea.org/weo2017/>.