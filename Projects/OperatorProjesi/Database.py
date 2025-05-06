import sqlite3
import time

def execute_db_operation(operation_func):
    conn = sqlite3.connect("overall_dataSet.db")
    try:
        cursor = conn.cursor()
        result = operation_func(cursor)
        conn.commit()
        return result
    finally:
        conn.close()

def addBalance(tc, miktar):
    def _add_balance(cursor):
        cursor.execute("SELECT * FROM user_packages WHERE tc=?", (tc,))
        user_package = cursor.fetchone()
        
        if not user_package:
            print(f"TC: {tc} numaralı kullanıcıya ait paket bilgisi bulunamadı!")
            return False
        cursor.execute("PRAGMA table_info(user_packages)")
        columns = cursor.fetchall()
        bakiye_index = None
        
        for i, col in enumerate(columns):
            if col[1].lower() in ['bakiye', 'balance']:
                bakiye_index = i
                break
        
        if bakiye_index is None:
            print("Bakiye sütunu bulunamadı!")
            return False
        
        mevcut_bakiye = float(user_package[bakiye_index]) if user_package[bakiye_index] is not None else 0.0
        yeni_bakiye = mevcut_bakiye + float(miktar)
        cursor.execute("UPDATE user_packages SET bakiye=? WHERE tc=?", (yeni_bakiye, tc))
        
        if cursor.rowcount > 0:
            print(f"Bakiye güncellendi! Eski bakiye: {mevcut_bakiye} TL, Yeni bakiye: {yeni_bakiye} TL")
            return True
        else:
            print("Bakiye güncellenirken bir sorun oluştu!")
            return False
    
    return execute_db_operation(_add_balance)

def buyPackage(tc, paket_id):
    def _buy_package(cursor):
        cursor.execute("SELECT * FROM users WHERE tc=?", (tc,))
        user = cursor.fetchone()
        
        if not user:
            print(f"TC: {tc} numaralı kullanıcı bulunamadı!")
            return False

        cursor.execute("PRAGMA table_info(users)")
        columns = cursor.fetchall()
        paket_id_index = None
        
        for i, col in enumerate(columns):
            if col[1].lower() in ['paket_id', 'paketid']:
                paket_id_index = i
                break
        
        if paket_id_index is None:
            print("users tablosunda paket_id sütunu bulunamadı!")
            return False

        current_paket_id = user[paket_id_index]
        if current_paket_id is not None and current_paket_id != "":
            print(f"Bu kullanıcının zaten bir paketi var! Paket ID: {current_paket_id}")
            return False
        
        cursor.execute("UPDATE users SET paket_id=? WHERE tc=?", (paket_id, tc))
        
        if cursor.rowcount > 0:
            cursor.execute("SELECT * FROM user_packages WHERE tc=?", (tc,))
            existing_package = cursor.fetchone()
            
            if existing_package:
                cursor.execute("UPDATE user_packages SET paket_id=? WHERE tc=?", (paket_id, tc))
            else:
                cursor.execute("SELECT * FROM packages WHERE paket_id=?", (paket_id,))
                paket_bilgisi = cursor.fetchone()
                
                if paket_bilgisi:
                    cursor.execute("PRAGMA table_info(packages)")
                    package_columns = cursor.fetchall()
                    
                    internet_index = dakika_index = sms_index = fiyat_index = None
                    for i, col in enumerate(package_columns):
                        col_name = col[1].lower()
                        if col_name in ['internet', 'internet_gb']:
                            internet_index = i
                        elif col_name in ['dakika', 'konusma_dk', 'konusma']:
                            dakika_index = i
                        elif col_name in ['sms', 'mesaj']:
                            sms_index = i
                        elif col_name in ['fiyat', 'ucret']:
                            fiyat_index = i
                    
                    internet_miktari = paket_bilgisi[internet_index] if internet_index is not None else 0
                    dakika_miktari = paket_bilgisi[dakika_index] if dakika_index is not None else 0
                    sms_miktari = paket_bilgisi[sms_index] if sms_index is not None else 0
                    bakiye = 0 
                    
                    cursor.execute("""
                        INSERT INTO user_packages (tc, paket_id, internet, dakika, sms, bakiye)
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (tc, paket_id, internet_miktari, dakika_miktari, sms_miktari, bakiye))
            
            cursor.execute("SELECT * FROM packages WHERE paket_id=?", (paket_id,))
            paket = cursor.fetchone()
            
            paket_adi = "Bilinmeyen Paket"
            if paket:
                cursor.execute("PRAGMA table_info(packages)")
                package_columns = cursor.fetchall()
                
                for i, col in enumerate(package_columns):
                    if col[1].lower() in ['paket_adi', 'adi', 'name', 'paket']:
                        paket_adi = paket[i]
                        break
            
            print(f"Paket satın alma işlemi başarılı! Satın alınan paket: {paket_adi}")
            return True
        else:
            print("Paket satın alırken bir sorun oluştu!")
            return False
    
    return execute_db_operation(_buy_package)

def deleteUser(tc):
    def _delete_user(cursor):
        cursor.execute("SELECT * FROM users WHERE tc=?", (tc,))
        user = cursor.fetchone()
        
        if not user:
            print(f"TC: {tc} numaralı kullanıcı bulunamadı!")
            return False
        
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        isim = ""
        soyisim = ""
        
        cursor.execute("PRAGMA table_info(users)")
        user_columns = cursor.fetchall()
        isim_index = soyisim_index = None
        
        for i, col in enumerate(user_columns):
            if col[1].lower() in ['isim', 'ad', 'name']:
                isim_index = i
            elif col[1].lower() in ['soyisim', 'soyad', 'surname']:
                soyisim_index = i
        
        if isim_index is not None and user[isim_index]:
            isim = user[isim_index]
        if soyisim_index is not None and user[soyisim_index]:
            soyisim = user[soyisim_index]
        
        kullanici_bilgisi = f"{isim} {soyisim}" if isim or soyisim else f"TC: {tc}"
    
        cursor.execute("BEGIN TRANSACTION")
        
        silinen_kayit_sayisi = 0
        try:
            for table in tables:
                table_name = table[0]
                cursor.execute(f"PRAGMA table_info({table_name})")
                columns = cursor.fetchall()
            
                tc_sutunu_var = False
                for col in columns:
                    if col[1].lower() in ['tc', 'tc_kimlik', 'tcno']:
                        tc_sutunu_var = True
                        break
                
                if tc_sutunu_var:
                    cursor.execute(f"DELETE FROM {table_name} WHERE tc=?", (tc,))
                    silinen_kayit_sayisi += cursor.rowcount
            
            cursor.execute("COMMIT")
            
            if silinen_kayit_sayisi > 0:
                print(f"{kullanici_bilgisi} kullanıcısı {silinen_kayit_sayisi} tablodan başarıyla silindi.")
                return True
            else:
                print(f"İlgili kullanıcı için herhangi bir kayıt silinemedi.")
                return False
            
        except sqlite3.Error as e:
            cursor.execute("ROLLBACK")
            print(f"Silme işlemi sırasında bir hata oluştu: {e}")
            return False
    
    return execute_db_operation(_delete_user)
