# Analiz sistemi veritabanı üzerinden kullanıcıların kullanım verilerine göre
# uygun paket önerir.
import time, sqlite3, re

def analysis(tc):
    print("Analiz sistemine hoş geldiniz..")    
    time.sleep(1)
    conn = sqlite3.connect('overall_dataSet.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM monthly_usage WHERE tc = ?", (tc,))
    usage_data = cursor.fetchall()
    
    if not usage_data:
        print(f"{tc} TC numarasına ait kullanım verisi bulunamadı.")
        conn.close()
        return
        
    latest_usage = usage_data[-1]
    Call = latest_usage[4]  
    Internet = latest_usage[2]  
    Sms = latest_usage[3]  
    SocialMedia = latest_usage[5] 
        
    print("\nEn son ay kullanım verileriniz şu şekildedir:")
    time.sleep(1)
    print("Dakika: ", Call)
    time.sleep(0.1)
    print("İnternet: ", Internet, " GB")
    time.sleep(0.1)
    print("SMS: ", Sms)
    time.sleep(0.1)
    if SocialMedia > 0:
        print("Sosyal Medya: ", SocialMedia, " GB")
        
    conn.close()
        

def suggestion(tc):
    print("Paket önerisi sistemimize hoş geldiniz.")
    time.sleep(1) 
    conn = sqlite3.connect('overall_dataSet.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM monthly_usage WHERE tc = ?", (tc,))
    usage_data = cursor.fetchall()
    
    if not usage_data:
        print(f"{tc} TC numarasına ait kullanım verisi bulunamadı.")
        conn.close()
        return
    
    latest_usage = usage_data[-1]
    dakika_kullanimi = latest_usage[4] 
    internet_kullanimi = latest_usage[2] 
    sms_kullanimi = latest_usage[3]  
    sosyal_medya_kullanimi = latest_usage[5]  

    onerilen_paket = ""
    
    if dakika_kullanimi <= 250 and internet_kullanimi <= 3 and sms_kullanimi <= 75:
        onerilen_paket = "iron"
    elif (dakika_kullanimi <= 350 and dakika_kullanimi > 250) and (internet_kullanimi <= 5 and internet_kullanimi > 3) and (sms_kullanimi <= 100 and sms_kullanimi > 75):
        onerilen_paket = "bronze"
    elif (dakika_kullanimi <= 500 and dakika_kullanimi > 350) and (internet_kullanimi <= 8 and internet_kullanimi > 5) and (sms_kullanimi <= 120 and sms_kullanimi > 100):
        onerilen_paket = "silver"
    elif (dakika_kullanimi <= 650 and dakika_kullanimi > 500) and (internet_kullanimi <= 10 and internet_kullanimi > 8) and (sms_kullanimi <= 150 and sms_kullanimi > 120) and (sosyal_medya_kullanimi <= 3):
        onerilen_paket = "gold"
    elif (dakika_kullanimi <= 850 and dakika_kullanimi > 650) and (internet_kullanimi <= 15 and internet_kullanimi > 10) and (sms_kullanimi <= 175 and sms_kullanimi > 150) and (sosyal_medya_kullanimi <= 5 and sosyal_medya_kullanimi > 3):
        onerilen_paket = "platinum"
    elif (dakika_kullanimi <= 1000 and dakika_kullanimi > 850) and (internet_kullanimi <= 20 and internet_kullanimi > 15) and (sms_kullanimi <= 200 and sms_kullanimi > 175) and (sosyal_medya_kullanimi <= 10 and sosyal_medya_kullanimi > 5):
        onerilen_paket = "diamond"
    else:
        onerilen_paket = "vip"
    

    cursor.execute("SELECT * FROM packages WHERE paket_adi = ?", (onerilen_paket,))
    paket_bilgisi = cursor.fetchone()
    
    if paket_bilgisi:
        paket_adi = paket_bilgisi[1]
        internet_gb = paket_bilgisi[2]
        dakika = paket_bilgisi[3]
        sms = paket_bilgisi[4]
        sosyal_medya_gb = paket_bilgisi[5]
        fiyat = paket_bilgisi[6]
        
        print(f"Kullanmanız gereken paketiniz: {paket_adi.capitalize()} Paketi")
        time.sleep(1)
        print(f"{paket_adi.upper()} PAKET DETAYLARI")
        time.sleep(0.1)
        print(f"İnternet: {internet_gb} GB")
        time.sleep(0.1)
        print(f"Dakika: {dakika}")
        time.sleep(0.1)
        print(f"SMS: {sms}")
        time.sleep(0.1)
        if sosyal_medya_gb > 0:
            print(f"Sosyal Medya: {sosyal_medya_gb} GB")
            time.sleep(0.1)
        print(f"Fiyat: {fiyat} TL")
    else:
        print("Paket bilgisi bulunamadı.")    
    conn.close()

