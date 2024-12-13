# Hatalar / istisnalar (exceptions)
# ZeroDivisionError Hatasi
a = 10
b = 0

a/b # çıktısı -> ZeroDivisionError: division by zero

try:
    print(a/b)
except ZeroDivisionError:
    print("Payda da sifir olmaz")


# tip hatasi

a = 10
b = "2"

a/b

try:
    print(a/b)
except TypeError:
    print("Sayi ve Str problemi")


a = 10
b = 2

a/b

try:
    print(a/b)
except TypeError:
    print("Sayi ve Str problemi")

# sınav 401

from functools import reduce
a = [1,2,3,4]
reduce(lambda a,b: a*b, a)

liste = ["a",20,10,30,"b"]
list(filter(lambda x: type(x) == int, liste))

A = [1,2,3,4,5]

if type(A) == ():
    print("islem gecersiz")
else:
    print(list(map(lambda x: x/1, A)))


from functools import reduce
A = ["Veri","Bilimi","Okulu"]
reduce(lambda a,b: a+b, list(map(lambda x: x[0], A)))

import numpy as np
a = np.array([1,1,1])
b = np.array([2])

a+b


A = [[1,2],[3,4],[5,6]]
list(map(lambda x: x[0]*3, A))

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A,B]


for i in AB:
    if type(i[0]) == int:
        print(list(map(lambda x: x-3, i)))


a = [1,2,3]
list(map(lambda x: x*2, a))


A = []
for i in ["ali","veli","isik"]:
    A.append(i.replace("i","a"))
print(A)

list(map(lambda x: x/10, filter(lambda x: x > 20, [10,20,30,40,50])))

list(filter(lambda x: x < 2, [1,2,3,4,5]))

from functools import reduce
reduce(lambda a,b: a+b, ["a","4","a"])

A = ["ali","veli","isik"]
B = [1,2,3]
AB = [A, B]

for i in AB:
    if type(i[0]) == str:
        print(list(map(lambda x: x + " hi", i)))  

