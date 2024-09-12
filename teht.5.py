# Funktio, joka palauttaa listan ilman parittomia lukuja
def karsi_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]


# Pääohjelma
if __name__ == "__main__":
    # Luodaan lista kokonaisluvuista
    numerot = [3, 5, 7, 10, 2, 8, 1, 14]

    # Kutsutaan funktiota ja tallennetaan karsittu lista
    karsittu_lista = karsi_parittomat(numerot)

    # Tulostetaan alkuperäinen ja karsittu lista
    print(f"Alkuperäinen lista: {numerot}")
    print(f"Karsittu lista (ilman parittomia lukuja): {karsittu_lista}")
