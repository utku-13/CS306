DELIMITER //
CREATE TRIGGER damage_record_notification
AFTER INSERT ON Car_has_damage_record
FOR EACH ROW
BEGIN
    INSERT INTO Notifications (car_id, message, date)
    VALUES (NEW.car_id, CONCAT('Araç ID:', NEW.car_id, ' için yeni hasar kaydı: ', NEW.description), NOW());
END;//
DELIMITER ; 