## BANKACILIK PROJESİ // ATM ve Mobil bankacılık olarak sanal makine
from veriDosyalari import Giris as giris
from veriDosyalari import Atm as atm

sorgu = input("Hoş geldiniz.Yapmak istediğiniz işlemi 'mobilbankacilik' veya 'atm' şeklinde giriniz: ").lower()
while sorgu not in ["atm", "mobilbankacilik"]:
    print("Yapılmak isteneni yanlış girdiniz !")
    sorgu = input("Lütfen yapmak istediğiniz işlemi 'mobilbankacilik' veya 'atm' şeklinde giriniz: ").lower()

if sorgu == "mobilbankacilik":
    giris.giris()
else:
    atm.atm()
