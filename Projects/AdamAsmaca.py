### Adam asmaca oyunu tasarlanmış python makinesi

print("Adam asmaca oyununa hoş geldiniz.")
print("Kurallar şöyledir: \n1-) Kelimenin sayısı kadar canınız bulunmaktadır\n2-) Canlarınız biterse oyunu kaybedersiniz")
print("3-) Kelimenin içinde olan bir harfi doğru tahmin ederseniz can kaybetmezsiniz\n4-) Tüm harfleri bulursanız oyunu kazanırsınız.")
print("Hadi başlayalım, başarılar !")

# yöneticinin belirleyeceği kelime ve kelimenin harflerini sırasıyla listeleyen kod blokları
harfler = []
yanlisSayac = 0  ## yanlış harf tahmini sayacı
dogruSayac = 0  ## doğru harf sayacı
kelime = str(input("Seçmek istediğiniz kelime: ")).lower()
for i in range(len(kelime)):
    harfler.append(kelime[i])

###### Yöneticinin seçtiği kelimeyi tahmin edecek oyuncuların kod blokları ######
print("Seçilen kelime ", len(kelime) , " Harflidir. ", len(kelime)," adet canınız bulunmaktadır, Başarılar dileriz !")

while yanlisSayac <= len(kelime):  ## Canın bitmediği sürece çalışan while döngüsü
    harfTahmini = str(input("Seçmek istediğiniz harf tahmini: ")).lower()  # Oyuncuların seçeceği harfi soran kod bloku
    if len(harfTahmini) != 1  or not harfTahmini.isalpha():  # Verilen inputa cevap harf mi veya 1 den fazla karakter içeriyor mu kontrol eden blok
        print("Lütfen bir karakterli harf giriniz.")
        continue

    elif yanlisSayac == len(kelime):  ## Canı biterse oyunu bitirecek olan kod bloku
        print("Kelimenin harf sayısı kadar olan bütün canlarınızı tükettiniz.\nOyun bitmiştir.")
        break

    elif harfTahmini in harfler: ## Her bir doğru harf için çalışan kod bloku
        print(f"seçmiş olduğunuz {harfTahmini} harfi kelimede bulunmaktadır.")
        for k in range(len(kelime)):  ## bilinen harfin hangi indexte olacagını veren for kodu
            if harfTahmini == kelime[k]:  ## indexi belirleyen if bloku
                print(f"Seçmiş olduğunuz harf kelimenin {k}. sırasıdır")
                dogruSayac += 1 ## harfleri doğru bilme sonucu oyunu bitirecek olan dogru harf sayacı
        if dogruSayac == len(kelime):  ## eğer bütün harfler bilinirse oyunu bitiren if bloku
            print("Tebrik ederiz. Tüm harfleri sırasıyla buldunuz !")
            break ## oyunu bitiren break komutu
    else:  ## Her bir yanlış harf tahmininde canı eksilten kod bloku
        print(f"seçmiş olduğunuz {harfTahmini} harfi kelimede bulunmamaktadır. Bir can kaybettiniz.")
        yanlisSayac += 1

print("Oyunumuzu oynadığınız için teşekkür ederiz.")  ## Oyun sonu outro
