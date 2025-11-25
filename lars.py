# Historie med valg for prosjektledelse

# Setter valg til 0 slik at vi kan summere dem senere
valg1 = 0

# Første scenario, gir input for hvike valg brukeren kan ta
print("Silje og Sivert har en uenighet om teknologivalg og design. Hvordan bør du løse konflikten? \n 1. " \
"Ta det opp i plenum \n 2. Ta et autoriært valg uten å konsultere dem")
v1 = int(input("Velger du nr 1 eller 2: "))
if v1 == 1:
    valg1 = valg1 + 1
elif v1 == 2:
    valg1 = valg1 + 2
# Hpndterer feil input og avslutter programmet
else:
    print("Feil input")
    exit()

# Gjør det samme for scenario 2 som i scenario 1
valg2 = 0

print("Sammtidig med konflikten mellom Silje og Sivert, har Hamdi og Jabir en uenighet om innbyggerenes innvolvering i digitale folkemøter \n Hva gjør du? \n" \
" 1. Sette opp et møte og bruke tid på å diskutere \n 2. Velge selv hva som er best for gruppen")
v2 = int(input("Velger du nr 1 eller 2: "))
if v2 == 1:
    valg2 = valg2 + 1
elif v2 == 2:
    valg2 = valg2 + 2
else:
    print("Feil input")
    exit()

# Gjør det samme for scenario 3 som i scenario 1 og 2
valg3 = 0
print("Erling må bevare motivasjonen i teamet som helhet. Hvordan gjør du dette? \n 1. " \
"Inviterer du hele gruppen til bowlign for å bygge lagånd \n 2. " \
"Sender en e-post hvor du sier at alle at de må jobbe hardere og lengre for å nå målene")
v3 = int(input("Enter a number: "))
if v3 == 1:
    valg3 = valg3 + 1
elif v3 == 2:
    valg3 = valg3 + 2
else:
    print("Invalid input")
    exit()

# Summerer opp valgene og gir en tilbakemelding basert på totalen
total = valg1 + valg2 + valg3

if total == 3:
    print("Valgene du tok gjorde at gruppen ferdigstilte prosjektet i tide og med god kvalitet!")
elif total == 4 or total == 5:
    print("Vaglene du tok førte til at prosjektet ble ferdig, men kvaliteten kunne vært bedre")
elif total == 6:
    print("Vlalgene du tok førte til at prosjektet ikke ble ferdigstilt i tide og kvaliteten var dårlig")
