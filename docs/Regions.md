<!-- 
- [Regions](#regions)
  - [Territories in the North Sea region](#territories-in-the-north-sea-region)
  - [Bidding zones in the North Sea region](#bidding-zones-in-the-north-sea-region)
  - [Transmission system operators and interconnections](#transmission-system-operators-and-interconnections)
 -->


# Regions


## Territories in the North Sea region

As per the definition provided by the European MSP Platform [@North] and the CPMR North Sea Commission [@Membe15], the North Sea region consists of eight countries: Belgium, Denmark, France, Germany, Netherlands, Norway, Sweden and United Kingdom.

The nomenclature of territorial units for statistics (NUTS) classifies territorial units in Europe in different levels [@NUTS]:

* NUTS 0: country-level
* NUTS 1: major socio-economic regions
* NUTS 2: basic regions for the application of regional policies
* NUTS 3: small regions for specific diagnoses

As explained in the problem definition section, short-term operational planning and systems with a high penetration of VRE must be described using data of high temporal and spatial resolutions. Therefore, NUTS 3 territories will be used as a standard in this project for aggregating short-term forecasting data.

This [Jupyter notebook](https://github.com/ENSYSTRA/short-term-forecasting/tree/master/jupyter-notebooks/nuts.ipynb) lists the NUTS territories in the North Sea region at all four NUTS levels. France is the only North Sea country with overseas territories included in the NUTS data (RUP FR - RÉGIONS ULTRAPÉRIPHÉRIQUES FRANÇAISES), so these were removed accordingly.

Performing the forecasting task at NUTS 3 level would be straightforward if it does not include the electricity market. Since the electricity market is considered in this project, it is important to look at how the bidding zones overlap with NUTS 3 territories.


## Bidding zones in the North Sea region

A bidding zone is the largest geographical area within which market participants are able to exchange energy without capacity allocation [@Biddi14]. According to [@Biddi14], there are three types of bidding zones:

1. national borders (e.g., France or the Netherlands) - majority of bidding zones in Europe
2. larger than national borders (e.g., Germany and Luxembourg or the Single Electricity Market for the island of Ireland) 
3. smaller zones within individual countries (e.g., Italy, Norway or Sweden)

The bidding zones in the North Sea electricity markets and surrounding regions are illustrated in @fig:map.

![Bidding zones in the North Sea electricity markets and surrounding regions. Countries in the North Sea region are in blue, while neighbouring contries with interconnections are in purple. Made using a blank SVG map of Europe from Wikimedia Commons (CC-BY-SA-4.0) [@Nordw15].](images/market-map.png "Bidding zones in the North Sea electricity markets and surrounding regions. Countries in the North Sea region are in blue, while neighbouring contries with interconnections are in purple. Made using a blank SVG map of Europe from Wikimedia Commons (CC-BY-SA-4.0) [@Nordw15]."){#fig:map}

The power exchanges (market operators) that operate in the North Sea region are APX (Netherlands, United Kingdom), Belpex (Belgium), EEX (Germany, Denmark, France, Norway, Sweden), EPEX (Germany, France), N2EX (United Kingdom) and Nord Pool (Denmark, Norway, Sweden) [@Power], [@Overv16], [@Seem], [@EPEX]. The day-ahead market takes place generally as an hourly auction 24 hours prior to dispatch [@Overv16]. The intra-day market has continuous trading and will operate until two hours and up to five minutes before dispatch [@Overv16].

Both Nord Pool and EPEX are part of the Price Coupling of Regions (PCR) project which aims to develop a single price coupling solution for the calculation of day-ahead electricity prices in Europe, taking into account day-ahead network capacities [@PCRE17].

@Tbl:zones below lists all bidding zones in the North Sea region by country and market operator. 

**Country** | **Markets** | **Zones**[^f4]
--- | --- | ---
Belgium (BE) | Belpex | BE
Germany (DE) | EEX, EPEX | DE-LU
Denmark (DK) | EEX, Nord Pool | DK1, DK2
France (FR) | EEX, EPEX | FR
Netherlands (NL) | APX | NL
Norway (NO) | EEX, Nord Pool | NO1, NO2, NO3, NO4, NO5
Sweden (SE) | EEX, Nord Pool | SE1, SE2, SE3, SE4
United Kingdom (UK) | APX, N2EX | GB, IE-SEM

: Bidding zones and market operators in the North Sea region. {#tbl:zones}

[^f4]: *Luxembourg (LU); Great Britain (GB); Irish single electricity market (IE-SEM), which includes Republic of Ireland and UK's Northern Ireland.*

Mapping bidding zones to NUTS 3 territories is straightforward for Belgium, Germany, France and Netherlands (bidding zone type 1 or 2) -- all NUTS 3 territories in these countries have the same bidding zone. 

Denmark and United Kingdom are both conveniently separated into two zones that are easily distinguishable. For Denmark, these are Western Denmark (NUTS IDs containing DK03-DK05) and Southern Denmark (NUTS IDs containing DK01-DK02). For United Kingdom, these are Great Britain (NUTS IDs containing UKC-UKM) and Northern Ireland (NUTS IDs containing UKN). 

There is no clear indication of the bidding zone boundaries for Norway and Sweden, so some assumptions were made. Both countries have multiple smaller bidding zones (type 3) with flexible borders [@Europ10], [@List]. This was done to optimise allocation of resources and reduce the overall price of electricity [@Europ10], [@List]. Norway has five zones and Sweden has four zones. By cross-referencing Nord Pool market data [@Seem], NUTS 3 data and county maps of Norway [@Count19] and Sweden [@Count19a], the territories are split into the bidding zones as shown in @tbl:nord. Nord Pool associates each bidding zone with a major reference city in that zone. However, there were six cities for Norway instead of the expected five. Historical Nord Pool market data for Norway suggests that two cities, Trondheim and Molde, have had the same system price since 2003. The ELSPOT area change log [@List] also confirms that Trondheim and Molde are city references for the NO3 bidding zone . Therefore, these two cities are grouped into the same bidding zone, which also satisfies what the maps suggest.

**Bidding zone** | **Reference cities** | **Counties** | **NUTS 3 IDs**
-- | -- | ------ | ---
NO1 | Oslo | Oslo, Akershus, Hedmark, Oppland, Østfold, Buskerud, Vestfold, Telemark | NO011-034
NO2 | Kristiansand | Aust-Agder, Vest-Agder, Rogaland | NO041-043
NO3 | Trondheim, Molde | Sogn og Fjordane, Møre og Romsdal, Trøndelag | NO052-060
NO4 | Tromsø | Nordland, Troms, Finnmark | NO071-073
NO5 | Bergen | Hordaland | NO051
SE1 | Luleå | Norrbotten | SE332
SE2 | Sundsvall | Gävleborg, Västernorrland, Jämtland, Västerbotten | SE313-331
SE3 | Stockholm | Stockholm, Uppsala, Södermanland, Östergötland, Örebro, Västmanland, Jönköping, Gotland, Västra Götaland, Värmland, Dalarna | SE110-211, SE214, SE232-312
SE4 | Malmö | Kronoberg, Kalmar, Blekinge, Halland, Skåne | SE212-213, SE221-231

: Bidding zones and their territories for Norway and Sweden, approximated based on Nord Pool market data [@Seem], [@List], NUTS 3 data and county maps of Norway [@Count19] and Sweden [@Count19a]. {#tbl:nord}

This [Jupyter notebook](https://github.com/ENSYSTRA/short-term-forecasting/tree/master/jupyter-notebooks/nuts_biddingZones.ipynb) lists all NUTS 3 territories and their bidding zones in the North Sea region, and explains how the different bidding zones were assigned to the territories.


## Transmission system operators and interconnections

The North Sea region consists of multiple TSOs and cross-border interconnections. These are listed, along with the bidding zones bidding zones, in @tbl:tso.

**Ctry.**[^f5] | **TSOs** | **Cross-border interconnection**[^f6] | **Bidding zones**
-|-----|---|---
BE | Elia System Operator | FR, LU, NL, UK | BE 
DK | Energinet | DE, NO, SE | DK1, DK2 
DE | TransnetBW, TenneT TSO, Amprion, 50Hertz Transmission | AT, CH, CZ, DK, FR, LU, NL, PL, SE | DE-LU 
FR | Réseau de Transport d'Electricité | BE, CH, DE, ES, IT, UK | FR 
NL | TenneT TSO | BE, DE, NO, UK | NL 
NO | Statnett | DK, FI, NL, SE | NO1, NO2, NO3, NO4, NO5 
SE | Svenska Kraftnät | DK, FI, DE, LT, NO, PL | SE1, SE2, SE3, SE4 
UK | National Grid Electricity Transmission, System Operator for Northern Ireland, Scottish Hydro Electric Transmission, ScottishPower Transmission | BE, FR, IE, NL | GB, IE-SEM

: TSOs and cross-border interconnections in the North Sea region. Data: European Network of Transmission System Operators for Electricity [@ENTSO], [@Regio]. {#tbl:tso}

[^f5]: *Ctry. - Country; AT - Austria; BE - Belgium; CH - Switzerland; CZ - Czech Republic; DE - Germany; DK - Denmark; ES - Spain; FI - Finland; FR - France; GB - Great Britain; IE - Ireland; IT - Italy; LT - Lithuania; LU - Luxembourg; NL - Netherlands; NO - Norway; PL - Poland; SE - Sweden; SK - Slovakia; UK - United Kingdom; SEM - Single electricity market.*

[^f6]: *These countries are not part of the North Sea region: AT, CH, CZ, ES, FI, IE, IT, LT, LU, PL.*
