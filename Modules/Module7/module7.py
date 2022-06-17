# IF-SETNINGER

# hvis betingelsen er sann, går vi inn i if-setningen og utfører koden der
if True:
    print("Dette vil bli skrevet ut til konsollen")

# hvis betingelsen er usann, går vi ikke inn i if-setningen
if False:
    print("Dette vil ikke bli skrevet ut til konsollen")

# Oppgave 1:
# Få tak i brukerens alder (input())
# Bruk en if-setning til å avgjøre om brukeren er myndig
# Tips: husk å konvere alder til int for at sammenlikningen skal fungere

# IF-ELSE

if True:
    print("Gjør dette hvis betingelsen er sann")
else:
    print("Gjør dette hvis betingelsen ikke er sann")

# Oppgave 2:
# Få tak i brukerens navn (input())
# Sjekk om brukerens navn er lenger enn 9 bokstaver
# Hvis det er det: skriv ut "Navnet ditt er for langt"
# Hvis det ikke er det: skriv ut "Navnet ditt er godkjent"
# tips:
navn = "Hans"
navn_lengde = len(navn) # lengde: 4

# IF-ELIF-ELSE

if False:
    print("Dette vil ikke bli skrevet ut")
elif False:
    print("Dette vil heller ikke bli skrevet ut")
else:
    print("Dette vil bli skrevet ut")

# Oppgave 3:
# Få tak i brukerens alder
# Hvis brukeren er under 18 år: skriv ut "Du kan ikke kjøpe øl eller sprit"
# Hvis brukeren er over 18, men under 20: skriv ut "Du kan kjøpe øl, men ikke sprit"
# Hvis brukeren er over 20: skriv ut "Du kan kjøpe øl og sprit"