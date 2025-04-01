from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
from pymysql.cursors import DictCursor
import traceback

app = Flask(__name__)
app.secret_key = 'arabakiralama123'

# Database connection function
def get_db_connection():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='',  # Veritabanı şifrenizi buraya yazın
                                 database='RENTACAR',
                                 cursorclass=DictCursor)
    return connection

# Ana sayfa
@app.route('/')
def index():
    return render_template('index.html')

# 1. Rezervasyon Yönetimi Modülü
@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        reservation_id = request.form['reservation_id']
        customer_id = request.form['customer_id']
        car_id = request.form['car_id']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.callproc('CreateNewReservation', (reservation_id, customer_id, car_id, start_date, end_date))
                conn.commit()
                flash('Rezervasyon başarıyla oluşturuldu!', 'success')
        except Exception as e:
            flash(f'Hata: {str(e)}', 'error')
        finally:
            conn.close()
            
        return redirect(url_for('reservation'))
    
    return render_template('reservation_form.html')

# 2. Araç Takip Modülü
@app.route('/branch_cars', methods=['GET', 'POST'])
def branch_cars():
    cars = []
    if request.method == 'POST':
        branch_id = request.form['branch_id']
        conn = None
        
        try:
            conn = get_db_connection()
            # Manual SQL sorgusu ile kontrol et
            with conn.cursor() as cursor:
                # Önce doğrudan SQL sorgusu ile deneyelim (Branch_has_car tablosundan)
                cursor.execute("""
                    SELECT car_id, brand, plate_number, model
                    FROM Branch_has_car
                    WHERE branch_id = %s
                """, (branch_id,))
                cars = cursor.fetchall()
                
                # Eğer Branch_has_car tablosunda sonuç yoksa, Car tablosundan deneyelim
                if not cars:
                    cursor.execute("""
                        SELECT car_id, brand, plate_number, model
                        FROM Car
                        WHERE branch_id = %s
                    """, (branch_id,))
                    cars = cursor.fetchall()
                    
                if not cars:
                    flash(f'Şube ID {branch_id} için araç bulunamadı.', 'error')
                else:
                    flash(f'Şube ID {branch_id} için {len(cars)} araç bulundu.', 'success')
        except Exception as e:
            flash(f'Hata: {str(e)}', 'error')
        finally:
            if conn:
                conn.close()
    
    return render_template('branch_cars_form.html', cars=cars)

# 3. Çalışan Yönetim Modülü
@app.route('/employee_performance', methods=['GET', 'POST'])
def employee_performance():
    employee = None
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        conn = None
        
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.callproc('EmployeePerformanceReport', (emp_id,))
                result = cursor.fetchall()
                if result:
                    employee = result[0]
        except Exception as e:
            flash(f'Hata: {str(e)}', 'error')
        finally:
            if conn:
                conn.close()
    
    return render_template('employee_performance_form.html', employee=employee)

# 4. Hasar/Bakım Takip Modülü
@app.route('/car_damage', methods=['GET', 'POST'])
def car_damage():
    damages = []
    if request.method == 'POST':
        car_id = request.form['car_id']
        conn = None
        
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                cursor.callproc('GetCarDamageHistory', (car_id,))
                damages = cursor.fetchall()
        except Exception as e:
            flash(f'Hata: {str(e)}', 'error')
        finally:
            if conn:
                conn.close()
    
    return render_template('car_damage_form.html', damages=damages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False) 