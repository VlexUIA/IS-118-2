print("Introduksjon til historien\n")

# Spørsmål 1
svar1 = input("Spørsmål 1: Skriv 1 eller 2: ")

# Hvis man skriver noe feil (ikke 1 eller 2), så spør vi på nytt helt til det blir riktig
while svar1 != "1" and svar1 != "2":
    print("Skriv 1 eller 2.")
    svar1 = input("Spørsmål 1: Skriv 1 eller 2: ")

# Her lagres poengene for det første spørsmålet
if svar1 == "1":
    sporsmal1 = 1
    print("Forklaring for svar 1 i spørsmål 1\n")
else:
    sporsmal1 = 2
    print("Forklaring for svar 2 i spørsmål 1\n")


# Spørsmål 2
svar2 = input("Spørsmål 2: Skriv 1 eller 2: ")

# Sørger for at man ikke kan gå videre uten gyldig svar
while svar2 != "1" and svar2 != "2":
    print("Skriv 1 eller 2.")
    svar2 = input("Spørsmål 2: Skriv 1 eller 2: ")

if svar2 == "1":
    sporsmal2 = 1
    print("Forklaring for svar 1 i spørsmål 2\n")
else:
    sporsmal2 = 2
    print("Forklaring for svar 2 i spørsmål 2\n")


# Spørsmål 3
svar3 = input("Spørsmål 3: Skriv 1 eller 2: ")

# Samme sjekk her som på de andre
while svar3 != "1" and svar3 != "2":
    print("Skriv 1 eller 2.")
    svar3 = input("Spørsmål 3: Skriv 1 eller 2: ")

if svar3 == "1":
    sporsmal3 = 1
    print("Forklaring for svar 1 i spørsmål 3\n")
else:
    sporsmal3 = 2
    print("Forklaring for svar 2 i spørsmål 3\n")


# Avslutning og resultat
# Legger sammen poengene fra alle tre spørsmål
total = sporsmal1 + sporsmal2 + sporsmal3

print("=== Slutt ===")

# Sjekker hvor mange poeng man fikk for å velge riktig slutt
if total == 3:
    print("Slutt 1: Verste utfall")
elif total == 4 or total == 5:
    print("Slutt 2: Middels utfall")
else:
    print("Slutt 3: Beste utfall")
