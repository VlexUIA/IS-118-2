# Erlings valg

score = 0
Points = {1: 3, 2: 2, 3: 1}

Poengsum_riktig = 3
Poengsum_middels = 2
Poengsum_feil = 1

def pause(msg="Trykk Enter for å fortsette..."):
    input(msg)

import os 
import sys

def clear_screen():
    # Cross-platform clear using a single expression to avoid static analysis marking a branch as dead.
    os.system('cls' if os.name == 'nt' else 'clear')

# Tekstsvar for de ulike valgene
Svar1 = "Bra del 1"
Svar2 = "Middels del 1"
Svar3 = "Dårlig del 1"

Svar4 = "Bra del 2"
Svar5 = "Middels del 2"
Svar6 = "Dårlig del 2"

Svar7 = "Bra del 3"
Svar8 = "Middels del 3"
Svar9 = "Dårlig del 3"


# --------------- Historie om prosjektleder Erling ------------------
# --------------- Del 1 ------------------
print (
    "\nErling sitter foreløpig i en vanskelig situasjon med teamet hans."
)

print ("\nDu har følgende valg for å hjelpe ham:")

print (
    
    "\n1 - Be teamet om å jobbe overtid for å møte fristen."
    "\n2 - Gi teamet ekstra ressurser for å hjelpe til."
    "\n3 - Kommunisere med ledelsen for å justere fristen."
)

#1.1 Ugyldig input, feilmelding og nytt forsøk
while True:
    s = input("Hvilket valg bør han ta? (1, 2 eller 3): ").strip()
    try:
        First_choice = int(s)
    except ValueError:
        print("Ugyldig svar")
        continue
    if First_choice in (1, 2, 3):
        break
    print("Ugyldig svar")

#1.2 Gyldig valg og resultat   
if First_choice == 1:
    print(Svar1)
elif First_choice == 2:
    print(Svar2)
elif First_choice == 3:
    print(Svar3)
pause()
clear_screen()

#1.3 Poeng
score += Points.get(First_choice, 0)



# --------------- Del 2 av Erling sin situasjon ------------------
print (
    "\nMen etter ett problem blir løst, dukker et nytt opp. Blablabla disse to andre krangler også"
)

print ("\nDu har følgende valg for å hjelpe ham:")

print (

    "\n1 - Del 2 alternativ 1"
    "\n2 - Del 2 alternativ 2"
    "\n3 - Del 2 alternativ 3"
)

#2.1 Ugyldig input, feilmelding og nytt forsøk
while True:
    s = input("Hvilket valg bør han ta? (1, 2 eller 3): ").strip()
    try:
        Second_choice = int(s)
    except ValueError:
        print("Ugyldig svar")
        continue
    if Second_choice in (1, 2, 3):
        break
    print("Ugyldig svar")

#2.2 Gyldig valg og resultat   
if Second_choice == 1:
    print(Svar4)
elif Second_choice == 2:
    print(Svar5)
elif Second_choice == 3:
    print(Svar6)
pause()
clear_screen()

#2.3 Poeng
score += Points.get(Second_choice, 0)
   
    # --------------- Del 3 av Erling sin situasjon ------------------
print (
    "\nTil slutt må han løse problemet med motivasjonen til gruppen"
)

print ("\nDu har følgende valg for å hjelpe ham:")

print (
    
    "\n1 - Del 2 alternativ 1"
    "\n2 - Del 2 alternativ 2"
    "\n3 - Del 2 alternativ 3"
)
#3.1 Ugyldig input, feilmelding og nytt forsøk
while True:
    s = input("Hvilket valg bør han ta? (1, 2 eller 3): ").strip()
    try:
        Third_choice = int(s)
    except ValueError:
        print("Ugyldig svar")
        continue
    if Third_choice in (1, 2, 3):
        break
    print("Ugyldig svar")

#3.2 Gyldig valg og resultat   
if Third_choice == 1:
    print(Svar7)
elif Third_choice == 2:
    print(Svar8)
elif Third_choice == 3:
    print(Svar9)
pause()
clear_screen()

#3.3 Poeng
score += Points.get(Third_choice, 0)


# --------------- Avslutning ------------------
if score >= 8:
    print("Erling dreper ikke seg selv")
elif score >= 6:
    print("Erling overlever selvmordsforsøket sitt")
else:
    print("Erling klarer ikke å overleve selvmordsforsøket sitt, gratulerer!")
