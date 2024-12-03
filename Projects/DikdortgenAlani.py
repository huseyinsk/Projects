# Dikdörtgen Alanını hesaplayan makine

sayi_1 = float(input("Dikdörtgenin ilk kenarını giriniz: "))
sayi_2 = float(input("Dikdörtgenin ikinci kenarını giriniz: "))

if sayi_1 > sayi_2:
    kisaKenar = sayi_2
    uzunKenar = sayi_1
else:
    kisaKenar = sayi_1
    uzunKenar = sayi_2

def alanHesapla(kisaKenar, uzunKenar):
    alan = (kisaKenar) * (uzunKenar)
    return alan

print(f"Girmiş olduğunuz {kisaKenar} uzunluğa sahip kısa kenarlı ve \n{uzunKenar} uzunluğa sahip uzun kenarlı dikdörtgen alanı: ", alanHesapla(kisaKenar, uzunKenar))