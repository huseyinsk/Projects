### Kimlik&Pasaport kaydı alan sanal makine

import re, random as r

def kimlik():
    ad = input("adınızı giriniz: ").upper()
    soyad = input("soyadınızı giriniz: ").upper()
    
    tc = input("oluşturmak istediğiniz 11 haneli tc kimlik numarasını giriniz: ")
    while (len(tc) != 11):
        print("Hatalı tuşlama yaptınız lütfen 11 haneli ve sadece rakamdan oluşan tc kimlik numarası giriniz.")
        tc = input("lütfen oluşturmak istediğiniz 11 haneli tc kimlik numarasını giriniz: ")

    anne_adi = input("anne adınızı giriniz: ").upper()
    baba_adi = input("baba adınızı giriniz: ").upper()

    dogumTarihi_gun = int(input("Doğum tarihinizin günü(rakam olarak giriniz): "))
    while (dogumTarihi_gun > 30 or dogumTarihi_gun < 1):
        dogumTarihi_gun = int(input("Doğum tarihininin gününü yanlış girdiniz. Lütfen 1 ile 30 arasında değer olarak giriniz: "))
    
    dogumTarihi_ay = int(input("Doğum tarihinizin ayı(rakam olarak giriniz): "))
    while (dogumTarihi_ay > 12 or dogumTarihi_ay < 1):
        dogumTarihi_ay = int(input("Doğum tarihininin ayını yanlış girdiniz. Lütfen 1 ile 12 arasında değer olarak giriniz: "))

    dogumTarihi_yil = int(input("Doğum tarihinizin yılı: "))
    kimlikNumarasi = r.randint(100000,999999)
    print(f"oluşturulan kimlikteki adınız: {ad}, soyadınız: {soyad}, tcniz: {tc}, anne adi: {anne_adi}, baba adi: {baba_adi}"+
          f"\ndogum tarihi:{dogumTarihi_gun}/{dogumTarihi_ay}/{dogumTarihi_yil} ve kimlik numarası: {kimlikNumarasi}")
    print("iyi günler dileriz.")

def pasaport():
    ad = input("adınızı giriniz: ").upper()
    soyad = input("soyadınızı giriniz: ").upper()
    
    tc = input("tc kimlik numarasını giriniz: ")
    while (len(tc) != 11):
        print("Hatalı tc kimlik numarası girdiniz")
        tc = input("lütfen 11 haneli ve sadece rakamdan oluşan tc kimlik numarası giriniz: ")

    unvan = input("ünvanınızı 'doktor','teknisyen',hemşire' olacak şekilde giriniz: ").lower()
    while unvan not in ["doktor","teknisyen","hemşire"]:
        print("Hatalı ünvan girişi yaptınız.")
        unvan = input("Lütfen ünvanınızı 'doktor','teknisyen',hemşire' olacak şekilde giriniz: ").lower()

    kurumSicil_NO = input("Kurum sicil numaranızı giriniz: ")
    
    telefon = input("telefon numaranızı başında sıfır olmadan giriniz: ")
    while (len(telefon) != 10):
        print("Hatalı telefon numarası girdiniz.")
        telefon = input("Lütfen telefon numaranızı başında sıfır olmadan 10 haneli olacak şekilde giriniz: ")

    e_posta = input("E-posta adresinizi giriniz: ")
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(pattern, e_posta):
        pass
    else:
        while not re.match(pattern, e_posta):
            print("Hatali e-mail formatı girdiniz ")
            e_posta = input("E-posta adresinizi düzgün formatta giriniz: ")

    print("Pasaportunuz başarıyla oluşturuldu." + 
          f"\nAdınız: {ad}, Soyadınız: {soyad}, Ünvanınız: {unvan}, kurum sicil no: {kurumSicil_NO}"+
          f"telefon numaranız: {telefon}, e-posta adresiniz: {e_posta}")
    print("İyi günler dileriz.")
            
print("Başvuru tipleri: 'pasaport', 'kimlik'")
basvuruTipi = input("başvuru tipini seçiniz: ").lower()
while basvuruTipi not in ["pasaport","kimlik"]:
    basvuruTipi = input("Yanlış başvuru tipi girdiniz lütfen 'pasaport', 'kimlik' şeklinde giriniz.").lower()

if (basvuruTipi == "kimlik"):
    kimlik()
else:
    pasaport()

 
