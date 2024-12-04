# Mobil bankacılık arama ekranı işlevi gören uygulama
from veriDosyalari.KrediCekme import krediCekme
from veriDosyalari.ParaTransfer import paraTransfer
from veriDosyalari.DovizAl import dovizAl
from veriDosyalari.MusteriDB import musteri_HesapNO


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
