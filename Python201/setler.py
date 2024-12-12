# Veri yapıları - Setler

"""
1. Sırasızdır
2. Değerleri eşsizdir
3. Değiştirilebilirdir
4. Farklı tipleri barındırabilir
"""

# Set olusturmak
# Kümeler olarak düşünülebilir. Matematiksel anlamda

s = set()    
s

l = [1,"a","ali", 123]
s = set(l)
s

t = ("a", "ali")
s = set(t)
s

ali = "lutfen_ata_bak ma_uza ya_git"
type(ali) # str

s = set(ali)
s
""" çıktısı ->
{' ',
 '_',
 'a',
 'b',
 'e',
 'f',
 'g',
 'i',
 'k',
 'l',
 'm',
 'n',
 't',
 'u',
 'y',
 'z'}
"""

l = ["ali", "lutfen", "ata", "bakma", "uzaya", 
     "git", "git", "ali","git"]
l

s = set(l)
s # listedeki elemanlar sadece bir defa alınır {'ali', 'ata', 'bakma', 'git', 'lutfen', 'uzaya'}

len(s) # 6

l[0] # -> 'ali'
s[0] # -> TypeError: 'set' object is not subscriptable


# Eleman Ekleme & Cikarma 

l = ["gelecegi", "yazanlar"]

s = set(l)
s # çıktısı -> {'gelecegi', 'yazanlar'}

dir(s)

s.add("ile")
s

s.add("gelecege_git")
s # çıktısı -> {'gelecege_git', 'gelecegi', 'ile', 'yazanlar'}


s.add("ile")
s # var olan bir değeri tekrar eklemiyor

s.remove("ali")
s # çıktı -> {'gelecege_git', 'gelecegi', 'ile', 'yazanlar'}

s.remove("ali")
s # KeyError: 'ali'

s.discard("ali")
s # eleman içinde olmasa bile hata vermez

# Setler - Klasik Kume İslemleri

# =============================================================================
# difference() ile iki kumenin farkını ya da "-" ifadesi
# intersection() iki kume kesişimi ya da "&" ifadesi
# union() iki kumenin birleşimi
# symmetric_difference() ikisinde de olmayanları
# =============================================================================

# difference 

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2) # set1 de olup set2 de olmayanları getirdi. çıktısı -> {5}

set2.difference(set1) # çıktısı -> {2}

set1.symmetric_difference(set2) # çıktısı -> {2, 5}

set1 - set2 # {5}
set2 - set1 # çıktısı -> {2}

#intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2) # {1, 3}
set2.intersection(set1) # {1, 3}

kesisim = set1 & set2 # {1, 3}
kesisim

set1.union(set2) # {1, 2, 3, 5}

birlesim = set1.union(set2)
birlesim

set2.union(set1) # {1, 2, 3, 5}

set1.intersection_update(set2)
set1 # {1, 3}


# Set Sorgu İslemleri

set1 = set([7,8,9])
set2 = set ([5,6,7,8,9,10])


# iki kumenin kesişiminin bos olup olmadıgının sorgulaması
set1.isdisjoint(set2) # False döner

# bir kumenin butun elemanlarının baska bir kume içerisinde yer alıp almadigi
# set1 set2'nin alt kumesi midir?
set1.issubset(set2) # True döner

# bir kumenin bir diğer kumeyi kapsayıp kapsamadığı
# set2 set1 i kapsıyor mu?
set2.issuperset(set1) # True döner


# 201 sınav
liste = [10,20,30,40]
liste.pop(1)
liste

liste = ["a","b","c"]
liste.extend(liste)
liste

sozluk = {"REG" : {"RMSE": 10,
"MSE": 11,
"SSE": 12},
 
"LOJ" : {"RMSE": 111,
"MSE": 2222,
"SSE": 333},
 
"CART" : {"RMSE": 99,
"MSE": 00,
"SSE": 66}}

sozluk["CART"]["SSE"]
 

liste = ["A","B","C"]
liste.insert(0, "D")
liste


liste = ["a","b","c"]
liste.index("b")

t = ("a",10,"b")
t[0] = 1


liste = [10,10,20,40]
liste.clear()
liste

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.difference(set2)

liste = ["a","b","c"]
liste.reverse()
print(liste)

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.union(set2)

set1 = set([5,7,9])
set2 = set([5,6,7])
set1.symmetric_difference(set2)


sozluk = {"REG" : {"RMSE": 10,
"MSE": 11,
"SSE": 12},
 
"LOJ" : {"RMSE": 111,
"MSE": 2222,
"SSE": 333},
 
"CART" : {"RMSE": 99,
"MSE": 00,
"SSE": 66}}

sozluk["LOJ"]["MSE"]

