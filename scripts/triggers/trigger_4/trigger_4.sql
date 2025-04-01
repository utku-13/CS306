DELIMITER //
CREATE TRIGGER check_insurance_validity
BEFORE INSERT ON Car_has_insurance
FOR EACH ROW
BEGIN
    IF NEW.end_date <= NEW.start_date THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Sigorta bitiş tarihi başlangıç tarihinden sonra olmalıdır';
    END IF;
END;//
DELIMITER ; 