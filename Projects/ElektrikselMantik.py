# Mantıksal verilere göre elektrik devresi çizen python programı 
import turtle,time
x = turtle.Turtle()

def pKontrol(p):
    if p == False:
        x.forward(30)
        x.dot(5,"black")
        x.left(45)
        x.forward(30)
        x.dot(5,"black")
        x.penup()
        x.forward(-30)
        x.right(45)
        x.forward(30)
        x.pendown()
        x.dot(5,"black")
        x.forward(30)
    else:
        x.forward(30)
        x.dot(5,"black")
        x.forward(30)
        x.dot(5,"black")
        x.forward(30)

def qKontrol(q):
    if q == False:
        x.forward(30)
        x.dot(5,"black")
        x.left(45)
        x.forward(30)
        x.dot(5,"black")
        x.penup()
        x.forward(-30)
        x.right(45)
        x.forward(30)
        x.pendown()
        x.dot(5,"black")
        x.forward(30)
    else:
        x.forward(30)
        x.dot(5,"black")
        x.forward(30)
        x.dot(5,"black")
        x.forward(30)

def veBaglaci(p,q):
    if p == False and q == True:
        pKontrol(False)
        qKontrol(True)
        time.sleep(3) ## Son şeklin vsc üstünde net görülmesi için eklendi
    elif p == False and q == False:
        pKontrol(False)
        qKontrol(False)
        time.sleep(3) ## Son şeklin vsc üstünde net görülmesi için eklendi
    elif p == True and q == False:
        pKontrol(True)
        qKontrol(False)
        time.sleep(3) ## Son şeklin vsc üstünde net görülmesi için eklendi
    else:
        pKontrol(True)
        qKontrol(True)
        time.sleep(1.5) ## Son şeklin vsc üstünde net görülmesi için eklendi

def veyaBaglaci(p,q):
    x.forward(30)
    x.left(90)
    x.forward(30)
    x.right(90)
    pKontrol(p)
    x.right(90)
    x.forward(30)
    x.penup()
    x.forward(-30)
    x.left(90)
    x.forward(-90)
    x.left(90)
    x.forward(-30)
    x.pendown()
    x.right(180)
    x.forward(30)
    x.left(90)
    qKontrol(q)
    x.left(90)
    x.forward(30)
    x.right(90)
    x.forward(30)
    time.sleep(1.5) ## Son şeklin vsc üstünde net görülmesi için eklendi

p = int(input("p değerini '1' veya '0' olarak değer giriniz: "))
q = int(input("q değerini '1' veya '0' olarak değer giriniz: "))
while q not in [0,1]:
    print("Yanlış değer girdiniz !")
    q = int(input("Lütfen q değerini '1' veya '0' olarak değer giriniz: "))
while p not in [0,1]:
    print("Yanlış değer girdiniz !")
    p = int(input("Lütfen p değerini '1' veya '0' olarak değer giriniz: "))

baglacTuru = input("Uygulamak istediğiniz baglacı 've', 'veya' olarak giriniz: ").lower()
while baglacTuru not in ["ve","veya"]:
    print("Yanlış bağlaç türü girdiniz !")
    baglacTuru = input("Uygulamak istediğiniz baglacı 've', 'veya' olarak giriniz: ").lower()

if baglacTuru == "ve":
    veBaglaci(p,q)
else:
    veyaBaglaci(p,q)

x.reset()

veyaBaglaci(1,0) ## Art arda girilerek istenilen şekiller çizdirilebilir.
veBaglaci(0,0)
time.sleep(3)