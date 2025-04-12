## Ek paketleri içeren dosya

def extraPackages():
    print("Ek Paketler: \n1. Ek Paket 1: 2 GB internet (20TL) \n2. Ek Paket 2: 100 Dakika(15TL) \n3. Ek Paket 3: 100 SMS(15TL)")
    exPack = input("Lütfen yukarıdaki ek paketlerden birini, numarasını yazarak seçiniz: ").lower()
    while exPack not in ["1", "2", "3"]:
        print("Lütfen geçerli bir ek paket seçiniz.")
        exPack = input("Lütfen yukarıdaki ek paketlerden birini, numarasını yazarak seçiniz: ").lower()

    print(f"{exPack} numaralı ek paket başarıyla seçildi, hesabınıza en kısa sürede tanımlanacaktır!")


def extraFullPackages():
    print("Ek tam paketler güncel fiyatlarının iki katına satılmaktadır.\nPaket içeriği ve fiyatı aşağıdaki gibidir:")
    print("1. Iron Paket(40TL)\n2. Bronze Paket(60TL)\n3. Silver Paket(80TL)\n4. Gold Paket(100TL)\n5. Platinum Paket(120TL)\n6. Diamond Paket(140TL)\n7. VIP Paket(160TL)")
    exFullPack = input("Lütfen yukarıdaki ek tam paketlerden birini, numarasını yazarak seçiniz: ").lower()
    while exFullPack not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Lütfen geçerli bir ek tam paket seçiniz.")
        exFullPack = input("Lütfen yukarıdaki ek tam paketlerden birini, numarasını yazarak seçiniz: ").lower()
    print(f"{exFullPack} numaralı ek tam paket başarıyla seçildi, hesabınıza en kısa sürede tanımlanacaktır!")

