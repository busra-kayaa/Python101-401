# VERI YAPILARI

# Listeler 

"""
1.Değiştirilebilirdir.
2.Kapsayıcıdır(Farklı tipte verileri tutabilir.)
3.Sıralıdır.
"""

# []
# list()

notlar = [90, 80, 70, 50] # liste tipinde
type(notlar) # çıktısı -> list

liste = ["a", 19.3, 90]
liste_genis = ["a", 19.3, 90, notlar]

len(liste_genis) # -> 4

liste_genis[0] # 'a'
liste_genis[1] # 19.3
liste_genis[2] # 90
liste_genis[3] # [90, 80, 70, 50]

type(liste_genis[0]) # çıktısı -> str
type(liste_genis[3]) # çıktısı -> list


tum_liste = [liste, liste_genis]

# del tum_liste

# Listeler - Eleman Islemleri

liste = [10, 20, 30, 40, 50]

liste[0] # 10
liste[1] # 20

liste[6] # IndexError: list index out of range

liste[0:2] # çıktısı -> [10, 20]

liste[:2] # çıktısı -> [10, 20]

liste[2:] # 2 den sona kadar al. Çıktısı -> [30, 40, 50]

yeni_liste = ["a",10, [20, 30, 40, 50]]
yeni_liste

yeni_liste[3] # IndexError: list index out of range

yeni_liste[2] # çıktısı ->[20, 30, 40, 50]
yeni_liste[0:2] # çıktısı -> ['a', 10]


yeni_liste[2][1] # çıktısı -> 30


#Listeler - Eleman Degistirme

liste = ["ali", "veli", "betul", "ayse"]
liste

liste[1] = "velinin_babasi"

liste # çıktı->['ali', 'velinin_babasi', 'betul', 'ayse']

liste[1] = "veli"

liste[0:3] = "alinin_babasi", "velinin_babasi","betulun_babasi"

liste # çıktı -> ['alinin_babasi', 'velinin_babasi', 'betulun_babasi', 'ayse']


liste = ["ali", "veli", "betul", "ayse"]
liste

liste + ["kemal"] # çıktı -> ['ali', 'veli', 'betul', 'ayse', 'kemal']
liste # çıktı -> ['ali', 'veli', 'betul', 'ayse']

liste = liste + ["kemal"] 
liste # çıktısı-> ['ali', 'veli', 'betul', 'ayse', 'kemal']

del liste[2]
liste # berkcan silindi -> ['ali', 'veli', 'ayse', 'kemal']


# Listeler - Liste Metodları

liste = ["ali", "veli", "isik"]

dir(liste)

#append -> ekleme
liste.append("berkcan")
liste # çıktısı -> ['ali', 'veli', 'isik', 'berkcan']

#remove -> çıkarma
liste.remove("berkcan")
liste # çıktısı -> ['ali', 'veli', 'isik']


# insert -> indexe göre eleman ekler

liste = ["ali", "veli", "isik"]
liste

liste.insert(0,"ayse")
liste # çıktısı -> ['ayse', 'ali', 'veli', 'isik']


liste = ["ali", "veli", "isik"]
liste[0] = "ayse"
liste # çıktı -> ['ayse', 'veli', 'isik']

liste.insert(0,"ayse")
liste

liste[1] = "ali"
liste

liste.insert(2, "mehmet")
liste # çıktı -> ['ayse', 'ali', 'mehmet', 'veli', 'isik']

liste.insert(5, "berk")
liste

len(liste)
liste.insert(len(liste),"beren") # çıktı -> ['ayse', 'ali', 'mehmet', 'veli', 'isik', 'berk', 'beren']
liste


# pop -> listeden eleman çıkar

liste.pop(0)
liste # çıktı->ayse cikti -> ['ali', 'mehmet', 'veli', 'isik', 'berk', 'beren']

liste.pop(4)
liste # berk cikti -> ['ali', 'mehmet', 'veli', 'isik', 'beren']

# count 

liste = ["ali", "veli", "isik", "ali", "veli"]
liste.count("ali") # çıktı-> 2
liste.count("veli") # çıktı-> 2
liste.count("isik") # çıktı-> 1

# copy

liste_yedek = liste.copy()

# extend -> iki listeyi birleştirir

liste = ["ali", "veli", "isik"]
liste.extend(["a","b",10])
liste # çıktısı - > ['ali', 'veli', 'isik', 'a', 'b', 10]

# index()

liste.index("ali") # çıktısı -> 0

# reverse() -> listeyi tersine çevirir

liste.reverse()
liste # çıktısı - > [10, 'b', 'a', 'isik', 'veli', 'ali']

# sort () -> sıralama yapar

liste = [10, 40, 5 ,12]
liste.sort() # çıktısı ->  [5, 10, 12, 40]
liste

# clear -> listeyi temizler

liste.clear()
liste 