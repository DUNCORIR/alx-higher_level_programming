-- SQL script to calculate average temperature
-- (Fahrenheit) by city and order by temperature

SELECT city,
	AVG(value *9/5 + 32) AS avg_temperature_fahrenheit
FROM temperatures
GROUP BY city
ORDER BY avg_temperature_fahrenheit DESC;
