SELECT
    REGIONID AS region,
    HOUR(SETTLEMENTDATE - INTERVAL 5 MINUTE) AS hour,
    AVG(CASE WHEN RRP < 0 THEN 1 ELSE 0 END) AS negative_proportion
FROM dispatch_price
GROUP BY region, hour
ORDER BY region, hour;