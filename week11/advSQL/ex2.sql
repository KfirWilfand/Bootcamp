use employees;

-- Question 1
-- How many male employees and how many female employees have worked in the company (single query)?
select count(*)
from employees where gender = 'M'


-- Question 2
-- How many different titles are there in the company?
select count(distinct(title))
from titles;

-- Question 3
-- What are the names and titles of the employees who got hired in 1993?
select first_name, last_name, title 
from employees em 
    inner join titles t     
    on em.emp_no = t.emp_no 
    where year(hire_date) = 1993;

-- Question 4
-- Who are the ten employees whose title is or was Staff and have the lowest salary?
select first_name, last_name, title, salary
from employees.employees em 
    inner join employees.titles t 
        on em.emp_no = t.emp_no
    inner join employees.salaries sal 
        on t.emp_no = sal.emp_no
where title = 'staff'
order by salary asc
limit 10;

-- Question 5
-- What is the average salary per title? Order the results from highest to lowest.
select title ,avg(salary)
from employees.titles t 
    inner join employees.salaries sal 
        on t.emp_no = sal.emp_no
GROUP by title
order by avg(salary) desc; 