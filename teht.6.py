import math


# Funktio, joka laskee pizzan yksikköhinnan euroina per neliömetri
def laske_yksikkohinta(halkaisija_cm, hinta_eurot):
    # Lasketaan pizzan pinta-ala neliömetreinä (A = pi * r^2)
    sade_m = (halkaisija_cm / 2) / 100  # Muutetaan halkaisija metreiksi ja lasketaan säde
    pinta_ala = math.pi * sade_m ** 2
    # Lasketaan yksikköhinta euroina per neliömetri
    yksikkohinta = hinta_eurot / pinta_ala
    return yksikkohinta


# Pääohjelma
if __name__ == "__main__":
    # Kysytään käyttäjältä kahden pizzan halkaisijat ja hinnat
    halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta (euroa): "))

    halkaisija2 = float(input("Anna toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Anna toisen pizzan hinta (euroa): "))

    # Lasketaan yksikköhinnat molemmille pizzoille
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    # Tulostetaan yksikköhinnat
    print(f"Ensimmäisen pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
    print(f"Toisen pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

    # Verrataan ja ilmoitetaan kumpi pizza antaa paremman vastineen
    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta1 > yksikkohinta2:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat saman vastineen rahalle.")
