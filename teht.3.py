def gallona_litroiksi(gallona):
    return gallona * 3.785

def paohjelma():
    while True:
        try:
            gallonat = float(input("Anna bensan määrä gallonoina (negatiivinen lopettaa): "))

            if gallonat < 0:
                print("Ohjelma lopetettu.")
                break

            litrat = gallona_litroiksi(gallonat)

            print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")

        except ValueError:
            print("Anna kelvollinen numero.")

paohjelma()
