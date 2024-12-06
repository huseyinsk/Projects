## Veri dosyasından öğrenci silen python dosyası
from veriDosyalari.hesaplarDB import ogrenci_tcNO as sozluk

def ogrenciSil():
    tc = int(input("Silmek istediğiniz öğrenci kaydına ait tc kimlik no'yu giriniz: "))
    if tc in sozluk.keys():
        del sozluk[tc]
        print("Kayıt başarıyla silindi")
    else:
        print(f"Girmiş olduğunuz {tc} TC Kimlik numarası sistemde kayıtlı değildir.")
