## 2. dereceden bilinmeyenli denklemin kökünü bulan python makinesi

print("Denkleminiz 2. derecen(a(x^2) + bx + c) bir denklem olmalıdır.")

a = int(input("(x^2)'nin başkatsayını giriniz: "))
b = int(input("x'in katsayısını giriniz: "))
c = int(input("sabit sayının değerini giriniz: "))

determinant = (b**2) - (4*a*c)  # determinant denklemi

birinciKok = (-b - (determinant**1/2)) / (2*a)  ## birinci kok denklemi
ikinciKok = (-b + (determinant**1/2)) / (2*a)  ## ikinci kok denklemi

if determinant == 0:
    print("Denklemin iki adet kökü vardır ancak çakışık yani birbirine eşittir.")
    print(f"Kökleriniz:{birinciKok} ve {ikinciKok}'tür.")
elif determinant < 0:
    print("Denkleminizin reel kökü yoktur.")
    print(f"Kökleriniz {birinciKok} ve {ikinciKok}'tür.")
else:
    print("Denklemin 2 adet gerçek kökü vardır. ")
    print(f"Kökleriniz {birinciKok} ve {ikinciKok}'tür.")
