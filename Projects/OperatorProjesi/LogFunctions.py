import sqlite3
ad, soyad, tc, numara = "", "", "", ""

def Login():
    global ad, soyad, tc
    deneme_hakki=3
    while True:
        if deneme_hakki <= 0:
            print("Hesabınız 15 dakika kilitlenmiştir. Lütfen daha sonra tekrar deneyiniz.")
            break
        
        ad_input = input("Adınızı giriniz: ").strip() 
        soyad_input = input("Soyadınızı giriniz: ").strip() 
        tc = input("TC Kimlik Numaranızı giriniz: ").strip()  
        
        conn = sqlite3.connect("overall_dataSet.db", timeout=30)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE tc=?", (tc,))
        user = cursor.fetchone()
        
        if user and user[1] and user[2]:
            db_isim = user[1].strip().lower() 
            db_soyisim = user[2].strip().lower()
            input_isim = ad_input.lower()
            input_soyisim = soyad_input.lower()  
            
            if db_isim == input_isim and db_soyisim == input_soyisim:
                print(f"Giriş başarılı! Hoş geldiniz {user[1]} {user[2]}!")
                ad = user[1] 
                soyad = user[2]  
                conn.close()
                break
            else:
                print("Hatalı isim veya soyisim!")
        else:
            print("Hatalı TC kimlik numarası!")
        
        conn.close()
        secim = input("Çıkış yapmak için 'q', tekrar denemek için herhangi bir tuşa basınız: ").lower()
        
        if secim == 'q':
            print("Program sonlandırılıyor...")
            return False
        else:
            deneme_hakki -= 1
            print(f"Kalan deneme hakkı: {deneme_hakki}")
            continue

def register(ad, soyad, tc, numara):
    conn = sqlite3.connect("overall_dataSet.db", timeout=30)    
    while True:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE tc=?", (tc,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            print(f"Bu TC kimlik numarası ({tc}) ile kayıtlı bir kullanıcı zaten var!")
            tc = input("Lütfen başka bir TC Kimlik numarası giriniz: ")
            continue
        else:
            cursor.execute("INSERT INTO users (tc, isim, soyisim, numara) VALUES (?, ?, ?, ?)",
                        (tc, ad, soyad, numara))
            conn.commit()
            conn.close()
            
            print(f"{ad} {soyad} kullanıcısı başarıyla kaydedildi!")
            print("Giriş yapabilirsiniz.")
            break
    
def logout():
    print("Başarıyla çıkış yapılıyor...")

def check_phone_exists(numara):
    while True:
        conn = sqlite3.connect("overall_dataSet.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE numara=?", (numara,))
        result = cursor.fetchone()
        conn.close()
        if result:
            print(f"Bu numara ({numara}) veritabanında zaten bulunmaktadır!")
            numara = input("Lütfen başka bir telefon numarası giriniz: ")
            while len(numara) != 11 or numara[0] != "0" or numara[1] != "5" or numara[2] != "3" or numara[3] != "6":
                print("Hatalı bir telefon numarası girdiniz! ")
                numara = input("Lütfen sahip olmak istediğiniz 11 haneli bir telefon numarası giriniz.(0536XXXXXXX şeklinde olmalıdır)")
            continue
        else:
            break
