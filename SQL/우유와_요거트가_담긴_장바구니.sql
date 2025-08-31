# 우유와 요거트를 동시에 구입한 장바구니가 있는지 알아보려고 함, 장바구니 아이디 순
SELECT CART_ID
FROM CART_PRODUCTS
GROUP BY CART_ID
HAVING SUM(NAME = 'Milk') > 0 AND SUM(NAME = 'Yogurt') > 0
ORDER BY CART_ID