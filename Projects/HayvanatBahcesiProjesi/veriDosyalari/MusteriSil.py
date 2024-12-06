from veriDosyalari.hesapDB import musteri_tcno as sozluk

def musteriSil():
    tc = int(input("Silmek istediğiniz müşteri kaydına ait tc kimlik no'yu giriniz: "))
    if tc in sozluk.keys():
        del sozluk[tc]
        print("Kayıt başarıyla silindi")
    else:
        print(f"Girmiş olduğunuz {tc} TC Kimlik numarası sistemde kayıtlı değildir.")