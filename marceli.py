#!/usr/bin/env python3

#Funksjon for å hente valg med valgmuligheter
def hent_valg(prompt, alternativer):
    alternativer = [a.lower() for a in alternativer]
    vis = '/'.join(alternativer).upper()
    while True:
        val = input(f"{prompt} ({vis}): ").strip().lower()
        if val in alternativer:
            return val
        print(f"Ugyldig valg. Velg {vis}.")

#Sammendrag funksjon
def vis_sammendrag(valg):
    print("\n=== Sammendrag av dine valg ===\n")
    print(f"Konflikt 1: {valg['konflikt1_tekst']}")
    print(f"Ditt valg: {valg['konflikt1_valg']}")
    print(f"Konsekvens: {valg['konflikt1_konsekvens']}\n")
    print(f"Konflikt 2: {valg['konflikt2_tekst']}")
    print(f"Ditt valg: {valg['konflikt2_valg']}")
    print(f"Konsekvens: {valg['konflikt2_konsekvens']}\n")
    print(f"Konflikt 3: {valg['konflikt3_tekst']}")
    print(f"Ditt valg: {valg['konflikt3_valg']}")
    print(f"Konsekvens: {valg['konflikt3_konsekvens']}\n")
    print(f"Sluttresultat: {valg['utfall']}\n")
    print("Takk for at du spilte!")

#Definerer main og begynner spillet.
def main():
    print("=== Beslutningsspill: Erling som teamleder ===\n")
    print("Bakgrunn: Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens nye digitale medborgerportal, samlet sitt prosjektteam for første gang.")
    print("Etter en inspirerende oppstart med høy energi, begynner samarbeidet nå å møte sine første reelle prøver. I starten var stemningen god. ")
    print("Gruppen opplevde høy motivasjon og fellesskap i målet om å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen. ")
    print("Men nå, etter seks uker, har prosjektet gått inn i den klassiske storming-fasen, der ulike faglige perspektiver og personlige preferanser begynner å kollidere")
    print("Teamet består av Erling [Teamleder], Sivert [IT-Rådgiver], Silje [UX-Designer], Hamdi [Utvikler], Jabir [Innbyggerdialogspesialist], Nora [Kvalitetssikring] og Jabir [Brukerrepresentant]\n")
    print("======================\n")

    # Konflikt 1
    print("Konflikt 1:\nUenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til en personkonflikt. ")
    print("Silje mener løsningen Sivert foreslår vil låse brukeropplevelsen og hindre innovasjon. Siver mener Siljes forslag er urealistisk, usikker og for kostbart.\n")
    print("Valg:")
    print("a) Erling inkluderer hele gruppen i beslutningsprosessen og finner en ny løsning sammen.")
    print("b) Erling tar et autoritært valg og velger Siljes forslag, noe som øker friksjonen.")
    print("c) Erling utsetter avgjørelsen og håper konflikten løser seg selv.")
    valg1 = hent_valg("Hva gjør Erling?", ["a", "b", "c"])

#Valg som personen har tatt lagres i variabler
    if valg1 == "a":
        konflikt1_konsekvens = "God løsning: Åpen kommunikasjon, alle blir hørt, og gruppen finner en ny løsning sammen."
        konflikt1_tekst = "Erling inkluderer hele gruppen og finner en ny løsning."
    elif valg1 == "b":
        konflikt1_konsekvens = "Dårlig løsning: Erling bruker makt, velger Siljes forslag, og Sivert vurderer å slutte. Dårligere klima."
        konflikt1_tekst = "Erling tar et autoritært valg og velger Siljes forslag."
    else:
        konflikt1_konsekvens = "Passiv løsning: Konflikten ulmer videre, og teamet blir mer delt. Beslutningen utsettes og prosjektet stopper opp."
        konflikt1_tekst = "Erling utsetter avgjørelsen og håper konflikten løser seg selv."

    # Konflikt 2
    print("\nKonflikt 2:\nSamtidig med konflikten mellom Silje og Sivert oppstår det spenning mellom Hamdi (kulturavdelingen) og Jabir (brukerrepresentant). De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter. ")
    print("Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform. Jabir ønsker et mer åpent, dialogbasert system med rom for spontane innspill. ")
    print("Gruppen skal snart levere sin første prototype og Erling vet at valget han tar kan påvirke om gruppen klarer å levere prototypen og komme seg ut av storming fasen.\n")
    print("Valg:")
    print("a) Erling setter opp et møte med hele gruppen, diskusjonen blir intens men de finner en hybridløsning sammen.")
    print("b) Erling har et møte med kun Hamdi og Jabir, men må til slutt ta et autoritært valg og velger Hamdis forslag.")
    print("c) Erling ignorerer konflikten og håper de finner ut av det selv.")
    valg2 = hent_valg("Hva gjør Erling?", ["a", "b", "c"])

