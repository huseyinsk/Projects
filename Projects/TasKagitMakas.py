## Taş kağıt makas oyunu tasarlanmış python makinesi

print("Taş kağıt makas oyunumuza hoş geldiniz. ")
print("Bu oyun iki kişilik oynanır. Yani partneriniz yoksa bu oyunu oynayamazsınız. ")
print("Seçilebilecek objeler: Taş - Kağıt - Makas")
print("Oyun kuralları: \n1-) Taş makası kırar \n2-) Makas kağıtı keser \n3-) Kağıt taşı yutar")
print("Hadi başlayalım, başarılar !")

kisi_1 = str(input("Birinci oyuncunun seçtiği obje: ")).lower()
kisi_2 = str(input("İkinci oyuncunun seçtiği obje: ")).lower()

while (kisi_1 != "taş") and (kisi_1 != "kağıt") and (kisi_1 != "makas"): 
    print("Birinci oyuncu belirlenen objeler harici bir şey seçti.")
    kisi_1 = str(input("Lütfen belirlenen objeler arasından birini seçiniz: ")).lower()

while (kisi_2 != "taş") and (kisi_2 != "kağıt") and (kisi_2 != "makas"): 
    print("İkinci oyuncu belirlenen objeler harici bir şey seçti.")
    kisi_2 = str(input("Lütfen belirlenen objeler arasından birini seçiniz: ")).lower()

if (kisi_1 == "taş" and kisi_2 == "makas") or (kisi_1 == "kağıt" and kisi_2 == "taş") or (kisi_1 == "makas" and kisi_2 =="kağıt"):
    print("Birinci oyuncu kazandı. Tebrik ederiz !")
elif(kisi_1 == kisi_2):
    print("İki oyuncu da aynı objeyi seçti.Her iki tarafı da tebrik ederiz! 'BERABERE'")
else:
    print("İkinci oyuncu kazandı. Tebrik ederiz !")

print("Oyunumuzu oynadığınız için teşekkür ederiz.")