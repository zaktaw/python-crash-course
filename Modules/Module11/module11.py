# FUNKSJONER

# brukes for å definere kode som kan gjenbrukes

# definere funksjonen
def en_funksjon():
    print("Dette er en funksjon")

# kalle på funksjonen
en_funksjon()

# definere funksjon som tar inn argumenter
def addisjon(num1, num2):
    total = num1 + num2
    print(total)

addisjon(2, 5)

# definere funksjon som returnerer noe
def multiplikasjon(num1, num2):
    produkt = num1 * num2
    return produkt

produkt = multiplikasjon(5, 3)
print(produkt)

# Oppgave 1:
# Definer en funksjon som skriver ut "Hei, jeg heter Alf!" til konsollen
# Kall på funksjonen

# Oppgave 2:
# Definer en funksjon som tar inn et navn som argument og skriver ut "Hei, jeg heter " + navnet som ble gitt som argument
# Kall på funksjonen

# Oppgave 3:
# Definer en funksjon som
    # tar inn to tall
    # legger tallene sammen
    # returnerer resultatet
# Definer en til funksjon som regner ut kvadrat-tallet av et tall. Funksjonen skal
    # ta inn et tall
    # multiplisere tallet med seg selv
    # returnere resultatet
# Kall på den første funksjonen og bruk resultatet den returnerer som argument når du kaller på den andre funksjonen

# Oppgave 4:
# Definer en funksjon som tar inn et navn som argument og legger til navnet i en liste
# Definer en til funksjon som:
    # - Tar inn en bokstav
    # - Går gjennom listen med navn og skriver ut navnene som starter med bokstaven som ble gitt

# Oppgave 5:
# Lag et program som benytter funksjonene fra forrige oppgave
# Programmet skal legge til navn i listen så lenge brukeren skriver inn ikke-blankt navn
    # brukeren kan skrive et blankt navn ved å trykke på enter uten å skrive noe i input-feltet
# Programmet skal deretter ta inn en bokstav fra brukeren og skrive ut navnene som starter med denne bokstaven