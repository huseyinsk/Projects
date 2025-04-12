import sqlite3
import time

def execute_db_operation(operation_func):
    """Simple function to execute a database operation with basic retry logic."""
    max_attempts = 3
    for attempt in range(max_attempts):
        try:
            conn = sqlite3.connect("kullanicilar.db", timeout=5)
            conn.isolation_level = None
            cursor = conn.cursor()
            
            result = operation_func(cursor)
            
            conn.close()
            return result
        except sqlite3.Error as e:
            if "database is locked" in str(e) and attempt < max_attempts - 1:
                time.sleep(0.5)
                continue
            print(f"Veritabanı hatası: {e}")
            if conn:
                try:
                    conn.close()
                except:
                    pass
            return None

def init_db():
    def _create_table(cursor):
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS kullanicilar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Ad TEXT,
            Soyad TEXT,
            TC TEXT UNIQUE,
            Numara TEXT,
            Paket TEXT
        )
        """)
        return True
    
    execute_db_operation(_create_table)

init_db()

eski_paket = ""

def add_package_to_newUser(ad, soyad, tc, numara, newPackage):
    def _add_package(cursor):
        try:
            cursor.execute("SELECT Paket FROM kullanicilar WHERE TC=?", (tc,))
            user = cursor.fetchone()
            
            if not user:
                print(f"Hata: TC numarası {tc} olan kullanıcı bulunamadı.")
                return False
            
            if not user[0] or user[0] == "None" or user[0].strip() == "":
                cursor.execute("UPDATE kullanicilar SET Paket=? WHERE TC=?", (newPackage, tc))
                print(f"{ad} {soyad} kullanıcısına {newPackage} paketi başarıyla eklendi.")
                return True
            else:
                print(f"Hata: {ad} {soyad} kullanıcısının zaten bir paketi var: {user[0]}")
                print("Paketi değiştirmek için Paket Güncelle fonksiyonunu kullanabilirsiniz.")
                return False
        except Exception as e:
            print(f"Paket eklenirken hata oluştu: {e}")
            return False
    
    return execute_db_operation(_add_package)

def delete_user(ad, soyad, tc):
    def _delete_user(cursor):
        cursor.execute("DELETE FROM kullanicilar WHERE TC=?", (tc,))
        if cursor.rowcount > 0:
            print(f"{ad} {soyad} kullanıcısı başarıyla silindi.")
            return True
        else:
            print("Kullanıcı bulunamadı. Silme işlemi yapılmadı.")
            return False
    
    return execute_db_operation(_delete_user)

def get_user_package(ad, soyad, tc):
    global eski_paket
    
    def _get_package(cursor):
        try:
            cursor.execute("SELECT Paket FROM kullanicilar WHERE TC=?", (tc,))
            user = cursor.fetchone()
            
            if not user:
                print(f"TC: {tc} numaralı kullanıcı bulunamadı.")
                return None
            
            paket = user[0]
            if not paket or paket == "None" or paket.strip() == "":
                print("Kullanıcının henüz bir paketi yok.")
                return ""
            
            return paket
            
        except Exception as e:
            print(f"Paket bilgisi alınırken hata oluştu: {e}")
            return None
    
    try:
        result = execute_db_operation(_get_package)
        if result is not None:
            eski_paket = result
        return result
    except Exception as e:
        print(f"İşlem sırasında hata oluştu: {e}")
        return None

def update_package(ad, soyad, tc, numara, eski_paket, yeni_paket):
    def _update_package(cursor):
        cursor.execute("UPDATE kullanicilar SET Paket=? WHERE TC=?", (yeni_paket, tc))
        if cursor.rowcount > 0:
            print(f"{ad} {soyad} kullanıcısının paketi {yeni_paket} ile başarıyla güncellendi.")
            return True
        else:
            print(f"Hata: TC: {tc} numaralı kullanıcı bulunamadı veya pakette değişiklik olmadı.")
            return False
    
    return execute_db_operation(_update_package)

def display_user(ad, soyad, tc):
    def _display_user(cursor):
        cursor.execute("SELECT * FROM kullanicilar WHERE TC=?", (tc,))
        user = cursor.fetchone()
        if user:
            print("--- KULLANICI BİLGİLERİ ---")
            print(f"ID: {user[0]}")
            print(f"Ad: {user[1]}")
            print(f"Soyad: {user[2]}")
            print(f"TC: {user[3]}")
            print(f"Numara: {user[4]}")
            print(f"Paket: {user[5] if user[5] else 'Paket yok'}")
            print("-------------------------")
            return user
        else:
            print(f"{ad} {soyad} isimli kullanıcı bulunamadı.")
            return None
    
    return execute_db_operation(_display_user)
