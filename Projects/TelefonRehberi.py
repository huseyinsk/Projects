## Telefon rehberi işlevi gören python uygulaması

rehber = {"05362728011":{"HÜSEYİN":"SARIKAYA"} ## Numara : {ad:'soyad}
          ,"05362725512":{"HARUN":"BİNGÖL"}
          ,"05362361011":{"SERPİL":"ASLAN"}}

sorgu = input("Lütfen ne yapmak istediğinizi (kontrol/ekle/sil) olarak giriniz: ").lower()
while sorgu not in ["kontrol","ekle","sil"]:
    print("Yanlış girdi yaptınız !")
    sorgu = input("Lütfen ne yapmak istediğinizi (kontrol/ekle/sil) olarak giriniz: ").lower()

def rehberKontrol(numara):
    if numara in rehber.keys():
        isim = list(rehber["05362728011"].keys())[0]  # sözlükteki isimi listeleyip listenin 0. indexi ile ismi alır
        soyisim = list(rehber["05362728011"].values())[0] # sözlükteki soyismi listeleyip listenin 0. indexi ile soyismi alır
        print(f"Vermiş olduğunuz {numara} numarasına ait bilgiler için Ad: {isim}, Soyad: {soyisim} ")
    else:
        print(f"Vermiş olduğunuz {numara} numarası rehberde kayıtlı değildir ")

def rehberEkleme(eklenecekNumara):
    eklenecekIsim = input("Eklemek istediğiniz ismi giriniz: ").upper()
    eklenecekSoyisim = input("Eklemek istediğiniz soyismi giriniz: ").upper()
    rehber[eklenecekNumara] = {}
    bilgiEkle = rehber[eklenecekNumara]
    bilgiEkle[eklenecekIsim] = eklenecekSoyisim
    print(f"{eklenecekNumara} numaraya sahip {eklenecekIsim} {eklenecekSoyisim} rehbere başarıyla eklendi !")

def kisiSilme(numara):
    if numara in rehber.keys():
        del rehber[numara]
        print(f"{numara} numarası başarıyla rehberden silindi !")
    else:
        print(f"Girmiş olduğunuz {numara} numarası rehberde kayıtlı değildir !")

if sorgu == "ekle":
    eklenecekNumara = input("Lütfen eklemek istediğiniz numarayı giriniz: ")
    rehberEkleme(eklenecekNumara)
elif sorgu == "kontrol":
    numara = input("Lütfen kontrol etmek istediğiniz numarayı giriniz: ")
    rehberKontrol(numara)
else:
    numara = input("Lütfen silmek istediğiniz numarayı giriniz: ")
    kisiSilme(numara)

