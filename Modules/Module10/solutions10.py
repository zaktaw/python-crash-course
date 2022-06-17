# Oppgave 1:
for x in range(1, 101):
    print(x)

# Oppgave 2:
navn_liste = ["Alf", "Mari", "Nils", "Marianne", "Jonathan", "Marius", "Aurora"]

for navn in navn_liste:
    if navn.startswith("M"):
        print(navn)

# Oppgave 3:
# Hent tall bruker og legg de sammen
# Fortsett helt til brukeren skriver inn tallet 0
# Skriv ut slutt-resultatet til konsollen

total = 0
user_number = int(input("Nummer: "))

while user_number != 0:
    total += user_number
    user_number = int(input("Nummer: "))


print("Total: " + str(total))