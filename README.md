# NEM-negative-prices
Project to investigate when NEM has negative prices

Method to acquire data: Run the python file src/load_prices.py which uses SQL queries to acquire the data
Data: AEMO NEMWEB MMSDM (Market Management System Data Models) archive using the (DISPATCHPRICE table), retrieved via nemosis
    The data specifically collected will be 
    1. SETTLEMENTDATE: the end time of each 5-min interval
    2. REGIONID: the NEM region (QLD1, NSW1, TAS1, SA1, VIC1)
    3. RRP: the regional reference price in $/MWh
    4. INTERVENTION: a flag for when AEMO  intervened in the market. And filter for when AEMO does not interfere


Temporary ideas for EDA:
1. The loading process tells the min and max of the RRP for each of the regions, but doesn't contain information about the floor or ceiling of prices. These numbers may change every financial year, so will have to look them up, and any comparison will need to be with those numbers. 
2. How does price change over time? Summary statistics for a year of data?