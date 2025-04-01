DELIMITER //
CREATE PROCEDURE GetCarDamageHistory(
    IN p_car_id INT
)
BEGIN
    SELECT d.damage_id, d.description, d.repair_cost, c.brand, c.plate_number
    FROM Car_has_damage_record d
    JOIN Branch_has_car c ON d.car_id = c.car_id
    WHERE d.car_id = p_car_id;
END;//
DELIMITER ; 