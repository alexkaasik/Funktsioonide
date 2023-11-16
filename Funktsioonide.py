from math import pi
from math import sqrt
from random import *

# 1 Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
# Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitav sind Mati”, kui kasutaja nimi on Mati.
# Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
# “Tere, maailm! Tervitav sind Mati! Ma olen N aastat vana.”
print("-----1-----\n")

print("“Tere, maailm!”")
nimi=str(input("nini: "))
print("Tere, maailm! Tervitav sind ",nimi ,", kui kasutaja nimi on ",nimi ,".")
N=int(input("number of age: "))
print("Tere, maailm! Tervitav sind Mati! Ma olen ", N ," aastat vana.")

# 2 Mis tüüpi on järgnevad muutujad:
# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 16.5
# d) kas_käib_koolis = True

#Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
#Kirjuta kood tüüpide kontrollimiseks.
print("\n-----2-----\n")

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

print(type(vanus)) # int
print(type(eesnimi)) # str
print(type(pikkus)) # float
print(type(kas_käib_koolis)) # bool

#3 Kirjuta enda mängu koodis laual olevate kommide arv muutujasse. Seejärel kuva muutujas olev kommide arv ekraanile kasutades print() käsku.
#Küsi kasutajalt sisendit, mitu kommi ta soovib laualt ära võtta. Eemalda soovitud kommide arv laual olevate kommide arvust ja kuva ekraanile, kui palju komme laual nüüd on.
print("\n-----3-----\n")

candy = 6
print(candy, " candy are aviable")
take = int(input("how many to take: "))
print(candy-take)

#4 Puu läbimõõdu arvutamine
#Kirjuta programm, mis küsib kasutaja käest puu ümbermõõdu ning teatab selle peale puu läbimõõdu
print("\n-----4-----\n")

puu = float(input("give me circumference number: "))
radius = round(puu/(2*pi),4)
print("Report: the radius of circumference is ", radius)

#5 Arvutage Pythoni käsureal, kui pikk on ristkülikukujulise maatüki diagonaal, mille mõõtmed on Nm x Mm. N ja M küsi kasutajalt
print("\n-----5-----\n")

Nm = int(input("adding number for Nm(int): "))
Mm = int(input("adding number for Mm(int): "))
print("diagonaal Nm ja Mm ", round(sqrt(Nm**2+Mm**2),3) )

N  = int(input("adding number for N(int): "))
M  = int(input("adding number for M(int): "))
print("diagonaal N ja M", round(sqrt(N**2+M**2),3) )

# 6 Leidke järgnevast näiteprogrammist semantiline viga:
print("\n-----6-----\n")
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
    kiirus = teepikkus/aeg
    print("Sinu kiirus oli " + str(kiirus) + " km/h")
except:
    print("ZeroDivisionError: division by zero or/and Could not convert string to float: 'word'")

# 7 Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
print("\n-----7-----\n")
j0=randint(1,10)
j1=randint(1,10)
j2=randint(1,10)
j3=randint(1,10)
j4=randint(1,10)

print("Arvude {0},{1},{2},{3} ja {4} aritmeetilise keskmise {5}".format(j0,j1,j2,j3,j4, (j0+j1+j2+j3+j4)/5) )

# 8 Joonista samasugune konn #
print("\n-----8-----\n")
print('  @..@  ')
print(' (----) ')
print('( \__/ )')
print('^^ "" ^^')

# 9 Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
print("\n-----9-----\n")

a=randint(1,10)
b=randint(1,10)
c=randint(1,10)
P=a+b+c
print(P)

#10 Pitsa
#    Võtsite P sõbraga suure pitsa hinnaga 12,90€
#    Jätate teenindajale 10% jootraha
#    Koosta programm, mis leiab kui palju peab igaüks maksma
print("\n-----10-----\n")

P = int(input("Palju sõbre: "))
print("palju maksmab sõbraga", round( P/(12.90 * (1 + 10 / 100 ) ), 2),"€")