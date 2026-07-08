# Write your MySQL query statement below
select name As customers
from customers 
left join orders on customers.id=orders.customerId
where orders.customerId is null;