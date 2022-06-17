# LOGISKE OPERATORER

# and: Binder flere betingelser sammen. Alle betingelser må være sanne for at uttrykket skal være sant
# or: Binder flere betingelser sammen. Minst én av betingelsene må være sanne for at uttrykket skal være sant
# not: Inverterer en betingelse (gjør True til False, og False til True). Betingelsen må være usann for at uttrykket skal være sant

# and
if True and True:
    print("Sant")

if True and False:
    print("Usant")

# or
if True or False:
    print("Sant")

if False or False:
    print("Usant")

if True or True:
    print("Sant")

# not
if not True:
    print("Usant")

if not False:
    print("Sant")

# Oppgave 1:
# Hva blir resultatet (True eller False) av følgende uttrykk:

a = (10 < 13) and (9 == 10)
b = (2 >= 4) or (5 > 3)
c = not (10 > 15)
d = (19 > 5) and (10 < 12)
e = (19 != 19) or (19 == 19)

# Oppgave 2:
# Hent brukernavn og passord fra bruker
# Hvis brukernavnet er 'admin' og passordet er 'admin123': skriv ut "Innlogging vellykket" til konsollen
# Hvis ikke: skriv ut "innlogging feilet" til konsollen

# Oppgave 3:
# Hent alder og antall år arbeidserfaring fra bruker
# Brukere som er over 50 år eller som har over 5 år med arbeidserfaring er kvalifiserte
# Sjekk om brukeren er kvalifisert og skriv ut resultatet til konsollen