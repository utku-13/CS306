import pymysql

def get_db_connection():
    connection = pymysql.connect(host='localhost',
                               user='root',
                               password='U147613d!',
                               database='RENTACAR')
    return connection

def main():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # 1. Branch veri girişi
        cursor.execute("""
        INSERT INTO Branch VALUES
        (200, 'Kadikoy', '531-5600'),
        (201, 'Taksim', '555-0102'),
        (202, 'Besiktas', '533-2200'),
        (203, 'Uskudar', '532-9999'),
        (204, 'Sariyer', '534-1010'),
        (205, 'Levent', '535-3311'),
        (206, 'Atasehir', '538-4412'),
        (207, 'Bakirkoy', '536-7700'),
        (208, 'Maltepe', '531-5601'),
        (209, 'Sisli', '535-7788')
        """)
        print("Branch verileri eklendi.")
        
        # 2. Customer veri girişi
        cursor.execute("""
        INSERT INTO Customer VALUES
        (1001, 'Zeki', '554-1111', 1111),
        (1002, 'Aslı', '554-2222', 1112),
        (1003, 'Murat', '554-3333', 1113),
        (1004, 'Gülcan', '554-4444', 1114),
        (1005, 'Tuna', '554-5555', 1115),
        (1006, 'Yeliz', '554-6666', 1116),
        (1007, 'Kaan', '554-7777', 1117),
        (1008, 'Buse', '554-8888', 1118),
        (1009, 'Onur', '554-9999', 1119),
        (1010, 'Sıla', '554-0000', 1120)
        """)
        print("Customer verileri eklendi.")
        
        # 3. Employee veri girişi
        cursor.execute("""
        INSERT INTO Employee VALUES
        (300, 'Efe', '555-3001', 'Yonetici', 5000.00),
        (301, 'Sevgi', '555-3002', 'Satis', 3500.00),
        (302, 'Arda', '555-3003', 'Satis', 3400.00),
        (303, 'Hülya', '555-3004', 'Danisman', 2800.00),
        (304, 'Tekin', '555-3005', 'Yonetici', 5200.00),
        (305, 'Bilge', '555-3006', 'Satis', 3300.00),
        (306, 'Nazan', '555-3007', 'Danisman', 2900.00),
        (307, 'Tamer', '555-3008', 'Satis', 3600.00),
        (308, 'Ipek', '555-3009', 'Danisman', 2700.00),
        (309, 'Gökhan', '555-3010', 'Yonetici', 6000.00)
        """)
        print("Employee verileri eklendi.")
        
        # 4. Car veri girişi
        cursor.execute("""
        INSERT INTO Car VALUES
        (50, 'Toyota', 200, 'PLATE-050', 2020),
        (51, 'Honda', 200, 'PLATE-051', 2021),
        (52, 'Fiat', 201, 'PLATE-052', 2022),
        (53, 'Ford', 202, 'PLATE-053', 2023),
        (54, 'Opel', 203, 'PLATE-054', 2019),
        (55, 'BMW', 204, 'PLATE-055', 2018),
        (56, 'VW', 205, 'PLATE-056', 2017),
        (57, 'Renault', 206, 'PLATE-057', 2016),
        (58, 'Peugeot', 207, 'PLATE-058', 2021),
        (59, 'Hyundai', 208, 'PLATE-059', 2022)
        """)
        print("Car verileri eklendi.")
        
        # 5. Reservation veri girişi
        cursor.execute("""
        INSERT INTO Reservation VALUES
        (400, '2023-06-11'),
        (401, '2023-06-12'),
        (402, '2023-06-13'),
        (403, '2023-06-14'),
        (404, '2023-06-15'),
        (405, '2023-06-16'),
        (406, '2023-06-17'),
        (407, '2023-06-18'),
        (408, '2023-06-19'),
        (409, '2023-06-20')
        """)
        print("Reservation verileri eklendi.")
        
        # 6. RentalPeriod veri girişi
        cursor.execute("""
        INSERT INTO RentalPeriod VALUES
        (500, 400, '2023-07-01', '2023-07-02'),
        (501, 401, '2023-07-03', '2023-07-04'),
        (502, 402, '2023-07-05', '2023-07-06'),
        (503, 403, '2023-07-07', '2023-07-08'),
        (504, 404, '2023-07-09', '2023-07-10'),
        (505, 405, '2023-07-11', '2023-07-12'),
        (506, 406, '2023-07-13', '2023-07-14'),
        (507, 407, '2023-07-15', '2023-07-16'),
        (508, 408, '2023-07-17', '2023-07-18'),
        (509, 409, '2023-07-19', '2023-07-20')
        """)
        print("RentalPeriod verileri eklendi.")
        
        # 7. Employee_works_in_Branch veri girişi
        cursor.execute("""
        INSERT INTO Employee_works_in_Branch VALUES
        (300, 200),
        (301, 201),
        (302, 202),
        (303, 203),
        (304, 204),
        (305, 205),
        (306, 206),
        (307, 207),
        (308, 208),
        (309, 209)
        """)
        print("Employee_works_in_Branch verileri eklendi.")
        
        # 8. Branch_has_car veri girişi
        cursor.execute("""
        INSERT INTO Branch_has_car VALUES
        (50, 'Toyota', 200, 'PLATE-050', 2020),
        (51, 'Honda', 200, 'PLATE-051', 2021),
        (52, 'Fiat', 201, 'PLATE-052', 2022),
        (53, 'Ford', 202, 'PLATE-053', 2023),
        (54, 'Opel', 203, 'PLATE-054', 2019),
        (55, 'BMW', 204, 'PLATE-055', 2018),
        (56, 'VW', 205, 'PLATE-056', 2017),
        (57, 'Renault', 206, 'PLATE-057', 2016),
        (58, 'Peugeot', 207, 'PLATE-058', 2021),
        (59, 'Hyundai', 208, 'PLATE-059', 2022)
        """)
        print("Branch_has_car verileri eklendi.")
        
        # 9. Branch_makes_Employee_has_Insurance veri girişi
        cursor.execute("""
        INSERT INTO Branch_makes_Employee_has_Insurance VALUES
        (720, 'POL-720', '2023-01-01', '2023-12-31', 200, 300),
        (721, 'POL-721', '2023-01-01', '2023-12-31', 201, 301),
        (722, 'POL-722', '2023-01-01', '2023-12-31', 202, 302),
        (723, 'POL-723', '2023-01-01', '2023-12-31', 203, 303),
        (724, 'POL-724', '2023-01-01', '2023-12-31', 204, 304),
        (725, 'POL-725', '2023-01-01', '2023-12-31', 205, 305),
        (726, 'POL-726', '2023-01-01', '2023-12-31', 206, 306),
        (727, 'POL-727', '2023-01-01', '2023-12-31', 207, 307),
        (728, 'POL-728', '2023-01-01', '2023-12-31', 208, 308),
        (729, 'POL-729', '2023-01-01', '2023-12-31', 209, 309)
        """)
        print("Branch_makes_Employee_has_Insurance verileri eklendi.")
        
        # 10. Car_has_damage_record veri girişi
        cursor.execute("""
        INSERT INTO Car_has_damage_record VALUES
        (710, 50, 'Kaporta çizik', 300),
        (711, 51, 'Sol ayna kırık', 200),
        (712, 52, 'Ön tampon çatlak', 400),
        (713, 53, 'Lastik patlaması', 150),
        (714, 54, 'Cam çatlağı', 350),
        (715, 55, 'Far bozuk', 250),
        (716, 56, 'Motor arızası', 2000),
        (717, 57, 'Arka tampon çizik', 100),
        (718, 58, 'Klima bozuk', 500),
        (719, 59, 'Vites sorunu', 800)
        """)
        print("Car_has_damage_record verileri eklendi.")
        
        # 11. Car_has_insurance veri girişi
        cursor.execute("""
        INSERT INTO Car_has_insurance VALUES
        (700, 50, 'CINS-700', '2023-01-01', '2023-12-31'),
        (701, 51, 'CINS-701', '2023-01-01', '2023-12-31'),
        (702, 52, 'CINS-702', '2023-01-01', '2023-12-31'),
        (703, 53, 'CINS-703', '2023-01-01', '2023-12-31'),
        (704, 54, 'CINS-704', '2023-01-01', '2023-12-31'),
        (705, 55, 'CINS-705', '2023-01-01', '2023-12-31'),
        (706, 56, 'CINS-706', '2023-01-01', '2023-12-31'),
        (707, 57, 'CINS-707', '2023-01-01', '2023-12-31'),
        (708, 58, 'CINS-708', '2023-01-01', '2023-12-31'),
        (709, 59, 'CINS-709', '2023-01-01', '2023-12-31')
        """)
        print("Car_has_insurance verileri eklendi.")
        
        # 12. Reservation_includes_car veri girişi
        cursor.execute("""
        INSERT INTO Reservation_includes_car VALUES
        (400, 50),
        (401, 51),
        (402, 52),
        (403, 53),
        (404, 54),
        (405, 55),
        (406, 56),
        (407, 57),
        (408, 58),
        (409, 59)
        """)
        print("Reservation_includes_car verileri eklendi.")
        
        # 13. Customer_makes_reservation veri girişi
        cursor.execute("""
        INSERT INTO Customer_makes_reservation VALUES
        (1001, 400),
        (1002, 401),
        (1003, 402),
        (1004, 403),
        (1005, 404),
        (1006, 405),
        (1007, 406),
        (1008, 407),
        (1009, 408),
        (1010, 409)
        """)
        print("Customer_makes_reservation verileri eklendi.")
        
        # 14. Receipt veri girişi
        cursor.execute("""
        INSERT INTO Receipt VALUES
        (600, 250, '1'),
        (601, 300, '2'),
        (602, 180, '1'),
        (603, 500, '1'),
        (604, 220, '2'),
        (605, 280, '2'),
        (606, 320, '1'),
        (607, 450, '2'),
        (608, 200, '1'),
        (609, 400, '2')
        """)
        print("Receipt verileri eklendi.")
        
        # 15. Customer_Owns_Reservation_Needs_Receipt veri girişi
        cursor.execute("""
        INSERT INTO Customer_Owns_Reservation_Needs_Receipt VALUES
        (600, 400, 1001, 250, 1),
        (601, 401, 1002, 300, 2),
        (602, 402, 1003, 180, 1),
        (603, 403, 1004, 500, 1),
        (604, 404, 1005, 220, 2),
        (605, 405, 1006, 280, 2),
        (606, 406, 1007, 320, 1),
        (607, 407, 1008, 450, 2),
        (608, 408, 1009, 200, 1),
        (609, 409, 1010, 400, 2)
        """)
        print("Customer_Owns_Reservation_Needs_Receipt verileri eklendi.")
        
        # 16. Reservation_has_rental_period veri girişi
        cursor.execute("""
        INSERT INTO Reservation_has_rental_period VALUES
        (500, 400, '2023-07-01', '2023-07-02'),
        (501, 401, '2023-07-03', '2023-07-04'),
        (502, 402, '2023-07-05', '2023-07-06'),
        (503, 403, '2023-07-07', '2023-07-08'),
        (504, 404, '2023-07-09', '2023-07-10'),
        (505, 405, '2023-07-11', '2023-07-12'),
        (506, 406, '2023-07-13', '2023-07-14'),
        (507, 407, '2023-07-15', '2023-07-16'),
        (508, 408, '2023-07-17', '2023-07-18'),
        (509, 409, '2023-07-19', '2023-07-20')
        """)
        print("Reservation_has_rental_period verileri eklendi.")
        
        # Değişiklikleri kaydet
        conn.commit()
        print("Tüm veriler başarıyla eklendi!")
        
    except Exception as e:
        conn.rollback()
        print(f"Hata: {e}")
    finally:
        conn.close()
        print("Veritabanı bağlantısı kapatıldı.")

if __name__ == "__main__":
    main() 