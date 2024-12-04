## BANKACILIK PROJESİ // ATM ve Mobil bankacılık olarak sanal makine
import Giris as giris
import Atm as atm

sorgu = input("Hoş geldiniz.Yapmak istediğiniz işlemi 'mobilbankacilik' veya 'atm' şeklinde giriniz: ").lower()
while sorgu not in ["atm", "mobilbankacilik"]:
    print("Yapılmak isteneni yanlış girdiniz !")
    sorgu = input("Lütfen yapmak istediğiniz işlemi 'mobilbankacilik' veya 'atm' şeklinde giriniz: ").lower()

if sorgu == "mobilbankacilik":
    giris.giris()
else:
    atm.atm()
