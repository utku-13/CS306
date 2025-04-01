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
END;//
DELIMITER ; 