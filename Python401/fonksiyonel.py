# Fonksiyonel Programlama

# Fonksiyonlar dilin bastacidir.
# Fonkssiyonlar (Birinci sinif nesnelerdir.)
# Yan etkisiz fonksiyonlar (stateless, girdi-cikti)
# Yuksek seviye fonksiyonlar
# Vektorel operasyonlar


#Yan Etkisiz Fonksiyonlar (Pure Functions)

#Ornek1: Bagimsizlik

A = 9

def impure_sum(b): # fonksiyonun dişarıdan bir bağımlılığı var
    return b + A

def pure_sum(a,b):
    return a + b

impure_sum(6)
pure_sum(3, 4)


#Ornek2 : Olumcül Yan Etkiler
#OOP
class LineCounter:
    def __init__(self,filename):
        self.file = open(filename, 'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
    
    def count(self):
        return len(self.lines)

lc = LineCounter('deneme.txt')
print(lc.lines)
print(lc.count())

lc.read()

print(lc.lines)
print(lc.count())


#FP
def read(filename):
    with open(filename, "r") as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read("deneme.txt")
lines_count = count(example_lines)
lines_count

# ancak bir girdi verdiğimizde çıktı üretecek şekilde değişecektir

# bagimsiz


# Isimsiz Fonksiyonlar (Anonymous Functions)

def old_sum(a,b):
    return a+b

old_sum(4, 5)

new_sum = lambda a, b : a + b

new_sum(4,5)

sirasiz_liste = [('b',3), ('a', 8), ('d', 12), ('c', 1)]
sirasiz_liste

sorted(sirasiz_liste, key = lambda x: x[1])
sorted(sirasiz_liste, key = lambda x: x[0])


# Vektorel Operasyonlar
#OOP
a = [1,2,3,4]
b = [2,3,4,5]

ab = []

range(0, len(a)) # çıktısı -> range(0, 4)

for i in range(0, len(a)):
    ab.append(a[i]*b[i])
    
ab

#FP

import numpy as np
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])

a*b

# map & filter & reduce

liste = [1,2,3,4,5]

for i in liste:
    print(i+10)

list(map(lambda x: x*10,liste))
# map fonksiyonu verilen vektörün içerisinde belirli bir fonksiyonu çalıştırma imkanı verir

# filter 
# filter fonksiyonu iteratif bir nesne alır, bu nesne üzerinden başka bir iteratif nesne oluşturulur
# ve iteratif nesne içerisinde aradığı şartın sağlandığı tüm elemanlar filtrlenir.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list(filter(lambda x: x % 2 == 0, liste))

#reduce 

from functools import reduce
liste = [1,2,3,4]
reduce(lambda a,b: a+b, liste)

# bir diziyi tek bir değere indirgemeyi sağlar