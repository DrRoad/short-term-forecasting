<!-- 
- [Regions](#regions)
  - [North Sea countries](#north-sea-countries)
    - [NUTS (Nomenclature of territorial units for statistics)](#nuts-nomenclature-of-territorial-units-for-statistics)
  - [Bidding zones](#bidding-zones)
    - [Definition](#definition)
    - [Bidding zones in the North Sea region](#bidding-zones-in-the-north-sea-region)
    - [Transmission system operators and interconnections](#transmission-system-operators-and-interconnections)
 -->

# Regions

## North Sea countries

As per the definition provided by the European MSP Platform [NortND] and the CPMR North Sea Commission [Memb15], the North Sea region consists of eight countries: Belgium, Denmark, France, Germany, Netherlands, Norway, Sweden and United Kingdom.

### [NUTS (Nomenclature of territorial units for statistics)](https://ec.europa.eu/eurostat/web/nuts/background)

[See the Jupyter notebook](https://github.com/ENSYSTRA/short-term-forecasting/tree/master/jupyter-notebooks/NUTS.ipynb).

## Bidding zones

### Definition

According to [Bidd14]:

* The largest geographical area within which market participants are able to exchange energy without capacity allocation. 
* The majority of bidding zones in Europe are defined by national borders (e.g., France or the Netherlands).
* Some are larger than national borders (e.g., Austria, Germany and Luxembourg or the Single Electricity Market for the island of Ireland) 
* Some are smaller zones within individual countries (e.g., Italy, Norway or Sweden). 

### Bidding zones in the North Sea region

The bidding zones in the European electricity market are illustrated in the map below [Tren17].

![Bidding zones in the European electricity market. Source: [Polskie Sieci Elektroenergetyczne](http://raport.pse.pl/en/trends-and-market-context) [Tren17].](images/market-map.png "Bidding zones in the European electricity market. Source: Polskie Sieci Elektroenergetyczne [Tren17].")

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

<a name="f4">[f4]</a> *Austria (AT / AU); Luxembourg (LU); Great Britain (GB); Irish single electricity market (I-SEM), which includes Republic of Ireland (IE) and UK's Northern Ireland (NI).*

### Transmission system operators and interconnections

The power exchanges that operate in the North Sea region are EPEX SPOT (Belgium, France, Germany, Netherlands, United Kingdom) and Nord Pool (Denmark, Norway, Sweden, United Kingdom) [Over16], [See ND], [EPEXND]. The day-ahead market takes place generally as an hourly auction 24 hours prior to dispatch [Over16]. The intra-day market has continuous trading and will operate until two hours and up to five minutes before dispatch [Over16]. The North Sea region consists of multiple TSOs, cross-border interconnections and bidding zones, as listed in the table below.

Table: TSOs and cross-border interconnections in the North Sea region. Data: European Network of Transmission System Operators for Electricity [ENTSND], [RegiND].

Ctry.<sup>[[f5]](#f5)</sup> | TSOs | Cross-border interconnection<sup>[[f5]](#f5),[[f6]](#f6)</sup> | Bidding zones<sup>[[f5]](#f5),[[f6]](#f6)</sup>
-|-----|---|---
BE | Elia System Operator | FR, LU, NL, UK | BE 
DK | Energinet | DE, NO, SE | DK1, DK2 
DE | TransnetBW, TenneT TSO, Amprion, 50Hertz Transmission | AT, CH, CZ, DK, FR, LU, NL, PL, SE | CZ+DE+SK, DE-AT-LU, DE-LU 
FR | Réseau de Transport d'Electricité | BE, CH, DE, ES, IT, UK | FR 
NL | TenneT TSO | BE, DE, NO, UK | NL 
NO | Statnett | DK, FI, NL, SE | NO1, NO2, NO3, NO4, NO5 
SE | Svenska Kraftnät | DK, FI, DE, LT, NO, PL | SE1, SE2, SE3, SE4 
UK | National Grid Electricity Transmission, System Operator for Northern Ireland, Scottish Hydro Electric Transmission, ScottishPower Transmission | BE, FR, IE, NL | GB, IE (SEM)

<a name="f4">[f5]</a> *Ctry. - Country; AT - Austria; BE - Belgium; CH - Switzerland; CZ - Czech Republic; DE - Germany; DK - Denmark; ES - Spain; FI - Finland; FR - France; GB - Great Britain; IE - Ireland; IT - Italy; LT - Lithuania; LU - Luxembourg; NL - Netherlands; NO - Norway; PL - Poland; SE - Sweden; SK - Slovakia; UK - United Kingdom; SEM - Single electricity market.*

<a name="f4">[f6]</a> *These countries are not part of the North Sea region: AT, CH, CZ, ES, FI, IE, IT, LT, LU, PL.*