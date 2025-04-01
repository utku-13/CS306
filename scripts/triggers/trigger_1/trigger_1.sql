DELIMITER //
CREATE TRIGGER check_rental_period
BEFORE INSERT ON RentalPeriod
FOR EACH ROW
BEGIN
    IF NEW.end_date <= NEW.start_date THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Bitiş tarihi başlangıç tarihinden sonra olmalıdır';
    END IF;
END;//
DELIMITER ; 