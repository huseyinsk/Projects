# Yetkili silme kodunu içeren python dosyası
from veriDosyalari.hesaplarDB import yetkili_tcNO as sozluk

def yetkiliSil():
    tc = int(input("Silmek istediğiniz yetkili kaydına ait tc kimlik no'yu giriniz: "))
    if tc in sozluk.keys():
        del sozluk[tc]
    else:
        print(f"Girmiş olduğunuz {tc} TC Kimlik numarası sistemde kayıtlı değildir.")