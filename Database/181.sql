select e1.name as Employee
from Employee as e1, Employee as e2
where e1.managerId = e2.id
and e1.salary > (
    select e3.salary 
    from Employee as e3 
    where e3.id = e2.id);