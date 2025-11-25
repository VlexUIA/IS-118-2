# Sjekker at valget er A eller B
def hent_valg(prompt):
    while True:
        val = input(prompt).strip().lower()
        if val in ("a", "b"):
            return val
        print("Ugyldig valg. Velg 'A' eller 'B'.")


def main():
    print("=== Beslutningsspill: Erling som teamleder ===\n")
    print("Bakgrunn: Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal, samlet sitt prosjektteam for første gang.")
    print("Oppstarten var positiv, men nå har gruppen kommet inn i storming-fasen hvor konflikter og uenigheter oppstår.")
    print("Teamet består av: Erling (Teamleder), Sivert (IT-rådgiver), Silje (UX-designer), Hamdi (Utvikler), Jabir (Innbyggerrepresentant) og Nora (Kvalitetssikring).")
    print("======================\n")

    total_poeng = 0

    # Situasjon 1 – Silje vs Sivert
    print("Situasjon 1: Personkonflikten mellom Silje (UX) og Sivert (IT).")
    print("a) Erling setter opp et gruppemøte med åpen diskusjon.")
    print("b) Erling tar et autoritært valg og støtter Silje.")
    valg1 = hent_valg("Velg a eller b: ")

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
    print(f"Total poengsum: {total_poeng} av 6")

    # Oppsummering
    print("\n=== Oppsummering ===")
    print(f"1) Silje vs Sivert: {valg1}")
    print(f"2) Hamdi vs Jabir: {valg2}")
    print(f"3) Teamets motivasjon: {valg3}")


if __name__ == "__main__":
    main()
