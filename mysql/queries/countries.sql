SELECT countries.name, languages.language, languages.percentage FROM countries
LEFT JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name AS name , SUM(cities.name) AS cities from countires
LEFT JOIN cities ON countries.id = cities.coutnry_id
GROUP BY countries.name
ORDER BY cities DESC;

SELECT cities.name FROM countries
LEFT JOIN cities ON countries.id = cities.coutnry_id
WHERE countries.name = 'Mexico' and cities.population > 500000
ORDER BY cities.population DESC;

SELECT languages.language FROM countries
LEFT JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY percentage DESC;

SELECt countries.name FROM countries
WHERE countries.surface_area < 501 AND countries.population > 100000; 

SELECt countries.name FROM countries
WHERE countries.government_form = 'Constitutional Monarchy' AND countries.capital > 200 AND countries.life_expectancy < 75;

SELECT cities.name, cities.district, cities.population FROM countries
LEFT JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires';

SELECT countries.region, COUNT(countries.name) as countries
FROM countries
GROUP BY countries.region
ORDER BY countries DESC