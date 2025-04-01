import pymysql

# Veritabanı bağlantısı
def get_db_connection():
    connection = pymysql.connect(host='localhost',
                               user='root',
                               password='U147613d!',
                               database='RENTACAR')
    return connection

# Stored procedure scriptleri
create_new_reservation = """
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
END
"""

get_branch_cars = """
CREATE PROCEDURE GetBranchCars(
    IN p_branch_id INT
)
BEGIN
    SELECT c.car_id, c.brand, c.plate_number, c.model
    FROM Branch_has_car c
    WHERE c.branch_id = p_branch_id;
END
"""

employee_performance_report = """
CREATE PROCEDURE EmployeePerformanceReport(
    IN p_emp_id INT
)
BEGIN
    SELECT e.name, e.position, e.salary, b.location as branch
    FROM Employee e
    JOIN Employee_works_in_Branch ewb ON e.emp_id = ewb.emp_id
    JOIN Branch b ON ewb.branch_id = b.bra_id
    WHERE e.emp_id = p_emp_id;
END
"""

get_car_damage_history = """
CREATE PROCEDURE GetCarDamageHistory(
    IN p_car_id INT
)
BEGIN
    SELECT d.damage_id, d.description, d.repair_cost, c.brand, c.plate_number
    FROM Car_has_damage_record d
    JOIN Branch_has_car c ON d.car_id = c.car_id
    WHERE d.car_id = p_car_id;
END
"""

# Stored procedure'ları oluştur
def create_procedure(connection, proc_name, proc_sql):
    with connection.cursor() as cursor:
        try:
            # Eğer procedure zaten varsa, önce sil
            cursor.execute(f"DROP PROCEDURE IF EXISTS {proc_name}")
            # Yeni procedure'u oluştur
            cursor.execute(proc_sql)
            print(f"{proc_name} başarıyla oluşturuldu.")
        except Exception as e:
            print(f"Hata: {proc_name} oluşturulurken bir sorun oluştu: {str(e)}")

def main():
    try:
        conn = get_db_connection()
        print("Veritabanına bağlanıldı.")
        
        create_procedure(conn, "CreateNewReservation", create_new_reservation)
        create_procedure(conn, "GetBranchCars", get_branch_cars)
        create_procedure(conn, "EmployeePerformanceReport", employee_performance_report)
        create_procedure(conn, "GetCarDamageHistory", get_car_damage_history)
        
        conn.commit()
        print("Tüm stored procedure'lar başarıyla oluşturuldu.")
    except Exception as e:
        print(f"Hata: {str(e)}")
    finally:
        if conn:
            conn.close()
            print("Veritabanı bağlantısı kapatıldı.")

if __name__ == "__main__":
    main() 