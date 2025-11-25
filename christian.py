# Seette opp poengsystem
poengsum = 0

poeng_riktig = 3
poeng_kompromiss = 2
poeng_feil = 1

# Funksjon for å spørre bruker om valg på konflikter
def spør_valg(konflikt_text):
    """Spør bruker om valg 1/2/3, validerer og returnerer poeng for valget."""
    while True:
        print()
        print(konflikt_text)
        print("1) Dårlig valg")
        print("2) Kompromiss")
        print("3) Godt valg")
        valg = input("Velg 1, 2 eller 3: ").strip()
        if valg == "1":
            print("Dårlig valg")
            return poeng_feil
        elif valg == "2":
            print("Kompromiss")
            return poeng_kompromiss
        elif valg == "3":
            print("Godt valg")
            return poeng_riktig
        else:
            print("Ugyldig valg — prøv igjen (skriv 1, 2 eller 3).")

# Introduksjon og start
print("Erling har konflikter han må løse, velg de beste valga mulig for han")
input("Trykk Enter for å starte...")  # Setter startknappen til Enter

# Konflikt 1
poengsum += spør_valg("Konflikt 1: Uenighet med teknologivalg Silje vs Sivert")

# Konflikt 2
poengsum += spør_valg("Konflikt 2: Deltakelse i digitale møter - Hamdi vs Jabir")

# Konflikt 3
poengsum += spør_valg("Konflikt 3: Motivasjon for laget - Fremdrift, Hygg, Eller begge?")

# Sammendrag / poengvurdering
print()
print(f"Din totale poengsum: {poengsum}")

if poengsum <= 4:
    print("Du direkte feilet i å løse konfliktene, prosjektet mislyktes.")
elif 5 <= poengsum <= 6:
    print("Du var litt for ubesluttsom, prosjektet ble forsinket men kom fram til slutt.")
else:
    print("Prosjekt løst utmerket, teamet fikk levert og alle er fornøyde.")
