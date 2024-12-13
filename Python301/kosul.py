# KARAR & KONTROL YAPILARI

# True - False Sorgulamalari

sinir = 5000

sinir == 4000 # False döner

sinir == 5000 # True

5 == 4 # False
5 == 5 # True

# if -> eger

sinir = 50000
gelir = 60000

gelir < sinir

if gelir < sinir:
    print("Gelir sinirdan kucuk")
    print(gelir**2)

if gelir > sinir:
    print("Gelir sinirdan buyuk")


# else

sinir = 50000
gelir = 35000

if gelir > sinir:
    print("Gelir sinirdan buyuk")

else:
    print("Gelir sinirdan kucuk")

# diger ornek
sinir = 50000
gelir = 50000

if gelir == sinir:
    print("Gelir sinira esittir")

else:
    print("Gelir sinira esit degildir")


# elif

sinir = 50000
gelir1 = 60000
gelir2 = 50000
gelir3 = 35000

if gelir1 > sinir:
    print("Tebrikler, hediye kazandiniz.")   
elif gelir1 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")


if gelir3 > sinir:
    print("Tebrikler, hediye kazandiniz.")   
elif gelir3 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")


if gelir2 > sinir:
    print("Tebrikler, hediye kazandiniz.")   
elif gelir2 < sinir:
    print("Uyari!")
else:
    print("Takibe devam")


# mini uygulama 
sinir = 50000
magaza_adi = input("Magaza Adi Nedir?")
gelir = int(input("Gelirinizi Giriniz:"))

if gelir > sinir:
    print("Tebrikler, "+ magaza_adi + " promosyon kazandiniz!!")
elif gelir < sinir:
    print("Uyari! Cok dusuk gelir:"+ str(gelir))
else:
    print("Takibe devam")
