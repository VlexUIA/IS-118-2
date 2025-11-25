def hent_valg(prompt):
#Sjekker om valget er riktig, og sjekker om det er A eller B
    while True:
        val = input(prompt).strip().lower()
        if val in ("a", "b"):
            return val
        print("Ugyldig valg. Velg 'A' eller 'B'.")


def main():
    print("=== Beslutningsspill: Erling som teamleder ===\n")
    print("Bakgrunn: Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal, samlet sitt prosjektteam for første gang.")
    print("Etter en inspirerende oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver. I starten var stemningen god. ")
    print("Gruppen opplevde høy motivasjon og fellesskap i målet om å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen. ")
    print("Men nå, etter seks uker, har prosjektet gått inn i den klassiske storming-fasen, der ulike faglige perspektiver og personlige preferanser begynner å kollidere")
    print("Teamet består av Erling [Teamleder], Sivert [IT-Rådgiver], Silje [UX-Designer], Hamdi [Utvikler], Jabir [Innbyggerdialogspesialist], Nora [Kvalitetssikring] og Jabir [Brukerrepresentant]")
    print("======================")

   # Situasjon 1
    print("Situasjon 1: Konflikten mellom Silje (UX) og Sivert (IT).")
    print("Konflikten er i ferd med å bli personlig, og teamet begynner å ta parti.")
    print("a) Erling tar individuelle samtaler for å senke temperaturen før fellesmøte.")
    print("b) Erling tar konflikten i plenum for å 'rydde opp' åpent i gruppa.")
    valg1 = hent_valg("Velg a eller b: ")

    if valg1 == "a":
        print("\nKonsekvens: Begge føler seg hørt, temperaturen synker. Teamet får mer tillit til Erling.")
        print("Historien går videre: Silje og Sivert blir med på et strukturert dialogmøte.\n")
    elif valg1 == "b":
        print("\nKonsekvens: Konfrontasjonen skaper mer frustrasjon, og frontene blir hardere.")
        print("Historien går videre: Konflikten tar mer tid enn planlagt og påvirker arbeidsflyten.\n")

    print("Valg etter punkt 1\n")

   # Situasjon 2
    print("Situasjon 2: Samtidig med konflikten mellom Silje og Sivert oppstår det spenningen mellom Hamdi [Kulturavdeling] og Jabir [Brukerrepresentant].")
    print("Deres konflikt er fortsatt lavmælt, men påvirker samarbeidet om innbyggerdialogen.")
    print("a) Erling kaller inn begge til et avklaringsmøte for å finne felles løsning.")
    print("b) Erling avventer og håper de finner ut av det selv.")
    valg2 = hent_valg("Velg a eller b: ")

    if valg2 == "a":
        print("\nKonsekvens: Misforståelser avklares, og de finner en hybridløsning.")
        print("Historien går videre: De blir tryggere på samarbeid fremover.\n")
    elif valg2 == "b":
        print("\nKonsekvens: Konflikten ulmer videre og begynner å påvirke prototypeplanleggingen.")
        print("Historien går videre: Uenigheten blir mer synlig for de andre i teamet.\n")

    print("Valg etter punkt 2\n")

   # Situasjon 3
    print("Situasjon 3: Motivasjonen i teamet faller.")
    print("Prototype-fristen nærmer seg, men energien er lav etter flere konflikter.")
    print("a) Erling setter av tid til feiring av små seire og relasjonsbygging.")
    print("b) Erling fokuserer kun på fremdrift og strammer inn planene.")
    valg3 = hent_valg("Velg a eller b: ")

    if valg3 == "a":
        print("\nKonsekvens: Moralen løftes, teamet viser mer samarbeid og positivitet.")
    elif valg3 == "b":
        print("\nKonsekvens: Leveransetakten øker midlertidig, men motivasjonen faller ytterligere.")


    print("Valg etter punkt 3\n")
    print("\nSammendrag av dine valg:")
    print(f"1) Silje vs Sivert: {valg1}")
    print(f"2) Hamdi vs Jabir: {valg2}")
    print(f"3) Teamets motivasjon: {valg3}")
    print()

    # Avslutning
    print("=== Sluttresultat ===")
    print("Refleksjon: Dine valg illustrerer hvilke tilnærminger du ville brukt i teamet.")
    print("Vurder hvilke handlinger som best bygger tillit, løser konflikter og sikrer fremdrift.")
    # Faktorer, utfordringer og hovedbeslutninger
    faktorer = "Åpen kommunikasjon, tillit, klare roller"
    utfordringer = "Uenighet i faglig tilnærming, lav motivasjon etter konflikter"
    hovedbeslutninger = "Individuelle samtaler, avklaringsmøter og relasjonsbygging"

    print(f"Faktorer: {faktorer}")
    print(f"Utfordringer: {utfordringer}")
    print(f"Hovedbeslutninger: {hovedbeslutninger}\n")


if __name__ == "__main__":
    main()