#Valg som personen har tatt lagres i variabler [2.0]
    if valg2 == "a":
        konflikt2_konsekvens = "God løsning: Gruppen finner en hybridløsning, alle blir fornøyd, og samarbeidet styrkes."
        konflikt2_tekst = "Erling inkluderer hele gruppen og de finner en hybridløsning."
    elif valg2 == "b":
        konflikt2_konsekvens = "Dårlig løsning: Erling tar et autoritært valg, velger Hamdis forslag, og Jabir føler seg overkjørt. Dårlig stemning og lav motivasjon."
        konflikt2_tekst = "Erling tar et autoritært valg og velger Hamdis forslag."
    else:
        konflikt2_konsekvens = "Passiv løsning: Konflikten mellom Hamdi og Jabir vokser, og det blir dårligere samarbeid. Prototypen blir forsinket."
        konflikt2_tekst = "Erling ignorerer konflikten og håper de finner ut av det selv."

    # Konflikt 3
    print("\nKonflikt 3:\nErling må bevare motivasjonen i teamet som helhet. Skal han sette av tid til relasjonsbygging og sosiale aktiviteter for å gjenopprette tillit, ")
    print ("eller skal han prioritere fremdrift og leveranser for å holde fokus på resultatet?\n")
    print("Valg:")
    print("a) Erling inviterer hele gruppen på bowling og sosiale aktiviteter for å styrke samholdet.")
    print("b) Erling prioriterer fremdrift og leveranser, og innfører lengre arbeidsdager med fokus på produktivitet.")
    print("c) Erling gjør ingen endringer og håper motivasjonen kommer tilbake av seg selv.")
    valg3 = hent_valg("Hva gjør Erling?", ["a", "b", "c"])

#Valg som personen har tatt lagres i variabler [3.0]
    if valg3 == "a":
        konflikt3_konsekvens = "God løsning: Gruppen får bedre samhold, motivasjonen øker, og alle jobber godt sammen."
        konflikt3_tekst = "Erling inviterer til bowling og sosiale aktiviteter."
    elif valg3 == "b":
        konflikt3_konsekvens = "Dårlig løsning: Gruppen blir slitne, motivasjonen faller, og stemningen blir dårlig."
        konflikt3_tekst = "Erling prioriterer kun fremdrift og leveranser."
    else:
        konflikt3_konsekvens = "Passiv løsning: Motivasjonen forblir lav, og prosjektet mister fremdrift."
        konflikt3_tekst = "Erling gjør ingen endringer og håper motivasjonen kommer tilbake."

    # Bestemer utfall
    if valg1 == "a" and valg2 == "a" and valg3 == "a":
        utfall = "Den gode slutt: Prosjektet lykkes, gruppen har høy moral og kommunen er svært fornøyd."
    elif valg1 == "b" and valg2 == "b" and valg3 == "b":
        utfall = "Den dårlige slutt: Prosjektet mislykkes, gruppen splittes og kommunen er skuffet."
    elif valg1 == "c" or valg2 == "c" or valg3 == "c":
        utfall = "Den dårlige slutt: Prosjektet stopper opp eller blir forsinket, og gruppen mister motivasjon."
    else:
        utfall = "Mellommådig slutt: Prosjektet leveres, men gruppen er ikke helt fornøyd og samarbeidet kunne vært bedre."

    # Sammendrag
    valg_dict = {
        "konflikt1_tekst": konflikt1_tekst,
        "konflikt1_valg": (
            "a) Inkluderer gruppen" if valg1 == "a" else
            "b) Autoritært valg for Silje" if valg1 == "b" else
            "c) Utsetter avgjørelsen"
        ),
        "konflikt1_konsekvens": konflikt1_konsekvens,
        "konflikt2_tekst": konflikt2_tekst,
        "konflikt2_valg": (
            "a) Inkluderer gruppen" if valg2 == "a" else
            "b) Autoritært valg for Hamdi" if valg2 == "b" else
            "c) Ignorerer konflikten"
        ),
        "konflikt2_konsekvens": konflikt2_konsekvens,
        "konflikt3_tekst": konflikt3_tekst,
        "konflikt3_valg": (
            "a) Bowling og sosialt" if valg3 == "a" else
            "b) Kun fremdrift og leveranser" if valg3 == "b" else
            "c) Gjør ingen endringer"
        ),
        "konflikt3_konsekvens": konflikt3_konsekvens,
        "utfall": utfall
    }

#Viser sammendrag
    vis_sammendrag(valg_dict)

main()
