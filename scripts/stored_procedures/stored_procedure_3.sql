DELIMITER //
CREATE PROCEDURE EmployeePerformanceReport(
    IN p_emp_id INT
)
BEGIN
    SELECT e.name, e.position, e.salary, b.location as branch
    FROM Employee e
    JOIN Employee_works_in_Branch ewb ON e.emp_id = ewb.emp_id
    JOIN Branch b ON ewb.branch_id = b.bra_id
    WHERE e.emp_id = p_emp_id;
END;//
DELIMITER ; 