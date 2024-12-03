### Sezar şifreleme işlevi gören python uygulaması
import time

alfabeTR = ["A","B","C","Ç","D","E","F","G","Ğ","H","I","İ","J","K","L","M","N","O","Ö","P","R","S","Ş","T","U","Ü","V","Y","Z"]
alfabeEN = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

print("Uygulamamıza hoş geldiniz.\nSezar Şifreleme Metotu şu şekilde çalışır: \n1-) Gireceğiniz 'Mod' değeri alfabenin değeri olmalıdır")
print("2-) Şifrelenecek olan çıktı girmiş olduğunuz kelimedeki her harfin sırasıyla 3 harf sonraki alınarak şifrelenir.")
print("Uygulamamızda türkçe(mod 29) ve ingilizce(mod 27) bulunmaktadır dolayısıyla şifrelemeyi bu iki mod'a göre yapabilirsiniz.")
print("Hadi başlayalım.")
time.sleep(1.5)

sifrelenecek_Kelime = input("Lütfen şifrelemek istediğiniz kelimeyi giriniz: ").upper()
alfabeSorgu = input("Lütfen şifrelemekte kullanmak istediğiniz alfabeyi(modu) 'türkçe' veya 'ingilizce' olacak şekilde giriniz: ").lower()

while (alfabeSorgu != "türkçe") and (alfabeSorgu != "ingilizce"):
    print("Yanlış alfabe tuşladınız, Lütfen 'türkçe' veya 'ingilizce' olarak giriniz.")
    alfabeSorgu = input("Lütfen şifrelemekte kullanmak istediğiniz alfabeyi 'türkçe' veya 'ingilizce' olacak şekilde giriniz: ").lower()

if (alfabeSorgu == "türkçe"):
    sifrelenmisKelime = ""
    for i in range(len(sifrelenecek_Kelime)):
        kelimedekiHarf = sifrelenecek_Kelime[i]
        sifrelenecekHarf_Indexi = alfabeTR.index(kelimedekiHarf) + 3
        sifrelenecekHarf = alfabeTR[sifrelenecekHarf_Indexi]
        sifrelenmisKelime += sifrelenecekHarf
    print(sifrelenmisKelime)

else:
    sifrelenmisKelime = ""
    for i in range(len(sifrelenecek_Kelime)):
        kelimedekiHarf = sifrelenecek_Kelime[i]
        sifrelenecekHarf_Indexi = alfabeEN.index(kelimedekiHarf) + 3
        sifrelenecekHarf = alfabeEN[sifrelenecekHarf_Indexi]
        sifrelenmisKelime += sifrelenecekHarf
    print(sifrelenmisKelime)