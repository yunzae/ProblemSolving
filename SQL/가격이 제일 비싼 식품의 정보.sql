SELECT *
FROM FOOD_PRODUCT
WHERE PRICE=(SELECT MAX(PRICE)
FROM FOOD_PRODUCT)


SELECT * FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;