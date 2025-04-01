-- Stored Procedure 1: Yeni Rezervasyon Oluşturma
DELIMITER //
CREATE PROCEDURE CreateNewReservation(
    IN p_customer_id INT,
    IN p_car_id INT,
    IN p_start_date DATE,
    IN p_end_date DATE
)
BEGIN
    DECLARE v_res_id INT;
    DECLARE v_rent_id INT;
    
    -- Yeni rezervasyon oluştur
    INSERT INTO Reservation (res_date) VALUES (CURDATE());
    SET v_res_id = LAST_INSERT_ID();
    
    -- Kiralama periyodu oluştur
    INSERT INTO RentalPeriod (res_id, start_date, end_date)
    VALUES (v_res_id, p_start_date, p_end_date);
    
    -- Müşteri rezervasyon ilişkisi
    INSERT INTO Customer_makes_reservation (customer_id, res_id)
    VALUES (p_customer_id, v_res_id);
    
    -- Araç rezervasyon ilişkisi
    INSERT INTO Reservation_includes_car (res_id, car_id)
    VALUES (v_res_id, p_car_id);
END//

-- Stored Procedure 2: Şube Araçları Listesi
CREATE PROCEDURE GetBranchCars(
    IN p_branch_id INT
)
BEGIN
    SELECT c.car_id, c.brand, c.plate_number, c.model
    FROM Branch_has_car c
    WHERE c.branch_id = p_branch_id;
END//

-- Stored Procedure 3: Çalışan Performans Raporu
CREATE PROCEDURE EmployeePerformanceReport(
    IN p_emp_id INT
)
BEGIN
    SELECT e.name, e.position, e.salary, b.location as branch
    FROM Employee e
    JOIN Employee_works_in_Branch ewb ON e.emp_id = ewb.emp_id
    JOIN Branch b ON ewb.branch_id = b.bra_id
    WHERE e.emp_id = p_emp_id;
END//

-- Stored Procedure 4: Araç Hasar Geçmişi
CREATE PROCEDURE GetCarDamageHistory(
    IN p_car_id INT
)
BEGIN
    SELECT d.damage_id, d.description, d.repair_cost, c.brand, c.plate_number
    FROM Car_has_damage_record d
    JOIN Branch_has_car c ON d.car_id = c.car_id
    WHERE d.car_id = p_car_id;
END//

DELIMITER ; 