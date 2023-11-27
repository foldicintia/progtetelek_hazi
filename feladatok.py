import random
import math



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

# Kérj be a felhasználótól egy számot, és döntsd el, hogy szerepel -e a szám a húzott számok között?

#NEHEZEK
# Kérj be a felhasználótól 5 számot, és döntsd el, hogy van-e találata? 
# Kérj be a felhasználótól 5 számot, és a program mondja meg, hány találata van az illetőnek? 
# A húzott véletlen számok ne lehessenek azonosak!
# A felhasználótól addig kérd be a számokat, amíg 5 különbözőt ad meg!    

