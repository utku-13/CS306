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

-- Bildirimler tablosu (damage_record_notification trigger için)
CREATE TABLE Notifications (
    notification_id INT AUTO_INCREMENT,
    car_id INT,
    message VARCHAR(255),
    date DATETIME,
    is_read BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (notification_id)
);

-- Maaş değişikliği log tablosu (log_salary_changes trigger için)
CREATE TABLE SalaryChangeLog (
    log_id INT AUTO_INCREMENT,
    emp_id INT,
    old_salary DECIMAL(10,2),
    new_salary DECIMAL(10,2),
    change_date DATETIME,
    PRIMARY KEY (log_id),
    FOREIGN KEY (emp_id) REFERENCES Employee(emp_id)
); 