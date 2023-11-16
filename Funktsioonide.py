from math import pi
from math import sqrt

# 1
# Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
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

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = aeg / teepikkus
print("Sinu kiirus oli " + str(kiirus) + " km/h")

# 0/0 = ZeroDivisionError: division by zero

# 7 Koostada programm, mis arvutab aritmeetilise keskmise suvalisest etteantud 5 täis arvust.
print("\n-----7-----\n")
nua=1
while(nua <= 5):
    print(nua)
    nua+=1

# 8 Joonista samasugune konn #
print("\n-----8-----\n")
print('  @..@  ')
print(' (----) ')
print('( \__/ )')
print('^^ "" ^^')

# 9 Arvutame kolmnurga ümbermõõdu. Loo kolm täisarvulist muutujat a, b, c. Loo valem, mis arvutab kolmnurga ümbermõõdu (P=a+b+c)
print("\n-----9-----\n")

a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
P=a+b+c
print(P)

#10 Pitsa
#    Võtsite P sõbraga suure pitsa hinnaga 12,90€
#    Jätate teenindajale 10% jootraha
#    Koosta programm, mis leiab kui palju peab igaüks maksma
print("\n-----10-----\n")

P = 12.90
Per= 10
Pansw = round(P+(P*(10/100)),2)
print("leiab ", Pansw,"€")
