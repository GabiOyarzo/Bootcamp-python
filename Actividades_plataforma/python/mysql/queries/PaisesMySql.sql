use world;

-- 1. ¿Qué consulta ejecutarías para obtener todos los países que hablan esloveno? 
-- Tu consulta debe devolver el nombre del país, el idioma y el porcentaje de habla del idioma.  
-- Tu consulta debe ordenar el resultado por porcentaje de habla del idioma en orden descendente. (1)

SELECT country.Name AS pais, countrylanguage.Language AS idioma, countrylanguage.Percentage AS porcentaje_habla
FROM countrylanguage
JOIN country ON countrylanguage.CountryCode = country.Code
WHERE countrylanguage.Language = 'Slovene'
ORDER BY countrylanguage.Percentage DESC;

-- 2. ¿Qué consulta ejecutarías para mostrar el número total de ciudades de cada país?  Tu consulta debe devolver el nombre del país, 
-- el idioma y el número total de ciudades. Tu consulta debe ordenar el resultado por el número de ciudades en orden descendente. (3)

SELECT country.Name AS nombre_pais, COUNT(city.ID) AS total_ciudades
FROM country
JOIN city ON country.Code = city.CountryCode
GROUP BY country.Code
ORDER BY total_ciudades DESC;

-- 3. ¿Qué consulta ejecutarías para obtener todos ciudades de México con una población mayor a 500,000? 
-- Tu consulta debe ordenar el resultado por población en orden descendente. (1)

SELECT city.Name AS nombre_ciudad, city.Population AS poblacion
FROM city
JOIN country ON city.CountryCode = country.Code
WHERE country.Name = 'Mexico' AND city.Population > 500000
ORDER BY city.Population DESC;

-- 4. ¿Qué consulta ejecutarías para obtener todos los idiomas en cada país con un porcentaje de habla mayor a 89%? Tu consulta debe ordenar el resultado por porcentaje de habla en orden descendente. (1)

SELECT country.Name AS pais, countrylanguage.Language AS idioma, countrylanguage.Percentage AS porcentaje_habla
FROM countrylanguage
JOIN country ON countrylanguage.CountryCode = country.Code
WHERE countrylanguage.Percentage > 89
ORDER BY countrylanguage.Percentage DESC;

-- 5. ¿Qué consulta ejecutarías para obtener todos los países con un área de superficie menor a 501 y población mayor a 100,000? (2)

SELECT country.Name as Pais, country.SurfaceArea as Superficie, country.Population as Poblacion
FROM country
WHERE SurfaceArea < 501 AND Population > 100000;

-- 6. ¿Qué consulta ejecutarías para obtener países solo con monarquía constitucional, un capital superior a 200 y una esperanza de 
-- vida mayor a 75 años?  (1)

SELECT country.Name as Pais, GovernmentForm as tipo_gobierno, capital as capital, LifeExpectancy as ExpectativaVida
FROM country
WHERE GovernmentForm = 'Constitutional Monarchy' AND Capital > 200 AND LifeExpectancy > 75;

-- 7. ¿Qué consulta ejecutarías para obtener todas las ciudades de Argentina dentro del distrito de Buenos Aires con 
-- una población mayor a 500,000 habitantes?  La consulta debe devolver el nombre del país, el nombre de la ciudad, 
-- el distrito y la población.  (2)

SELECT country.Name as Pais, city.Name AS nombre_ciudad, district as distrito, city.Population AS poblacion
FROM city
JOIN country ON city.CountryCode = country.Code
WHERE country.Name = 'Argentina' AND city.Population > 500000 AND  district = 'Buenos Aires'
ORDER BY city.Population DESC;

-- 8. ¿Qué consulta ejecutarías para resumir el número de países en cada región? Tu consulta debe mostrar el nombre de la región y 
-- el número de países. Además, debe ordenar el resultado por el número de países en orden descendente. (2)

SELECT country.Region AS Region, COUNT(*) AS total_paises
from country
group by region
ORDER BY COUNT(*) DESC;