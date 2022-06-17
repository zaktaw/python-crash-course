# Oppgave 1:

alder = int(input("Hvor gammel er du? "))
if alder >= 18:
    print("Du er myndig")

# Oppgave 2:

navn = input("Hva heter du? ")
navn_lengde = len(navn)

if navn_lengde > 9:
    print("Navnet ditt er for langt")
else:
    print("Navnet ditt er godkjent")

# Oppgave 3:

alder = int(input("Alder: "))

if alder < 18:
    print("Du kan ikke kjøpe øl eller sprit")
elif alder < 20:
    print("Du kan kjøpe øl, men ikke sprit")
else:
    print("Du kan kjøpe øl og sprit")