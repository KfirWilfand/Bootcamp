-- nested selected

-- 1. Who are the first ten employees (who ever held this title) whose title is or was Assistant Engineer?
select first_name,last_name,title,from_date
from employees.employees em 
    inner join employees.titles t 
        on t.emp_no = em.emp_no
	WHERE title = 'Assistant Engineer'
    order by from_date asc
    limit 10


-- 2. Who are second ten employees (11-20, who ever held this title) whose title is or was Senior Engineer?
select first_name,last_name,title,from_date
from employees.employees em 
    inner join employees.titles t 
        on t.emp_no = em.emp_no
	WHERE title = 'Senior Engineer'
    order by from_date asc
    limit 10 offset 10

-- 3. What are the departments who have the largest amount of engineers (of any kind)?
select dept_name,count(*) 
from employees.titles t 
    inner join employees.dept_emp dep_em
		on dep_em.emp_no = t.emp_no
	inner join employees.departments dep
		on dep_em.dept_no = dep.dept_no
WHERE title LIKE '% Engineer'
GROUP BY dept_name
ORDER BY count(*) desc;
        

-- 4. Per department, who is the employee that held the highest salary?
SELECT dept_name, max(salary) FROM dept_emp as de
INNER JOIN departments as d ON de.dept_no = d.dept_no
INNER JOIN employees as e ON de.emp_no = e.emp_no
INNER JOIN salaries as s ON de.emp_no = s.emp_no and de.from_date < s.from_date and de.to_date > s.to_date
GROUP BY dept_name;