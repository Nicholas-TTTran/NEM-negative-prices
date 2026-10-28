from pathlib import Path
import duckdb
from nemosis import dynamic_data_compiler #package specific to AEMO that can help read data from nemweb.com.au

CACHE = Path("data/raw_cache")
CACHE.mkdir(parents=True, exist_ok=True)

START = "2024/01/01 00:00:00"
END = "2025/01/01 00:00:00" # test with one month, then increase later

prices = dynamic_data_compiler(
    START, END, "DISPATCHPRICE", str(CACHE), #AEMO table is DISPATCHPRICE
    select_columns= ["SETTLEMENTDATE", "REGIONID", "RRP", "INTERVENTION"], # The end time of the 5 min intervals, NEM region, regional reference price $/MWh, flag for AEMO intervening in the market
)
prices = prices[prices["INTERVENTION"]==0]

con = duckdb.connect("data/nem.duckdb") #open connection to file (or create one)
con.execute("CREATE OR REPLACE TABLE dispatch_price AS SELECT * FROM prices")
print(con.execute(
    "SELECT REGIONID, COUNT(*) AS n, min(RRP), max(RRP) FROM dispatch_price GROUP BY 1"
).df())
con.close()