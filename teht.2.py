import random

def heita_noppaa(tahkot):
    return random.randint(1, tahkot)

# Pääohjelma
def paohjelma():
    tahkot = int(input("Syötä nopan tahkojen määrä: "))
    maksimi_silmaluku = tahkot
    nopan_silmaluku = 0

    while nopan_silmaluku != maksimi_silmaluku:
        nopan_silmaluku = heita_noppaa(tahkot)
        print(f"Nopan silmäluku: {nopan_silmaluku}")

paohjelma()
