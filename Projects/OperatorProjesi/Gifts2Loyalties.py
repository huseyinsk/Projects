## Sadakat Programı: bu program her 3 ayda bir sadakat puanı verir bu puanlarla istenilen hediye seçilebilir.

MC = 0 # Monthly Counter
DC = 0 # Daily Counter
LP = 0 # Loyalty Points

def gifts2Loyalties():
    print("1. Hediye = 1 Aylık 2GB internet" + "\n" + "2. Hediye = 1 Aylık 100 Dakika" + "\n" + "3. Hediye = 1 Aylık 100 SMS")
    gift = input("Lütfen yukarıdaki hediyelerden birini, numarasını yazarak seçiniz: ").lower()
    while gift not in ["1", "2", "3"]:
        print("Lütfen geçerli bir hediye seçiniz.")
        gift = input("Lütfen yukarıdaki hediyelerden birini, numarasını yazarak seçiniz: ").lower()
    
    print("Hediye başarıyla seçildi, hesabınıza en kısa sürede tanımlanacaktır!")

def lpCounter():
    global MC, DC, LP
    while DC <= 30:
        DC += 1  # 30 gün boyunca her gün 1 artar time.sleep ile orjinal sayaç halinde çalışabilir şu an test amaçlı 3 ay dolmuş gibi çalışıyor
        # time.sleep(24*60*60)  # 24 saat bekletir 
        if DC == 30:
            MC += 1
            DC = 0
            if MC <= 3:
                LP += 1
                print("Sadakat Puanı kazanıldı!")
            elif LP == 3:
                print("3 aylık süreciniz dolmuş bu sebeple bir hediye seçmeye hak kazandınız!")
                gifts2Loyalties()
                break
            else:
                continue


