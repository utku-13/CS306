import pymysql
import os

# Veritabanı bağlantısı
def get_db_connection():
    connection = pymysql.connect(host='localhost',
                               user='root',
                               password='U147613d!',
                               database='RENTACAR')
    return connection

def read_sql_file(file_path):
    """Verilen SQL dosyasını okur ve içeriğini döndürür."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Dosya okuma hatası: {str(e)}")
        return None

def create_procedure_from_file(conn, proc_name, file_path):
    """Dosya içeriğini okuyarak stored procedure oluşturur."""
    # SQL dosyasını oku
    sql_content = read_sql_file(file_path)
    if not sql_content:
        print(f"{file_path} dosyası okunamadı.")
        return False
    
    # DELIMITER satırlarını kaldırma
    cleaned_sql = sql_content.replace("DELIMITER //", "").replace("DELIMITER ;", "").replace("//", ";")
    
    with conn.cursor() as cursor:
        try:
            # Eğer procedure zaten varsa, önce sil
            cursor.execute(f"DROP PROCEDURE IF EXISTS {proc_name}")
            # Yeni procedure'u oluştur
            cursor.execute(cleaned_sql)
            print(f"{proc_name} başarıyla oluşturuldu.")
            return True
        except Exception as e:
            print(f"Hata: {proc_name} oluşturulurken bir sorun oluştu: {str(e)}")
            return False

def main():
    try:
        conn = get_db_connection()
        print("Veritabanına bağlanıldı.")
        
        # Stored procedure dosyaları
        procedures = [
            ("CreateNewReservation", "scripts/stored_procedures/stored_procedure_1.sql"),
            ("GetBranchCars", "scripts/stored_procedures/stored_procedure_2.sql"),
            ("EmployeePerformanceReport", "scripts/stored_procedures/stored_procedure_3.sql"),
            ("GetCarDamageHistory", "scripts/stored_procedures/stored_procedure_4.sql")
        ]
        
        # Her procedure dosyasını yükle
        for proc_name, file_path in procedures:
            if os.path.exists(file_path):
                create_procedure_from_file(conn, proc_name, file_path)
            else:
                print(f"Hata: {file_path} dosyası bulunamadı.")
        
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