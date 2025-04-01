DELIMITER //
CREATE PROCEDURE GetBranchCars(
    IN p_branch_id INT
)
BEGIN
    SELECT c.car_id, c.brand, c.plate_number, c.model
    FROM Branch_has_car c
    WHERE c.branch_id = p_branch_id;
END;//
DELIMITER ; 