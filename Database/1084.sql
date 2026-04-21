select distinct P.product_id, P.product_name
from Product as P
where P.product_id in (select product_id
from Sales as S
group by product_id
having min(sale_date) >= '2019-01-01' and max(sale_date) <= '2019-03-31');
