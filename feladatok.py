import random
import math


"""
# Nézzük meg a lottószámok átlagát
def lotto_szamok():
    lista = []
    i = 0
    while i < 5:
        szam = math.floor(random.random()*90+1)
        lista.append(szam)
        i+=1
    return lista

def atlag():
    lista = lotto_szamok()
    print(f"A generált számok:{lista}")
    osszeg: int = 0
    db: int = 0
    atlag  = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
        db += 1
        atlag = osszeg / db
    return atlag

# Hány 50-nél nagyobb szám van közte? 
def otven_felettiek():
    lista = lotto_szamok()
    print(f"A generált számok:{lista}")
    nagyobb = 0
    for i in range(0,len(lista),1):
        if lista[i] > 50:
            nagyobb += 1
    return nagyobb


# Melyik a legnagyobb szám? 
def legnagyobb():
    lista = lotto_szamok()
    print(f"A generált számok:{lista}")
    max = lista[0]
    for i in range(0,len(lista),1):
        if max < lista[i]:
            max = lista[i]
    return max

# Hányadiknak generáltuk a a legnagyobb számot? 

# Melyik a legkisebb szám? 
def legkisebb():
    lista = lotto_szamok()
    print(f"A generált számok: {lista}")
    min = lista[0]
    for i in range(0,len(lista),1):
        if min > lista[i]:
            min = lista[i]
    return min

# A legkisebb és a leg nagyobb szám közti különbség? 
def kulonbseg():
    lista = lotto_szamok()
    print(lista)
    kulonbseg = legnagyobb()-legkisebb()
    return kulonbseg
"""
# Nézzük meg a lottószámok átlagát
def atlag2(lotto_szamok):
    osszeg = 0
    atlag = 0
    db= 0
    for i in range(0, len(lotto_szamok), 1):
        osszeg+=lotto_szamok[i]
        db+=1
    atlag=osszeg/db
    return atlag

# Hány 50-nél nagyobb szám van közte? 
def otven_felettiek2(lotto_szamok):
    nagyobb = 0
    for i in range(0,len(lotto_szamok),1):
        if lotto_szamok[i] > 50:
            nagyobb += 1
    return nagyobb

# Melyik a legnagyobb szám? 
def legnagyobb2(lotto_szamok):
    max = lotto_szamok[0]
    for i in range(0,len(lotto_szamok),1):
        if max < lotto_szamok[i]:
            max = lotto_szamok[i]
    return max

# Hányadiknak generáltuk a a legnagyobb számot? 
"""addig menjen amig a legnagyobb szammal egyenlo nem lesz az i?"""
def legnagyobb_sorszama(lotto_szamok):
    max = legnagyobb2(lotto_szamok)
    sorszam = 1
    for i in range(0,len(lotto_szamok),1):
        if lotto_szamok[i] != max:
            sorszam += 1
    return sorszam 

         

# Melyik a legkisebb szám? 
def legkisebb2(lotto_szamok):
    min = lotto_szamok[0]
    for i in range(0, len(lotto_szamok),1):
        if min > lotto_szamok[i]:
            min = lotto_szamok[i]
    return min

# A legkisebb és a legnagyobb szám közti különbség? 
def kulonbseg2(lotto_szamok):
    kulonbseg = legnagyobb2(lotto_szamok)-legkisebb2(lotto_szamok)
    return kulonbseg

# Kérj be a felhasználótól egy számot, és döntsd el, hogy szerepel -e a szám a húzott számok között?
def felhasznalo_szama(lotto_szamok):
    i = 0
    szam: int = int(input("Adj meg egy számot 1 és 90 között!"))
    while not (szam > 1 and szam < 90):
        print("Nem 1 és 90 közötti számot adtál meg!")
        szam: int = int(input("Adj meg egy számot 1 és 90 között!"))
        i += 1
    for i in range(0, len(lotto_szamok), 1):
        if lotto_szamok[i] == szam:
            return szam


            


#NEHEZEK
# Kérj be a felhasználótól 5 számot, és döntsd el, hogy van-e találata? 
# Kérj be a felhasználótól 5 számot, és a program mondja meg, hány találata van az illetőnek? 
# A húzott véletlen számok ne lehessenek azonosak!
# A felhasználótól addig kérd be a számokat, amíg 5 különbözőt ad meg!    

