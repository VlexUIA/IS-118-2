# Sjekker at valget er A eller B, hvis ikke så skriver det ut en feilmelding og spør på nytt
def hent_valg(prompt):
    while True:
        val = input(prompt).strip().lower()
        if val in ("a", "b"):
            return val
        print("Ugyldig valg. Velg 'A' eller 'B'.")

    # Definerer main og begynner spillet.
def main():
    print("\n=== Beslutningsspill: Erling som teamleder ===\n")
    print("Bakgrunn: Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal, samlet sitt prosjektteam for første gang.")
    print("Etter en inspirerende oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver. I starten var stemningen god. ")
    print("Gruppen opplevde høy motivasjon og fellesskap i målet om å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen. ")
    print("Men nå, etter seks uker, har prosjektet gått inn i den klassiske storming-fasen, der ulike faglige perspektiver og personlige preferanser begynner å kollidere")
    print("Teamet består av Erling [Teamleder], Sivert [IT-Rådgiver], Silje [UX-Designer], Hamdi [Utvikler], Jabir [Innbyggerdialogspesialist], Nora [Kvalitetssikring] og Jabir [Brukerrepresentant]")
    print("======================")

    total_poeng = 0

    # Situasjon 1 – Silje vs Sivert
    print("\nSituasjon 1: Personkonflikten mellom Silje (UX) og Sivert (IT).")
    print("a) Erling setter opp et gruppemøte med åpen diskusjon.")
    print("b) Erling tar et autoritært valg og støtter Silje.")
    valg1 = hent_valg("Velg a eller b: ")

    #Sjekker hvilket valg du har tatt, og gir poengsum
    if valg1 == "a":
        print("\nKonsekvens: Gruppen finner en hybridløsning og enigheten øker.")
        total_poeng += 2
    else:
        print("\nKonsekvens: Sivert reagerer negativt og vurderer å slutte.")
        total_poeng += 1

    # Situasjon 2 – Hamdi vs Jabir
    print("\nSituasjon 2: Latent konflikt mellom Hamdi og Jabir om plattformvalg.")
    print("a) Erling tar opp konflikten tidlig og holder et møte.")
    print("b) Han ignorerer spenningen og håper det løser seg selv.")
    valg2 = hent_valg("Velg a eller b: ")

    #Sjekker hvilket valg du har tatt, og gir poengsum
    if valg2 == "a":
        print("\nKonsekvens: Gruppen blir enige om en kombinasjonsløsning – konflikten avverges.")
        total_poeng += 2
    else:
        print("\nKonsekvens: Konflikten eskalerer og effektiviteten faller.")
        total_poeng += 1

    # Situasjon 3 – Teamets motivasjon
    print("\nSituasjon 3: Motivajsonen i gruppen faller.")
    print("a) Gruppeaktivitet: Bowling og relasjonsbygging.")
    print("b) Økt arbeidspress og lengre arbeidsdager.")
    valg3 = hent_valg("Velg a eller b: ")

    #Sjekker hvilket valg du har tatt, og gir poengsum
    if valg3 == "a":
        print("\nKonsekvens: Gruppen får bedre humør og økt motivasjon.")
        total_poeng += 2
    else:
        print("\nKonsekvens: Gruppen blir overbelastet og moral synker.")
        total_poeng += 1

    # Resultater
    print("\n=== Sluttresultat ===")
    if total_poeng == 3:
        print("Dårlig resultat: Teamet leverer et lite brukbart produkt.")
    elif total_poeng in (4, 5):
        print("Middels resultat: Produktet mangler innovasjon og helhet.")
    elif total_poeng == 6:
        print("Bra resultat: Kommunen er fornøyd med både prosess og produkt!")
    else:
        print("Uventet poengsum – sjekk logikken.")
    print(f"Total poengsum: {total_poeng}")

    # Oppsummering
    print("\n=== Oppsummering ===")
    print(f"1) Silje vs Sivert: {valg1}")
    print(f"2) Hamdi vs Jabir: {valg2}")
    print(f"3) Teamets motivasjon: {valg3}")
    print("======================")
    print("Takk for at du spilte!")
    print("======================\n")


if __name__ == "__main__":
    main()
