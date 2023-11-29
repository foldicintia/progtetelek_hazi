import feladatok

"""lista = feladatok.lotto_szamok()
print(lista)

atlag = feladatok.atlag()
print(f"A generált számok átlaga: {atlag}")

nagyobb = feladatok.otven_felettiek()
print(f"{nagyobb} db 50 feletti szám van a generélt számok között.")

max = feladatok.legnagyobb()
print(f"A generált számok közötti legnagyobb szám: {max}")



min = feladatok.legkisebb()
print(f"A legkisebb generált szám: {min}")

kulonbseg = feladatok.kulonbseg()
print(f"A legkisebb és a legnagyobb generált szám közötti különbség: {kulonbseg}")
"""

lotto_szamok=(5,22,14,58,66)

atlag = feladatok.atlag2(lotto_szamok)
print(f"A lottószámok átlaga: {atlag}")


nagyobb = feladatok.otven_felettiek2(lotto_szamok)
print(f"{nagyobb} db 50 feletti szám van a lottószámok között.")


max = feladatok.legnagyobb2(lotto_szamok)
print(f"A legnagyobb szám: {max}")

sorszam = feladatok.legnagyobb_sorszama(lotto_szamok)
print(f"A legnagyobb szám a/az {sorszam}. lottószám.")

min = feladatok.legkisebb2(lotto_szamok)
print(f"A legkisebb szám: {min}")

kulonbseg = feladatok.kulonbseg2(lotto_szamok)
print(f"A legkisebb és a legnagyobb szám közötti különbség: {kulonbseg}")

szam = feladatok.felhasznalo_szama(lotto_szamok)
print(f"Az általad megadott -{szam}- szám szerepel a lottószámok között.")














