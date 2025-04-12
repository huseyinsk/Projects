# sms = adet / internet & sosyalMedya = gb / dakika = dk / fiyat = TL olarak tasarlanmıştır
dakika,internet,sms,sosyalMedya,fiyat = 0,0,0,0,0

def packageDetails(dakika,internet,sms,sosyalMedya,fiyat):
    print("Paketinizin içeriği:"
          ,"\nDakika: ", dakika
          ,"\nİnternet: ", internet , " GB"
          ,"\nSMS: ", sms
          ,"\nSosyal Medya: ", sosyalMedya , " GB"
          ,"\nFiyat: ", fiyat , " TL")
    
def iron():
    global dakika,internet,sms,sosyalMedya,fiyat
    dakika = 250
    internet = 3
    sms = 75  
    sosyalMedya = 0
    fiyat = 20

def bronze():
    global dakika,internet,sms,sosyalMedya,fiyat
    dakika = 350
    internet = 5
    sms = 100
    sosyalMedya = 0 
    fiyat = 30

def silver():
    global dakika,internet,sms,sosyalMedya,fiyat
    dakika = 500
    internet = 8 
    sms = 120
    sosyalMedya = 0 
    fiyat = 40

def gold():
    global dakika,internet,sms,sosyalMedya,fiyat
    dakika = 650
    internet = 10 
    sms = 150
    sosyalMedya = 3
    fiyat = 50

def platinum():
    global dakika,internet,sms,sosyalMedya,fiyat
    dakika = 850
    internet = 15
    sms = 175
    sosyalMedya = 5
    fiyat = 60

def diamond():
    global dakika,internet,sms,sosyalMedya,fiyat
    dakika = 1000
    internet = 20
    sms = 200
    sosyalMedya = 10
    fiyat = 70

def vip():
    global dakika,internet,sms,sosyalMedya,fiyat
    dakika = 1500
    internet = 30
    sms = 500
    sosyalMedya = 20
    fiyat = 80 

