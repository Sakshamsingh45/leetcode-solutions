SELECT ep1.name AS Employee
FROM employee AS ep1
JOIN employee AS ep2
  ON ep1.managerId = ep2.id
WHERE ep1.salary > ep2.salary;
