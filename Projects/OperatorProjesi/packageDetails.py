import sqlite3,time

def packageDetails(tc):
    conn = sqlite3.connect("overall_dataSet.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_packages WHERE tc=?", (tc,))
    user_package = cursor.fetchone()
        
    if not user_package:
        print(f"TC: {tc} numaralı kullanıcıya ait paket bilgisi bulunamadı!")
        conn.close()
        return
    cursor.execute("PRAGMA table_info(user_packages)")
    columns = cursor.fetchall()
    internet_index = dakika_index = sms_index = sosyalmedya_index = bakiye_index = paket_id_index = None
        
    for i, col in enumerate(columns):
        col_name = col[1].lower()
        if col_name in ['internet', 'internet_gb']:
            internet_index = i
        elif col_name in ['dakika', 'konusma_dk', 'konusma']:
            dakika_index = i
        elif col_name in ['sms', 'mesaj', 'mesajlar']:
            sms_index = i
        elif col_name in ['sosyalmedya', 'sosyal_medya', 'sosyal']:
            sosyalmedya_index = i
        elif col_name in ['bakiye', 'balance']:
            bakiye_index = i
        elif col_name in ['paket_id', 'paketid']:
            paket_id_index = i
        
    paket_id = user_package[paket_id_index] if paket_id_index is not None else None
    paket_adi = "Bilinmiyor"
        
    if paket_id:
        cursor.execute("SELECT * FROM packages WHERE paket_id=?", (paket_id,))
        paket_bilgisi = cursor.fetchone()
                
        if paket_bilgisi:
            cursor.execute("PRAGMA table_info(packages)")
            package_columns = cursor.fetchall()
            paket_adi_index = None

            for i, col in enumerate(package_columns):
                if col[1].lower() in ['paket_adi', 'adi', 'name', 'paket']:
                    paket_adi_index = i
                    break

            if paket_adi_index is not None and paket_bilgisi[paket_adi_index]:
                paket_adi = paket_bilgisi[paket_adi_index]

    print("Paket detaylarınız şu şekildedir:")
    time.sleep(1)
    print(f"TC Kimlik No: {tc}")
    time.sleep(0.1)
    print(f"Paket Türü: {paket_adi}")
    time.sleep(0.1)
    if bakiye_index is not None:
        print(f"Bakiye: {user_package[bakiye_index]} TL")
        time.sleep(0.1)

    if internet_index is not None:
        print(f"İnternet: {user_package[internet_index]} GB")
        time.sleep(0.1)
        
    if dakika_index is not None:
        print(f"Dakika: {user_package[dakika_index]} DK")
        time.sleep(0.1)
        
    if sms_index is not None:
        print(f"SMS: {user_package[sms_index]} Adet")
        time.sleep(0.1)
        
    if sosyalmedya_index is not None:
        print(f"Sosyal Medya: {user_package[sosyalmedya_index]} GB")
        time.sleep(0.1)
        
    if 'conn' in locals():
        conn.close()
