## Ek paketleri içeren dosya
import sqlite3

def extraPackages(tc):
    print("Ek Paketler: \n1. Ek Paket 1: 2 GB internet (20TL) \n2. Ek Paket 2: 100 Dakika(15TL) \n3. Ek Paket 3: 100 SMS(15TL)")
    exPack = input("Lütfen yukarıdaki ek paketlerden birini, numarasını yazarak seçiniz: ").lower()
    while exPack not in ["1", "2", "3"]:
        print("Lütfen geçerli bir ek paket seçiniz.")
        exPack = input("Lütfen yukarıdaki ek paketlerden birini, numarasını yazarak seçiniz: ").lower()

    try:
        conn = sqlite3.connect("overall_dataSet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_packages WHERE tc=?", (tc,))
        user_package = cursor.fetchone()

        if not user_package:
            print("Kullanıcı paket bilgisi bulunamadı! Önce bir paket seçmelisiniz.")
            conn.close()
            return
        try:
            cursor.execute("PRAGMA table_info(user_packages)")
            columns = cursor.fetchall()
            bakiye_index = None
            
            for i, col in enumerate(columns):
                if col[1].lower() == 'bakiye':
                    bakiye_index = i
                    break
            
            if bakiye_index is None:
                for i, col in enumerate(columns):
                    print(f"Sütun {i}: {col[1]}")
                print("Bakiye sütunu bulunamadı!")
                conn.close()
                return

            current_balance = float(user_package[bakiye_index]) if user_package[bakiye_index] is not None else 0.0
            
            required_payment = 0
            if exPack == "1":
                required_payment = 20
                print("2 GB internet paketini seçtiniz. Ücret: 20TL")
            elif exPack == "2":
                required_payment = 15
                print("100 Dakika paketini seçtiniz. Ücret: 15TL")
            elif exPack == "3":
                required_payment = 15
                print("100 SMS paketini seçtiniz. Ücret: 15TL")

            if current_balance < required_payment:
                print(f"Bakiyeniz yetersiz! Mevcut bakiye: {current_balance}TL, Gerekli bakiye: {required_payment}TL")
                print("Lütfen bakiye yükleyip tekrar deneyiniz.")
                conn.close()
                return

            cursor.execute("BEGIN TRANSACTION")
            
            new_balance = current_balance - required_payment
            cursor.execute(f"UPDATE user_packages SET bakiye=? WHERE tc=?", (new_balance, tc))
            
            if exPack == "1":
                cursor.execute("UPDATE user_packages SET internet = internet + 2 WHERE tc=?", (tc,))
                print("2 GB internet hakkınız eklendi!")
            elif exPack == "2":
                cursor.execute("UPDATE user_packages SET dakika = dakika + 100 WHERE tc=?", (tc,))
                print("100 dakika konuşma hakkınız eklendi!")
            elif exPack == "3":
                cursor.execute("UPDATE user_packages SET sms = sms + 100 WHERE tc=?", (tc,))
                print("100 SMS hakkınız eklendi!")

            conn.commit()
            print(f"İşlem başarılı! Yeni bakiyeniz: {new_balance}TL")
            
        except sqlite3.Error as e:
            if 'conn' in locals():
                conn.rollback()
            print(f"İşlem sırasında bir hata oluştu: {e}")

    except sqlite3.Error as e:
        print(f"Veritabanı hatası: {e}")
    finally:
        if 'conn' in locals():
            conn.close()


