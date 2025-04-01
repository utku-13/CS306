import pymysql

def get_db_connection():
    connection = pymysql.connect(host='localhost',
                               user='root',
                               password='U147613d!',
                               database='RENTACAR')
    return connection

# Tablo oluşturma SQL komutları
create_tables = """
CREATE TABLE Customer (
    cus_id INT,
    name VARCHAR(100),
    phone_num VARCHAR(20),
    licence_num INT,
    PRIMARY KEY (cus_id)
);

CREATE TABLE Branch(
    bra_id INT,
    location VARCHAR(23),
    phone_number VARCHAR(20),
    Primary Key(bra_id)
);

CREATE TABLE Employee (
    emp_id INT,
    name VARCHAR(100),
    phone_num VARCHAR(20),
    position VARCHAR(50),
    salary DECIMAL(10,2),
    PRIMARY KEY (emp_id)
);

CREATE TABLE Car(
    car_id INT,
    brand VARCHAR(25),
    branch_id INT,
    plate_number VARCHAR(25),
    model INT,
    Primary Key(car_id),
    Foreign Key (branch_id) references Branch(bra_id)
);

CREATE TABLE Reservation (
    res_id INT,
    res_date DATE,
    PRIMARY KEY (res_id)
);

CREATE TABLE RentalPeriod (
    rent_id INT,
    res_id INT,
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (rent_id),
    Foreign Key (res_id) references Reservation(res_id)
);

CREATE TABLE Employee_works_in_Branch(
    emp_id INT,
    branch_id INT,
    PRIMARY KEY (emp_id),
    foreign key (branch_id) references Branch(bra_id),
    foreign key (emp_id) references Employee(emp_id)
);

CREATE TABLE Branch_makes_Employee_has_Insurance(
    ins_id INT,
    pol_num VARCHAR(50),
    start_date DATE,
    end_date DATE,
    branch_id INT,
    emp_id INT,
    PRIMARY KEY (ins_id),
    foreign key (emp_id) references Employee_works_in_Branch(emp_id),
    foreign key (branch_id) references Branch(bra_id)
);

CREATE TABLE Branch_has_car(
    car_id INT,
    brand VARCHAR(25),
    branch_id INT,
    plate_number VARCHAR(25),
    model INT,
    Primary Key(car_id),
    Foreign Key (branch_id) references Branch(bra_id)
);

CREATE TABLE Car_has_damage_record(
    damage_id INT,
    car_id INT,
    description VARCHAR(200),
    repair_cost DECIMAL(10,2),
    PRIMARY KEY (damage_id),
    Foreign Key (car_id) references Branch_has_car(car_id)
);

CREATE TABLE Car_has_insurance(
    cins_id INT,
    car_id INT,
    pol_num VARCHAR(50),
    start_date DATE,
    end_date DATE,
    PRIMARY KEY (car_id),
    Foreign Key (car_id) references Branch_has_car(car_id)
);

CREATE TABLE Reservation_includes_car(
    res_id INT,
    car_id INT,
    PRIMARY KEY (res_id, car_id),
    Foreign Key (car_id) references Branch_has_car(car_id),
    Foreign Key (res_id) references Reservation(res_id)
);

CREATE TABLE Customer_makes_reservation (
    customer_id INT,
    res_id INT,
    Primary Key(res_id, customer_id),
    Foreign Key (customer_id) references Customer(cus_id),
    Foreign Key (res_id) references Reservation(res_id)
);

CREATE TABLE Receipt (
    rec_id INT,
    amount INT,
    payment_method VARCHAR(20),
    PRIMARY KEY (rec_id)
);

CREATE TABLE Customer_Owns_Reservation_Needs_Receipt(
    rec_id INT,
    res_id INT,
    customer_id INT,
    amount INT,
    payment_method INT,
    Primary Key(rec_id, res_id, customer_id),
    Foreign Key (customer_id) references Customer(cus_id),
    Foreign Key (res_id) references Reservation(res_id),
    Foreign Key (rec_id) references Receipt(rec_id)
);

CREATE TABLE Reservation_has_rental_period(
    rent_id INT,
    res_id INT,
    start_date DATE,
    end_date DATE,
    primary key(rent_id),
    Foreign Key (res_id) references Reservation(res_id)
);
"""

