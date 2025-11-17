#!/usr/bin/env python3
"""
Beslutningsspill: Erling håndterer konflikter og motivasjon i teamet.

Tre beslutningspunkter (a/b), konsekvenser og tre mulige sluttutfall.
Kjør: python python.py
"""

def hent_valg(prompt):
    """Henter et gyldig valg 'a' eller 'b' fra brukeren."""
    while True:
        val = input(prompt).strip().lower()
        if val in ("a", "b"):
            return val
        print("Ugyldig valg. Skriv 'a' eller 'b'.")


def main():
    print("=== Beslutningsspill: Erling som teamleder ===\n")

    # Lagrer valg
    valg1 = None
    valg2 = None
    valg3 = None

    # Score avgjør sluttutfall
    score = 0

    # --- Beslutningspunkt 1 ---
    print("Situasjon 1: Konflikten mellom Silje (UX) og Sivert (IT).")
    print("Konflikten er i ferd med å bli personlig, og teamet begynner å ta parti.")
    print("a) Erling tar individuelle samtaler for å senke temperaturen før fellesmøte.")
    print("b) Erling tar konflikten i plenum for å 'rydde opp' åpent i gruppa.")
    valg1 = hent_valg("Velg a eller b: ")

    if valg1 == "a":
        print("\nKonsekvens: Begge føler seg hørt, temperaturen synker. Teamet får mer tillit til Erling.")
        score += 1
        print("Historien går videre: Silje og Sivert blir med på et strukturert dialogmøte.\n")
    elif valg1 == "b":
        print("\nKonsekvens: Konfrontasjonen skaper mer frustrasjon, og frontene blir hardere.")
        score -= 1
        print("Historien går videre: Konflikten tar mer tid enn planlagt og påvirker arbeidsflyten.\n")

    print("--- Status etter punkt 1 ---\n")

    # --- Beslutningspunkt 2 ---
    print("Situasjon 2: Spenningen mellom Hamdi og Jabir.")
    print("Deres konflikt er fortsatt lavmælt, men påvirker samarbeidet om innbyggerdialogen.")
    print("a) Erling kaller inn begge til et avklaringsmøte for å finne felles løsning.")
    print("b) Erling avventer og håper de finner ut av det selv.")
    valg2 = hent_valg("Velg a eller b: ")

    if valg2 == "a":
        print("\nKonsekvens: Misforståelser avklares, og de finner en hybridløsning.")
        score += 1
        print("Historien går videre: De blir tryggere på samarbeid fremover.\n")
    elif valg2 == "b":
        print("\nKonsekvens: Konflikten ulmer videre og begynner å påvirke prototypeplanleggingen.")
        score -= 1
        print("Historien går videre: Uenigheten blir mer synlig for de andre i teamet.\n")

    print("--- Status etter punkt 2 ---\n")

    # --- Beslutningspunkt 3 ---
    print("Situasjon 3: Motivasjonen i teamet faller.")
    print("Prototype-fristen nærmer seg, men energien er lav etter flere konflikter.")
    print("a) Erling setter av tid til feiring av små seire og relasjonsbygging.")
    print("b) Erling fokuserer kun på fremdrift og strammer inn planene.")
    valg3 = hent_valg("Velg a eller b: ")

    if valg3 == "a":
        print("\nKonsekvens: Moralen løftes, teamet viser mer samarbeid og positivitet.")
        score += 1
    elif valg3 == "b":
        print("\nKonsekvens: Leveransetakten øker midlertidig, men motivasjonen faller ytterligere.")
        score -= 1

    print("\n--- Sammendrag av dine valg ---")
    print(f"1) Silje vs Sivert: {valg1}")
    print(f"2) Hamdi vs Jabir: {valg2}")
    print(f"3) Teamets motivasjon: {valg3}")
    print(f"Score: {score}\n")

    # Sluttutfall
    if score >= 2:
        slutt = "Samarbeidet styrkes"
        beskrivelse = (
            "Erling lykkes med å løse konfliktene, motivasjonen løftes og "
            "prototypen leveres med godt samarbeid og høy kvalitet."
        )
    elif score == 1:
        slutt = "Delvis løst"
        beskrivelse = (
            "Teamet kommer seg videre, men spenning gjenstår. Prosjektet holder så vidt fremdrift."
        )
    else:
        slutt = "Prosjektet forsinkes"
        beskrivelse = (
            "Konfliktene eskalerer, motivasjonen faller og prototypen blir forsinket. "
            "Erling må ta grep for å redde prosjektet."
        )

    print("=== Sluttresultat ===")
    print(f"Utfallet: {slutt}")
    print(beskrivelse)


if __name__ == "__main__":
    main()
