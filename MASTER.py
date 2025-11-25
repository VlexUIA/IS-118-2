
    #Gjør sikker på at valget er A eller B, hvis valget er feil, så spør den igjen og viser "Ugyldivg valg. Velg 'A' eller 'B'.
def hent_valg(prompt):
    while True:
        val = input(prompt).strip().lower()
        if val in ("a", "b"):
            return val
        print("Ugyldig valg. Velg 'A' eller 'B'.")


    #Definerer main og begynner spillet | Bruker print til å definere historien.
def main():
    print("=== Beslutningsspill: Erling som teamleder ===\n")
    print("Bakgrunn: Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal, samlet sitt prosjektteam for første gang.")
    print("Etter en inspirerende oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver. I starten var stemningen god. ")
    print("Gruppen opplevde høy motivasjon og fellesskap i målet om å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen. ")
    print("Men nå, etter seks uker, har prosjektet gått inn i den klassiske storming-fasen, der ulike faglige perspektiver og personlige preferanser begynner å kollidere")
    print("Teamet består av Erling [Teamleder], Sivert [IT-Rådgiver], Silje [UX-Designer], Hamdi [Utvikler], Jabir [Innbyggerdialogspesialist], Nora [Kvalitetssikring] ")
    print ("og Jabir [Brukerrepresentant]")
    print("======================")

    total_poeng = 0

    # Situasjon 1 – Sivert vs Silje
    print("Situasjon 1: Konflikten mellom Silje (UX) og Sivert (IT).")
    print("a) Erling setter opp gruppemøte")
    print("b) Autoritært valg: Silje får viljen sin")
    valg1 = hent_valg("Velg a eller b: ")

     #Hvis valget er A så kommer Konsekvens X, hvis valg b så kommer Konsekvens Y
    if valg1 == "a":
        print("\nKonsekvens: Hybrid løsning – samhold og enighet i gruppen.")
        total_poeng += 2
    else:
        print("\nKonsekvens: Sivert truer med å slutte.")
        total_poeng += 1

    # Situasjon 2 – Hamdi vs Jabir
    print("Situasjon 2: Samtidig med konflikten mellom Silje og Sivert oppstår det spenningen mellom Hamdi [Kulturavdeling] og Jabir [Brukerrepresentant].")
    print("a) Erling setter opp personlig møte")
    print("b) Erling setter opp obligatorisk møte")
    valg2 = hent_valg("Velg a eller b: ")

    #Hvis valget er A så kommer Konsekvens X, hvis valg b så kommer Konsekvens Y
    if valg2 == "a":
        print("\nKonsekvens: Det blir krangel – Erling får dårlig leder-rykte.")
        total_poeng += 1
    else:
        print("\nKonsekvens: Gruppen blir enige og fornøyde.")
        total_poeng += 2

    # Situasjon 3 – Teamets motivasjon
    print("Situasjon 3: Motivasjonen i teamet faller.")
    print("a) Bowling som gruppe")
    print("b) Fokus på leveranse og fremdrift")
    valg3 = hent_valg("Velg a eller b: ")

     #Hvis valget er A så kommer Konsekvens X, hvis valg b så kommer Konsekvens Y
    if valg3 == "a":
        print("\nKonsekvens: Mer motivasjon i gruppen.")
        total_poeng += 2
    else:
        print("\nKonsekvens: Dårlig moral, overbelastning og slitenhet.")
        total_poeng += 1

    # Resultat | Gir sluttresultatet basert på poengsummen brukeren har fått gjennom valgene sine og viser hvor mye poeng brukeren har fått.
    print("\n=== Sluttresultat ===")
    if total_poeng == 3:
        print("Dårlig Resultat: Lite brukbart produkt.")
    elif total_poeng in (4, 5):
        print("Middels Resultat: Produktet mangler innovasjon og helhet.")
    elif total_poeng == 6:
        print("Bra Resultat: Kommunen er fornøyd!")
    else:
        print("Uventet poengsum – sjekk logikken.")
    print(f"Total poengsum: {total_poeng} av 6")

    # Oppsummering av valg
    print("\n=== Oppsummering ===")
    print(f"1) Silje vs Sivert: {valg1}")
    print(f"2) Hamdi vs Jabir: {valg2}")
    print(f"3) Teamets motivasjon: {valg3}")

    #Gir muligheten til å starte spillet stasjonært. 
if __name__ == "__main__":
    main()
