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
        
        print("\nTüm tablolar başarıyla oluşturuldu!")
        
    except Exception as e:
        print(f"Genel Hata: {str(e)}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()
            print("\nVeritabanı bağlantısı kapatıldı.")

if __name__ == "__main__":
    main() 