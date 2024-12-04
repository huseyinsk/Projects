# Mobil bankacılık arama ekranı işlevi gören uygulama
from KrediCekme import krediCekme
from ParaTransfer import paraTransfer
from DovizAl import dovizAl
from MusteriDB import musteri_HesapNO


def yapilmakIstenen():
    print("Uygulamamıza hoş geldiniz.")
    print("Yapılabilecek şeyler: 'kredicek','paragonder','dovizal','bakiyesorgu'")
    istenenSorgu = input("Lütfen yapmak istediğiniz şeyi arama butonuna yazınız: ").lower()

    while (istenenSorgu != "kredicek") and (istenenSorgu!="bakiyesorgu") and (istenenSorgu != "paragonder") and (istenenSorgu != "dovizal"):
        print("Yanlış seçenek girdiniz. Lütfen tekrar deneyiniz."
              +"\nYapılabilecek şeyler: 'kredicek','paragonder','dovizal','bakiyesorgu'")
        istenenSorgu = input("Lütfen yapmak istediğiniz şeyi arama butonuna yazınız: ").lower()

    if istenenSorgu == "kredicek":
        krediCekme()
    elif istenenSorgu == "paragonder":
        paraTransfer()
    elif istenenSorgu == "bakiyesorgu":
        hesapNO = int(input("Lütfen hesap numaranızı giriniz: "))
        print("Güncel bakiyeniz: ", musteri_HesapNO[hesapNO]["BAKiYE"])
    else:
        dovizAl()