# Veri ekleme SQL komutları
insert_data = """
-- Şube verileri
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
(209, 'Sisli', '535-7788');

-- Müşteri verileri
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
(1010, 'Sıla', '554-0000', 1120);

-- Çalışan verileri
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
(309, 'Gökhan', '555-3010', 'Yonetici', 6000.00);

-- Araç verileri
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
(59, 'Hyundai', 208, 'PLATE-059', 2022);

-- Rezervasyon verileri
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
(409, '2023-06-20');

-- Kiralama periyodu verileri
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
(509, 409, '2023-07-19', '2023-07-20');

-- Çalışan-Şube ilişkisi
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
(309, 209);

-- Şube araçları verileri
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
(59, 'Hyundai', 208, 'PLATE-059', 2022);

-- Çalışan sigortası verileri
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
(729, 'POL-729', '2023-01-01', '2023-12-31', 209, 309);

-- Araç hasar kayıtları
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
(719, 59, 'Vites sorunu', 800);

-- Araç sigorta verileri
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
(709, 59, 'CINS-709', '2023-01-01', '2023-12-31');

-- Rezervasyon-Araç ilişkisi
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
(409, 59);

-- Müşteri-Rezervasyon ilişkisi
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
(1010, 409);

-- Fatura verileri
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
(609, 400, '2');

-- Müşteri-Rezervasyon-Fatura ilişkisi
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
(609, 409, 1010, 400, 2);

-- Rezervasyon-Kiralama Periyodu ilişkisi
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
(509, 409, '2023-07-19', '2023-07-20');
"""

def execute_sql_script(conn, sql_script):
    """Verilen SQL scriptini çalıştırır. Her bir komut ayrı ayrı çalıştırılır."""
    cursor = conn.cursor()
    
    # SQL komutlarını ayır
    commands = sql_script.split(';')
    
    for command in commands:
        # Boş komutları atla
        if command.strip() == '' or command.strip().startswith('--'):
            continue
            
        try:
            cursor.execute(command)
            print(f"Komut başarıyla çalıştırıldı: {command[:50]}...")
        except Exception as e:
            print(f"Hata: {str(e)}")
            print(f"Komut: {command[:100]}...")
    
    conn.commit()
    cursor.close()

def main():
    try:
        # Veritabanına bağlanma
        conn = get_db_connection()
        print("Veritabanına başarıyla bağlanıldı!")
        
        # İlk olarak var olan tabloları temizle
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        
        if tables:
            print("Var olan tablolar temizleniyor...")
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            
            for table in tables:
                table_name = list(table.values())[0]
                cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
                print(f"- {table_name} tablosu silindi.")
                
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
            conn.commit()
        
        # Tabloları oluştur
        print("\nYeni tablolar oluşturuluyor...")
        execute_sql_script(conn, create_tables)
        
        # Verileri ekle
        print("\nVeriler ekleniyor...")
        cursor = conn.cursor()
        
        # SQL komutlarını ayır ve her birini ayrı ayrı çalıştır
        statements = insert_data.split(';')
        
        for statement in statements:
            # Boş veya yorum satırlarını atla
            if statement.strip() == '' or statement.strip().startswith('--'):
                continue
                
            try:
                cursor.execute(statement)
                print(f"Veri eklendi: {statement[:50]}...")
            except Exception as e:
                print(f"Veri eklenirken hata: {str(e)}")
                print(f"SQL: {statement[:100]}...")
        
        conn.commit()
        
        print("\nTüm işlemler tamamlandı!")
        
    except Exception as e:
        print(f"Genel Hata: {str(e)}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("\nVeritabanı bağlantısı kapatıldı.")

if __name__ == "__main__":
    main() 