## İspat Yöntemlerine örnek olarak yazılmış python programı 
import time

def aksineOrnekVererek():
    print("Tüm asal sayılar tek sayıdır'ı ; 2 bir asal sayıdır ve tek değildir ile yanlışlığı ifade edilir")

def denemeYontemi():
    print("İstenileni yerine koyarak(deneme yaparak) ispatlama yöntemidir. ")
    elemanSayisi = int(input("Kümenizin kaç elemanlı olmasını istersiniz ? : "))
    kumeSayaci = 0
    kume = []
    while kumeSayaci < elemanSayisi:
        kumeSayaci += 1
        eleman = int(input(f"Lütfen kümenize eklemek istediğiniz {kumeSayaci}. elemanı giriniz."))
        kume.append(eleman)
    y = int(input("x vermiş olduğunuz kümenin elemanı olmak üzere x^2 <= y olduğunu deneme yöntemi ile ispatlayan y sayısı giriniz: "))
    indexSayaci = 0
    while indexSayaci < elemanSayisi:
        eleman = kume[indexSayaci]
        if eleman**2 >= y:
            print(f"{eleman} sayısının karesi {y} sayısından büyük veya eşit olduğu için deneme yoluyla yanılgı sonucunu ispatladık.")
            break
        elif indexSayaci == elemanSayisi - 1:
            print("Verilen her küme elemanın karesi {y}'den küçük olduğununun doğruluğunu deneme yöntemi ile ispatladık.") 
            break
        else:
            indexSayaci += 1

def olmayanaEngi():
    print("p ise q doğru ise q' ise p' de doğrudur bu önerme olmayana engi ile ispat edilme denir.")
    print("n^2 tek ise n tektir koşulunu olmayana engi ile ispat edelim")
    time.sleep(1)
    n = int(input("Bir n tek sayısı giriniz: "))
    while n % 2 == 0:
        n = int(input("Çift sayı girdiniz, bir n tek sayısı giriniz: "))
    p = n**2
    q = n
    print("p ise q için n^2 tek ise n tektir ifadesi q' ise p' için n tek değilse n^2 tek değil olur.")
    min_qDegil = (n**2) + 1 
    min_pDegil = n + 1
    print("q' != 2n+1 ve p' != 2n+1 için (2n+1)^2 = (2n+1)*(2n+1) = 4(n^2) + 4n + 1 = 2(2(n^2)+2n) + 1 olur."
          +"2(n^2)+2n işlemine a dersek sonuç 2a + 1 yani tek sayı olur.")
    print(f"Vermiş olduğunuz {n} sayısına göre p ise q önermesi: {p} tek ise {q} tektir doğruluğunu sağlar."
          +f"\nq' ise p' önermesi ise: q={min_qDegil} ise p = {min_pDegil} şeklinde {n} sayısına kıyasla minimum değerlerini alır"
          +"\nBu şekilde çözümlenmesine 'Olmayana Engi ile İspat Yöntemi' denir.")

def dogrudanIspat():
    print("p ise q biçiminde şartlı önerme için kullanılır."
          +"\n1.Adım = 1. önerme yani p = 1 olarak kabul edilir"
          +"\n2.Adım = q'nun doğru olduğu gösterilmeye çalışılır."
          +"\n3.Adım = Eğer doğru ise p ise q doğru kabul edilir")
    print("n^2 tek ise n tektir önermesini doğrudan ispat ile ispatlayalım")
    n = int(input("Bir n tek sayısı giriniz: "))
    while n % 2 == 0:
        n = int(input("Çift sayı girdiniz, bir n tek sayısı giriniz: "))
    p = n**2
    q = n
    min_qDegil = (n**2) + 1 
    min_pDegil = n + 1
    print("q' != 2n+1 için (2n+1)^2 = (2n+1)*(2n+1) = 4(n^2) + 4n + 1 = 2(2(n^2)+2n) + 1 olur."
          +"2(n^2)+2n işlemine a dersek sonuç 2a + 1 yani tek sayı olur.")
    print(f"Vermiş olduğunuz {n} sayısına göre p ise q önermesi: {p} tek ise {q} tektir doğruluğunu sağlar."
          +f"\nq' ise p' önermesi ise: q={min_qDegil} ise p = {min_pDegil} şeklinde {n} sayısına kıyasla minimum değerlerini alır"
          +"\nBu şekilde çözümlenmesine 'Olmayana Engi ile İspat Yöntemi' denir.")
    
def tumeVarim():
    print("Gauss Yöntemi = 1+2+3+4+..+n için n.(n+1)/2 dir"
          +"\n1.Adım: n'in en küçük değeri kontrol edilir\n2.Adım: En küçük değer doğruysa n=k doğru kabul edilir."
          +"\n3.Adım: n = k+1 doğru olduğu gösterilmeye çalışılır.")
    n = int(input("Kontrol etmek istediğiniz bir n sayısı giriniz: "))
    while n < 0:
        print("Negatif sayı girdiniz.Lütfen pozitif tam sayı giriniz.")
        n = int(input("Kontrol etmek istediğiniz bir n sayısı giriniz: "))

    print("1+2+..+k+(k+1) (k.(k+1)/2)+(k+1) olur bu da (k+1)'i 2 ile genişleşletip (k+1) parantezine alırsak --> (k+1).(k+2)/2 olur."
          +f"\n girmiş olduğunuz {n} sayısı için {n} = k+1 doğru olur.")


ispatYontemi = input("Kullanmak istediğiniz ispat yöntemini giriniz: ").lower()
while ispatYontemi not in ["aksine","deneme","olmayanaengi","doğrudanispat","tümevarım"]:
    print("Yanlış girdiniz.Lütfen 'aksine','deneme','olmayanaengi','doğrudanispat','tümevarım' şekilde giriniz")
    ispatYontemi = input("Kullanmak istediğiniz ispat yöntemini giriniz: ").lower()

if ispatYontemi == "aksine":
    aksineOrnekVererek()
elif ispatYontemi == "deneme":
    denemeYontemi()
elif ispatYontemi == "olmayanaengi":
    olmayanaEngi()
elif ispatYontemi == "doğrudanispat":
    dogrudanIspat()
else:
    tumeVarim()
