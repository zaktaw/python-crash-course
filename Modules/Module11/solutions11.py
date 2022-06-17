# Oppgave 1:

def alf():
    print("Hei, jeg heter Alf!")

alf()

# Oppgave 2:

def skriv_ut_navn(navn):
    print("Hei, jeg heter " + navn)

skriv_ut_navn("Alf")

# Oppgave 3:

def addisjon(tall1, tall2):
    return tall1 + tall2

def kvadrat(tall):
    return tall * tall

tall = addisjon(5, 8)
kvadrat(tall)

# Oppgave 4:

navn_liste = []

def legg_til_navn(navn):
    navn_liste.append(navn)

def skriv_ut_navn(forbokstav):
    for navn in navn_liste:
        if (navn.startswith(forbokstav)):
            print(navn)

# Oppgave 5:

user_input = input("Navn: ")
navn_liste = []

while user_input != "":
    user_input = input("Navn: ")
    legg_til_navn(user_input)

forbokstav = input("Forbokstav: ")
skriv_ut_navn(forbokstav)
