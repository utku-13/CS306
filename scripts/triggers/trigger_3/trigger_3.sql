DELIMITER //
CREATE TRIGGER log_salary_changes
AFTER UPDATE ON Employee
FOR EACH ROW
BEGIN
    IF OLD.salary != NEW.salary THEN
        INSERT INTO SalaryChangeLog (emp_id, old_salary, new_salary, change_date)
        VALUES (NEW.emp_id, OLD.salary, NEW.salary, NOW());
    END IF;
END;//
DELIMITER ; 