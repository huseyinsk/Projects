## Rus ruleti işlevini gören python uygulaması
import random
from time import sleep

mermiSayisi = int(input("Silahınıza eklemek istediğiniz mermi sayısını giriniz: "))
kisiSayisi = int(input("Sırasıyla oynayacak kişi sayısını giriniz: "))
silahJarjor = ["","","","","",""]

while mermiSayisi > 6:
    print("6'dan büyük değer girdiniz !"
          +"\nTabanca maksimum 6 mermi alabiliyor, Lütfen tekrar deneyiniz !")
    mermiSayisi = int(input("Silahınıza eklemek istediğiniz mermi sayısını giriniz: "))

while mermiSayisi < 0:
    print("Negatif bir değer girdiniz, Lütfen tekrar deneyiniz !")
    mermiSayisi = int(input("Silahınıza eklemek istediğiniz mermi sayısını giriniz: "))

while kisiSayisi > 6:
    print("6'dan büyük değer girdiniz !"
          +"\nTabanca maksimum 6 mermi alabiliyor bu sebeple maksimum 6 kişi oynayabilir, Lütfen tekrar deneyiniz !")
    kisiSayisi = int(input("Sırasıyla oynayacak kişi sayısını giriniz: "))

while kisiSayisi < 0:
    print("Negatif bir değer girdiniz, Lütfen tekrar deneyiniz !")
    kisiSayisi = int(input("Sırasıyla oynayacak kişi sayısını giriniz: "))

def oyun():
    for i in range(mermiSayisi):   ## Silaha istenilen kadar mermi ekleyecek for döngüsü
        while True:
            mermiYeri = random.randint(0,5)
            if silahJarjor[mermiYeri] == "":
                silahJarjor[mermiYeri] = "mermi"
                break

    for i in range(6):
        if silahJarjor[i] == "":
            print(f"Oyuncu {i+1}.denemede boş mermiye denk gelerek hayatta kalmıştır.")
        else:
            print(f"Oyuncu {i+1}.denemede dolu mermiye denk gelerek hayatına veda etmiştir.")

    print("Oyunumuz sona ermiştir.")

if kisiSayisi == 1:
    print("Oyun tek kişilik oynanamaz.")
elif kisiSayisi == 2:
    print("Oyun 3 tur olacak şekilde sırasıyla iki kişi olarak döner.Oyuncu bir sırasıyla '1,3,5'. atışları yapar"
          +"\nOyuncu iki ise sırasıyla '2,4,6' atışlarını yapar.")
    sleep(1.5)
    oyun()
    
elif kisiSayisi == 3: 
    print("Oyun 2 tur olacak şekilde üç kişi olarak döner.Oyuncu bir sırasıyla '1,4'. Atışlara sahiptir."
          +"\nOyuncu iki ise sırasıyla '2,5,' atışlarını yapar."
          +"\nOyuncu üç ise sırasıyla '3,6' atışlarını yapar.")
    sleep(1.5)
    oyun()
elif kisiSayisi == 6:
    print("Oyun sırasıyla ateşlenerek her oyuncu ateşlediği sırasındaki mermiyi dener.")
    sleep(1.5)
    oyun()
else:
    print(f"Oyun verilen {kisiSayisi} kişi sayısı ile oynanamaz.")
