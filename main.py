import feladatok

lista = feladatok.lotto_szamok()
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




























