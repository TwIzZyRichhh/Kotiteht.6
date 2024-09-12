import random

def noppa():
    return random.randint(1, 6)

def paohjelma():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = noppa()
        print(f"Nopan silmäluku: {silmaluku}")

paohjelma()