def extraFullPackages(tc):
    print("Ek tam paketler güncel fiyatlarının iki katına satılmaktadır.\nPaket içeriği ve fiyatı aşağıdaki gibidir:")
    print("1. Iron Paket(40TL)\n2. Bronze Paket(60TL)\n3. Silver Paket(80TL)\n4. Gold Paket(100TL)\n5. Platinum Paket(120TL)\n6. Diamond Paket(140TL)\n7. VIP Paket(160TL)")
    exFullPack = input("Lütfen yukarıdaki ek tam paketlerden birini, numarasını yazarak seçiniz: ").lower()
    while exFullPack not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Lütfen geçerli bir ek tam paket seçiniz.")
        exFullPack = input("Lütfen yukarıdaki ek tam paketlerden birini, numarasını yazarak seçiniz: ").lower()
    
    try:
        conn = sqlite3.connect("overall_dataSet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user_packages WHERE tc=?", (tc,))
        user_package = cursor.fetchone()

        if not user_package:
            print("Kullanıcı paket bilgisi bulunamadı! Önce bir paket seçmelisiniz.")
            conn.close()
            return

        try:
            cursor.execute("PRAGMA table_info(user_packages)")
            columns = cursor.fetchall()
            bakiye_index = None
            
            for i, col in enumerate(columns):
                if col[1].lower() == 'bakiye':
                    bakiye_index = i
                    break
            
            if bakiye_index is None:
                for i, col in enumerate(columns):
                    print(f"Sütun {i}: {col[1]}")
                print("Bakiye sütunu bulunamadı!")
                conn.close()
                return

            current_balance = float(user_package[bakiye_index]) if user_package[bakiye_index] is not None else 0.0
            
            required_payment = 0
            paket_id = 0
            package_name = ""
            
            if exFullPack == "1":  
                required_payment = 40
                paket_id = 1
                package_name = "Iron"
                print("Iron Paketi seçtiniz. Ücret: 40TL")
            elif exFullPack == "2":  
                required_payment = 60
                paket_id = 2
                package_name = "Bronze"
                print("Bronze Paketi seçtiniz. Ücret: 60TL")
            elif exFullPack == "3":  
                required_payment = 80
                paket_id = 3
                package_name = "Silver"
                print("Silver Paketi seçtiniz. Ücret: 80TL")
            elif exFullPack == "4":  
                required_payment = 100
                paket_id = 4
                package_name = "Gold"
                print("Gold Paketi seçtiniz. Ücret: 100TL")
            elif exFullPack == "5":  
                required_payment = 120
                paket_id = 5
                package_name = "Platinum"
                print("Platinum Paketi seçtiniz. Ücret: 120TL")
            elif exFullPack == "6":  
                required_payment = 140
                paket_id = 6
                package_name = "Diamond"
                print("Diamond Paketi seçtiniz. Ücret: 140TL")
            elif exFullPack == "7":  
                required_payment = 160
                paket_id = 7
                package_name = "VIP"
                print("VIP Paketi seçtiniz. Ücret: 160TL")

            if current_balance < required_payment:
                print(f"Bakiyeniz yetersiz! Mevcut bakiye: {current_balance}TL, Gerekli bakiye: {required_payment}TL")
                print("Lütfen bakiye yükleyip tekrar deneyiniz.")
                conn.close()
                return

            cursor.execute("BEGIN TRANSACTION")
            
            new_balance = current_balance - required_payment
            cursor.execute(f"UPDATE user_packages SET bakiye=? WHERE tc=?", (new_balance, tc))
            
            cursor.execute("UPDATE user_packages SET paket_id=? WHERE tc=?", (paket_id, tc))
            
            cursor.execute("SELECT * FROM packages WHERE paket_id=?", (paket_id,))
            paket_bilgisi = cursor.fetchone()
            
            if paket_bilgisi:
                cursor.execute("PRAGMA table_info(packages)")
                package_columns = cursor.fetchall()
                
                internet_index = dakika_index = sms_index = None
                
                for i, col in enumerate(package_columns):
                    if col[1].lower() in ['internet', 'internet_gb']:
                        internet_index = i
                    elif col[1].lower() in ['dakika', 'konusma_dk']:
                        dakika_index = i
                    elif col[1].lower() in ['sms', 'mesaj']:
                        sms_index = i
                
                internet_miktari = int(paket_bilgisi[internet_index]) if internet_index is not None and paket_bilgisi[internet_index] is not None else 0
                dakika_miktari = int(paket_bilgisi[dakika_index]) if dakika_index is not None and paket_bilgisi[dakika_index] is not None else 0
                sms_miktari = int(paket_bilgisi[sms_index]) if sms_index is not None and paket_bilgisi[sms_index] is not None else 0
                
                cursor.execute("UPDATE user_packages SET internet=?, dakika=?, sms=? WHERE tc=?", 
                              (internet_miktari, dakika_miktari, sms_miktari, tc))
            else:
                if exFullPack == "1": 
                    cursor.execute("UPDATE user_packages SET internet=5, dakika=500, sms=250 WHERE tc=?", (tc,))
                elif exFullPack == "2": 
                    cursor.execute("UPDATE user_packages SET internet=10, dakika=750, sms=500 WHERE tc=?", (tc,))
                elif exFullPack == "3":  
                    cursor.execute("UPDATE user_packages SET internet=15, dakika=1000, sms=750 WHERE tc=?", (tc,))
                elif exFullPack == "4": 
                    cursor.execute("UPDATE user_packages SET internet=20, dakika=1500, sms=1000 WHERE tc=?", (tc,))
                elif exFullPack == "5":  
                    cursor.execute("UPDATE user_packages SET internet=25, dakika=2000, sms=1500 WHERE tc=?", (tc,))
                elif exFullPack == "6":  
                    cursor.execute("UPDATE user_packages SET internet=35, dakika=3000, sms=2000 WHERE tc=?", (tc,))
                elif exFullPack == "7":  
                    cursor.execute("UPDATE user_packages SET internet=50, dakika=5000, sms=3000 WHERE tc=?", (tc,))

            conn.commit()
            print(f"İşlem başarılı! {package_name} paketi hesabınıza tanımlandı.")
            print(f"Yeni bakiyeniz: {new_balance}TL")
            
        except sqlite3.Error as e:
            if 'conn' in locals():
                conn.rollback()
            print(f"İşlem sırasında bir hata oluştu: {e}")

    except sqlite3.Error as e:
        print(f"Veritabanı hatası: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

