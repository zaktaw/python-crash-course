# LØKKER / LOOPS

# Bruker for å gjøre en operasjon gjentatte ganger
# To forskjellige løkker: for og while
# For-løkke brukes for å gjøre et forhåndsbestemt antall operasjoner
# While-løkke brukes for å gjøre operajsoner så lenge en betingelse er sann

# FOR-LØKKE

# skrive ut alle elementer i en liste
bokstaver = ["A", "B", "C", "E"]
for bokstav in bokstaver:
    print(bokstav)

# skrive ut tall fra og med x til 10
for x in range(1, 10):
    print(x)

# Oppgave 1:
# Skriv ut alle tallene fra og med 1 til og med 100 til konsollen

# Oppgave 2:
navn_liste = ["Alf", "Mari", "Nils", "Marianne", "Jonathan", "Marius", "Aurora"]
# bruk en for-løkke til å skrive ut navnene som begynner med bokstaven M
# Tips: 
a = "Marius"
print(a.startswith("M")) # True

# WHILE-LØKKE

# Løkke som kjører for alltid
while True:
    print("Hei!")

# Løkke som kjører så lenge num er mindre enn 10
# Skriver ut tall fra og med 0 til 10
num = 0
while num < 10:
    print(num)
    num += 1

# Oppgave 3:
# Hent tall bruker og legg de sammen
# Fortsett helt til brukeren skriver inn tallet 0
# Skriv ut slutt-resultatet til konsollen