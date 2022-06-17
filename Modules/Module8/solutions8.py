# Oppgave 1:

a = (10 < 13) and (9 == 10) # False
b = (2 >= 4) or (5 > 3) # True
c = not (10 > 15) # True
d = (19 > 5) and (10 < 12) # True
e = (19 != 19) or (19 == 19) # True

# Oppgave 2:

brukernavn = input("Brukernavn: ")
passord = input("Passord: ")

if brukernavn == "admin" and passord == "admin123":
    print("Innlogging vellykket")
else:
    print("Innlogging feilet")

# Oppgave 3:
alder = int(input("Alder: "))
antall_år_arbeidserfaring = int(input("Antall år arbeidserfaring: "))

if (alder > 50) or (antall_år_arbeidserfaring > 5):
    print("Du er kvalifisert")
else:
    print("Du er ikke kvalifisert")