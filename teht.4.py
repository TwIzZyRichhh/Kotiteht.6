# Funktio, joka laskee listan kokonaislukujen summan
def laske_summa(lista):
    return sum(lista)


# Pääohjelma
if __name__ == "__main__":
    # Luodaan lista kokonaisluvuista
    numerot = [3, 5, 7, 10, 2]

    # Kutsutaan funktiota ja tallennetaan summa
    summa = laske_summa(numerot)

    # Tulostetaan listan summa
    print(f"Listan {numerot} summa on: {summa}")
